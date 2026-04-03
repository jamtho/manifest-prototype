"""Tests for MCP server helper functions."""

import duckdb
import pytest

from manifest.server import (
    _format_csv,
    _format_markdown_table,
    _summarise_query,
    _template_to_glob,
)


# ---------------------------------------------------------------------------
# _template_to_glob
# ---------------------------------------------------------------------------


class TestTemplateToGlob:
    def test_inline_placeholder(self):
        assert _template_to_glob("ais-{date}.parquet") == "ais-*.parquet"

    def test_full_segment_placeholder(self):
        assert _template_to_glob("{stream}/data.parquet") == "**/data.parquet"

    def test_mixed(self):
        # {year} occupies the full segment -> **, {date} is inline -> *
        result = _template_to_glob("broadcasts/{year}/ais-{date}.parquet")
        assert result == "broadcasts/**/ais-*.parquet"

    def test_hive_style(self):
        result = _template_to_glob("data/parquet/{stream}/dt={date}/hour={hour}.parquet")
        assert result == "data/parquet/**/dt=*/hour=*.parquet"

    def test_no_placeholders(self):
        assert _template_to_glob("data/file.parquet") == "data/file.parquet"


# ---------------------------------------------------------------------------
# _format_markdown_table
# ---------------------------------------------------------------------------


class TestFormatMarkdown:
    def test_basic(self):
        result = _format_markdown_table(["a", "b"], [(1, "x"), (2, "y")])
        lines = result.split("\n")
        assert lines[0] == "| a | b |"
        assert lines[1] == "| --- | --- |"
        assert lines[2] == "| 1 | x |"
        assert lines[3] == "| 2 | y |"
        assert len(lines) == 4

    def test_null_values(self):
        result = _format_markdown_table(["col"], [(None,)])
        assert "NULL" in result

    def test_empty_rows(self):
        result = _format_markdown_table(["col"], [])
        lines = result.split("\n")
        assert len(lines) == 2  # header + separator only


# ---------------------------------------------------------------------------
# _format_csv
# ---------------------------------------------------------------------------


class TestFormatCsv:
    def test_basic(self):
        result = _format_csv(["a", "b"], [(1, "hello"), (2, "world")])
        lines = result.split("\n")
        assert lines[0] == "a,b"
        assert lines[1] == "1,hello"
        assert lines[2] == "2,world"

    def test_null_values(self):
        result = _format_csv(["col"], [(None,), ("val",)])
        lines = result.split("\n")
        # None renders as empty string; csv.writer may quote it
        assert lines[1].strip('"') == ""
        assert lines[2] == "val"

    def test_value_with_comma(self):
        result = _format_csv(["col"], [("a,b",)])
        lines = result.split("\n")
        assert lines[1] == '"a,b"'

    def test_value_with_quotes(self):
        result = _format_csv(["col"], [('say "hi"',)])
        lines = result.split("\n")
        assert '"say ""hi"""' in lines[1]

    def test_no_trailing_newline(self):
        result = _format_csv(["a"], [(1,)])
        assert not result.endswith("\n")


# ---------------------------------------------------------------------------
# _summarise_query
# ---------------------------------------------------------------------------


@pytest.fixture
def db():
    conn = duckdb.connect(":memory:")
    conn.execute(
        """CREATE TABLE sample AS
           SELECT i::INTEGER AS id,
                  CASE WHEN i % 3 = 0 THEN NULL ELSE chr(65 + (i % 26)::INTEGER) END AS letter,
                  (i * 1.1)::DOUBLE AS val
           FROM generate_series(1, 100) AS s(i)"""
    )
    yield conn
    conn.close()


class TestSummariseQuery:
    def test_returns_summary_table(self, db):
        result = _summarise_query(db, "SELECT * FROM sample")
        assert "**Full result summary:**" in result
        assert "column_name" in result
        assert "column_type" in result
        # All three columns should appear
        assert "| id " in result
        assert "| letter " in result
        assert "| val " in result

    def test_includes_null_percentage(self, db):
        result = _summarise_query(db, "SELECT * FROM sample")
        # letter has ~33% nulls (every 3rd row)
        assert "null_percentage" in result

    def test_invalid_sql_returns_empty(self, db):
        result = _summarise_query(db, "SELECT * FROM nonexistent")
        assert result == ""

    def test_empty_result(self, db):
        result = _summarise_query(db, "SELECT * FROM sample WHERE false")
        # SUMMARIZE on empty result may return column info or nothing
        # either way, it shouldn't crash
        assert isinstance(result, str)
