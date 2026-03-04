# Agent Guidelines

## Language and tooling

- Python 3.11+
- Use `uv` for dependency management and running commands (`uv run`, `uv sync`)
- Prefer type hints on all function signatures and return types
- Use `rdflib` for RDF/Turtle handling, `duckdb` for data queries, `pyarrow` for Parquet metadata

## Code style

- Keep it simple. Don't add abstractions, helpers, or configurability beyond what's needed now
- Don't add docstrings, comments, or type annotations to code you didn't change
- Only add comments where the logic isn't self-evident
- Prefer editing existing files over creating new ones

## Testing

- Write tests for new functionality using `pytest`
- Run tests before declaring work done: `uv run pytest`
- If tests fail, fix them — don't mark tasks as complete with failing tests

## Git

- Commit regularly with clear, concise messages
- Write commit messages as a human would — no "Co-Authored-By: Claude" or similar AI attribution lines
- Stage specific files, not `git add -A`
- Don't amend commits unless explicitly asked
- Don't force push

## Project conventions

- Vocabulary definitions go in `vocabularies/`
- Domain descriptions go in `descriptions/`
- Documentation goes in `docs/`
- The `sdl/` package contains the Python toolkit (graph loader, validators, CLI)
- Namespace prefixes used in `.ttl` files must be registered in `sdl/graph.py` (module constant, `_str()`, `__init__()` bind, `_resolve_uri()` ns_map)
