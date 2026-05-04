# Beaver Dataset Description

*Generated from `beaver_description.ttl` — do not edit.*

## Datasets

| Dataset | Row Semantics | Schema | Partitioning | Format |
|---------|---------------|--------|--------------|--------|
| keystone.user — abstract user identity | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.local_user — local-identity specialisation | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.federated_user — federated-identity specialisation (EMPTY) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.password — credentials (heavily anonymised) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.group — identity groups (MySQL RESERVED WORD) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.user_group_membership — group memberships | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.project — tenants (and domains, see duality) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.domain — top-level identity containers (domain-as-project duality) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.role — named roles | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.assignment — authorisation edges (polymorphic) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.trust — time-bounded role delegations | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.trust_role — roles granted within a trust | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.credential — additional credentials (EC2 only here) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.region — endpoint geographic grouping | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.service — OpenStack service catalogue | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.endpoint — service URL bindings per region | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.revocation_event — token revocation history | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.identity_provider — federation IdPs (EMPTY) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.federation_protocol — federation protocols (EMPTY) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.mapping — federation attribute mapping (EMPTY) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| keystone.idp_remote_ids — federation remote-id list (EMPTY) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw — database-level catalogue (synthetic) | mnf:AggregateRow | — | — | Database catalogue (INFORMATION_SCHEMA + sidecar) |
| dw.buildings — addressable buildings (simple shape) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fac_building — buildings with rich attributes (FAC_-keyed) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_building — buildings with rich attributes (FCLT_-keyed) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_building_address — addresses by purpose (FCLT-keyed) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fac_building_address — addresses by purpose (FAC-keyed) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fac_rooms — room inventory (granular, includes service spaces) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_rooms — curated room inventory (FCLT-keyed) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.space_detail — leaner space inventory (third representation) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fac_floor — floor records (FAC-keyed) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_floor — floor records (FCLT-keyed) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.space_floor — floor-name dictionary | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_major_use — MAJOR_USE_DESC code legend | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.space_usage — granular room-purpose taxonomy | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.space_unit — DLC mapping (proper-case names) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.space_unit2 — DLC mapping (uppercase abbreviated) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.space_supervisor_usage — pre-aggregated per-supervisor metrics | mnf:AggregateRow | mnf:FixedSchema | — | MySQL Table |
| dw.master_dept_hierarchy — DLC org tree (5-level path) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.master_dept_hierarchy_links — DLC↔external-system cross-refs | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.master_dept_dcode_parent — adjacency-list parent pointers | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.sis_department — academic-side department catalogue | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.sis_admin_department — admin-office catalogue | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_organization — facilities org table (DLC-aware) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fac_organization — facilities org table (D_CODE-style) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_org_dlc_key — explicit FCLT_ORGANIZATION_KEY ↔ DLC_KEY bridge | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.hr_org_unit — HR org units (older system) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.hr_org_unit_new — HR org units (current; superset) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.subject_offered — subject sections per term | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.subject_offered_summary — per-(subject, term) summary | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.course_catalog_subject_offered — recent year-scoped catalogue | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.cis_course_catalog — older CIS course catalogue | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.cis_hass_attribute — HASS attribute taxonomy lookup | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.sis_course_description — canonical course descriptor (with TYPO COLUMN) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.sis_subject_code — subject-code prefix → dept+school | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.iap_subject_detail — IAP activity registry (2021JA snapshot only) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.iap_subject_person — IAP person/role records | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.iap_subject_session — IAP session schedule | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.iap_subject_sponsor — IAP activity sponsor catalogue | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.iap_subject_category — IAP category labels | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.library_subject_offered — library's per-(subject, term) view (2009-2021) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.library_course_instructor — instructor↔course assignments | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.library_reserve_catalog — library catalogue records | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.library_reserve_matrl_detail — pure linkage table (5 keys per row) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.library_material_status — 6-value status lookup | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.tip_subject_offered — TIP per-(subject, term) (2024+ only) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.tip_detail — TIP join table | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.tip_material — textbook records with prices | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.tip_material_status — 12-value status lookup with data-quality blips | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.employee_directory — MIT phonebook (Namespace A) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.drupal_employee_directory — Drupal-published mirror | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.mit_student_directory — student phonebook (NO MIT_ID) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.se_person — payroll-flavoured people (Namespace B) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.hr_faculty_roster — faculty-only HR view (Namespace B) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.warehouse_users — staff + students union (Namespace B) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.person_auth_area — auth flags by KRB_NAME (UPPERCASE) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.student_department — student-side dept catalogue | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.academic_terms_all — canonical term catalogue (300 rows, 1951-2030) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.academic_terms — current-relevant term subset (144 rows) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.academic_term_parameter — pointer to current/previous/upcoming terms | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.time_day — daily fact table with fiscal/calendar/academic context | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.time_month — monthly granularity with fiscal context | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.time_quarter — quarterly granularity (fiscal + calendar) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.mit_holiday_closing_calendar — MIT closures | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.frc_fiscal_periods — FY 2025 fiscal periods (incl. adjustments 13-16) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.moira_list — Moira mailing-list catalogue (with DUPLICATES) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.moira_list_detail — list memberships (one (list, member) per row) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.moira_list_owner — owner identity catalogue (NOT keyed by list) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.cip — Federal CIP program taxonomy (4 editions stacked) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.zpm_rooms_load — SAP ZPM room/HR-org-unit binding | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.roles_fin_pa — financial-PA roles by user (lowercase KRB) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.estimated_surcharges_estonly — schema stub (empty in this dump) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fund_center_hierarchy — schema stub (empty in this dump) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.opa_person_current — schema stub (empty in this dump) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.profit_center_group — schema stub (empty in this dump) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.subject_selector — schema stub (empty in this dump) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_building_address_hist — schema stub (SCD-2 history table — vocab gap (GAP-16)) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_building_hist — schema stub (SCD-2 history table — vocab gap (GAP-16)) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_building_hist_1 — schema stub (SCD-2 history table — vocab gap (GAP-16)) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_floor_hist — schema stub (SCD-2 history table — vocab gap (GAP-16)) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_major_use_hist — schema stub (SCD-2 history table — vocab gap (GAP-16)) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_organization_hist — schema stub (SCD-2 history table — vocab gap (GAP-16)) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fclt_rooms_hist — schema stub (SCD-2 history table — vocab gap (GAP-16)) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.drupal_course_catalog — schema stub (cross-system mirror (see GAP-23)) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.cip_with_version — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.fac_major_use — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.ir_institution — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.sis_lookup — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.sis_term_address_category — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.student_degree_program — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.student_ethnic_subgroup — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.subject_attribute — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.subject_enrollable — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.subject_grouping — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.subject_iap_schedule — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.subject_summary — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.top_level_domain — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.zip_canada — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |
| dw.zip_usa — schema stub (reference / lookup) | mnf:EventRow | mnf:FixedSchema | — | MySQL Table |

---

## keystone.user — abstract user identity

**URI:** `ks:user`
  
[BVT-K-GAP-1] Snapshot row count: 944. The abstract user identity. Specialised by local_user (1:1) or federated_user (empty in this dump). NB: NO `name` column — names live in local_user.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/user`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `default_project_id` | mnf:Varchar | ks:ProjectId | yes |
| `enabled` | mnf:Integer | bvtk:MySQLBoolean | yes |
| `extra` | mnf:Varchar | bvtk:JSONInString | yes |
| `id` | mnf:Varchar | ks:UserId | no |

### Derivations

| Derived Column | Source Columns | Function | Properties |
|----------------|----------------|----------|------------|
| `extra` |  | bvtk:KeystoneEmailAnonymisation | mnf:Deterministic, mnf:Lossy |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| severe | user.default_project_id is non-null on 940 of 944 users; ZERO of these resolve to a real project.id. Anonymisation re-randomised user-side and project-side ids independently. |

---

## keystone.local_user — local-identity specialisation

**URI:** `ks:local_user`
  
[BVT-K-GAP-1] Snapshot row count: 944, strict 1:1 with user. Names live here. The `id` column is a surrogate auto-increment int — references from elsewhere use either `user_id` (varchar, the FK back to user) OR `id` (int, FK target for password.local_user_id).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/local_user`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `domain_id` | mnf:Varchar | ks:DomainId | no |
| `id` | mnf:Integer | ks:LocalUserSurrogateId | no |
| `name` | mnf:Varchar | ks:AnonymisedName | no |
| `user_id` | mnf:Varchar | ks:UserId | no |

### Derivations

| Derived Column | Source Columns | Function | Properties |
|----------------|----------------|----------|------------|
| `name` |  | bvtk:KeystoneWordPairAnonymisation | mnf:Deterministic, mnf:Lossy |

---

## keystone.federated_user — federated-identity specialisation (EMPTY)

**URI:** `ks:federated_user`
  
Schema-present but row-empty in this dump. Federation is not configured in this deployment, so no users are federated. SQL against this table parses and runs but returns no rows.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/federated_user`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `display_name` | mnf:Varchar |  | yes |
| `id` | mnf:Integer |  | no |
| `idp_id` | mnf:Varchar |  | no |
| `protocol_id` | mnf:Varchar |  | no |
| `unique_id` | mnf:Varchar |  | no |
| `user_id` | mnf:Varchar | ks:UserId | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Federation tables (federated_user, identity_provider, federation_protocol, mapping, idp_remote_ids) are schema-present but empty in this dump. Federation is not configured in this deployment. |

---

## keystone.password — credentials (heavily anonymised)

**URI:** `ks:password`
  
[BVT-K-GAP-1] Snapshot row count: 944, strict 1:1 with local_user. Older keystone schema — only 3 columns. Modern deployments would have password_hash, expires_at, self_service — they're absent here.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/password`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `id` | mnf:Integer |  | no |
| `local_user_id` | mnf:Integer | ks:LocalUserSurrogateId | no |
| `password` | mnf:Varchar | ks:AnonymisedPassword | yes |

### Derivations

| Derived Column | Source Columns | Function | Properties |
|----------------|----------------|----------|------------|
| `password` | `local_user_id` | bvtk:KeystonePasswordAnonymisation | mnf:Deterministic, mnf:Lossy |

---

## keystone.group — identity groups (MySQL RESERVED WORD)

**URI:** `ks:group`
  
Single group named `proto4` in this dump. `group` is a MySQL reserved word — every reference in SQL must be backticked (`` `group` ``) or the parser will error.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/group`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `description` | mnf:Varchar |  | yes |
| `domain_id` | mnf:Varchar | ks:DomainId | no |
| `extra` | mnf:Varchar | bvtk:JSONInString | yes |
| `id` | mnf:Varchar | ks:GroupId | no |
| `name` | mnf:Varchar | ks:AnonymisedName | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| severe | `group` is a MySQL reserved word. Any unquoted reference parses as a syntax error. Must be backticked (`` `group` ``) or wrapped in a subquery / aliased. |

---

## keystone.user_group_membership — group memberships

**URI:** `ks:user_group_membership`
  
[BVT-K-GAP-1] Snapshot row count: 10, all to the single `proto4` group. Both columns are declared FKs.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/user_group_membership`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `group_id` | mnf:Varchar | ks:GroupId | no |
| `user_id` | mnf:Varchar | ks:UserId | no |

---

## keystone.project — tenants (and domains, see duality)

**URI:** `ks:project`
  
[BVT-K-GAP-1] Snapshot row count: 923. Self- referential: `domain_id` and `parent_id` both FK back to `project.id`. 3 rows have `is_domain=1` and parent_id=NULL — these are the domain-as-project rows. See ks:domain_project_duality.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/project`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `description` | mnf:Varchar |  | yes |
| `domain_id` | mnf:Varchar | ks:ProjectId | no |
| `enabled` | mnf:Integer | bvtk:MySQLBoolean | yes |
| `extra` | mnf:Varchar | bvtk:JSONInString | yes |
| `id` | mnf:Varchar | ks:ProjectId | no |
| `is_domain` | mnf:Integer | bvtk:MySQLBoolean | no |
| `name` | mnf:Varchar | ks:AnonymisedName | no |
| `parent_id` | mnf:Varchar | ks:ProjectId | yes |

---

## keystone.domain — top-level identity containers (domain-as-project duality)

**URI:** `ks:domain`
  
[BVT-K-GAP-1] Snapshot row count: 3. Same ids as the three `project` rows where `is_domain=1`. The `domain` table kept the real names ('Default', 'heat'); the twin project rows were anonymised. See ks:domain_project_duality.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/domain`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `enabled` | mnf:Integer | bvtk:MySQLBoolean | no |
| `extra` | mnf:Varchar | bvtk:JSONInString | yes |
| `id` | mnf:Varchar | ks:DomainId | no |
| `name` | mnf:Varchar |  | no |

---

## keystone.role — named roles

**URI:** `ks:role`
  
[BVT-K-GAP-1] Snapshot row count: 6. UNIQUE on (name, domain_id). Names are anonymised except 'xenon' (the OpenStack default-member role kept its description JSON, which gives away the real role).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/role`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `domain_id` | mnf:Varchar |  | no |
| `extra` | mnf:Varchar | bvtk:JSONInString | yes |
| `id` | mnf:Varchar | ks:RoleId | no |
| `name` | mnf:Varchar | ks:AnonymisedName | no |

### Derivations

| Derived Column | Source Columns | Function | Properties |
|----------------|----------------|----------|------------|
| `name` |  | bvtk:KeystoneWordPairAnonymisation | mnf:Deterministic, mnf:Lossy |

---

## keystone.assignment — authorisation edges (polymorphic)

**URI:** `ks:assignment`
  
[BVT-K-GAP-1] Snapshot row count: 3,433 (largest keystone table). Polymorphic on `type` — actor_id resolves to user.id (when type LIKE 'User%') or group.id (when type LIKE 'Group%'); target_id resolves to project.id or domain.id. 99.5% are UserProject; 1 UserDomain, 0 GroupDomain. See [BVT-K-GAP-3].
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/assignment`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `actor_id` | mnf:Varchar |  | no |
| `inherited` | mnf:Integer | bvtk:MySQLBoolean | no |
| `role_id` | mnf:Varchar | ks:RoleId | no |
| `target_id` | mnf:Varchar |  | no |
| `type` | mnf:Varchar | ks:AssignmentType | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
|  |  |

---

## keystone.trust — time-bounded role delegations

**URI:** `ks:trust`
  
[BVT-K-GAP-1] Snapshot row count: 82, of which 75 are soft-deleted (deleted_at NOT NULL). 83% are auto-generated by Heat orchestration (extra carries 'heat_stack_owner' as a role name not present in role table). All four user/project references are soft FKs.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/trust`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `deleted_at` | mnf:Varchar |  | yes |
| `expires_at` | mnf:Varchar |  | yes |
| `extra` | mnf:Varchar | bvtk:JSONInString | yes |
| `id` | mnf:Varchar |  | no |
| `impersonation` | mnf:Integer | bvtk:MySQLBoolean | yes |
| `project_id` | mnf:Varchar | ks:ProjectId | yes |
| `remaining_uses` | mnf:Integer |  | yes |
| `trustee_user_id` | mnf:Varchar | ks:UserId | no |
| `trustor_user_id` | mnf:Varchar | ks:UserId | no |

---

## keystone.trust_role — roles granted within a trust

**URI:** `ks:trust_role`
  
[BVT-K-GAP-1] Snapshot row count: 96. Every trust has at least one trust_role row.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/trust_role`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `role_id` | mnf:Varchar | ks:RoleId | no |
| `trust_id` | mnf:Varchar |  | no |

---

## keystone.credential — additional credentials (EC2 only here)

**URI:** `ks:credential`
  
[BVT-K-GAP-1] Snapshot row count: 144. All rows have type='ec2'. PK is 64-char hex (sha256-shaped, NOT 32 like every other keystone id). 1 of 144 user_id references is orphan.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/credential`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `blob` | mnf:Varchar | bvtk:JSONInString | no |
| `extra` | mnf:Varchar | bvtk:JSONInString | yes |
| `id` | mnf:Varchar | bvtk:Sha256Hex | no |
| `project_id` | mnf:Varchar | ks:ProjectId | yes |
| `type` | mnf:Varchar | ks:CredentialType | no |
| `user_id` | mnf:Varchar | ks:UserId | no |

### Derivations

| Derived Column | Source Columns | Function | Properties |
|----------------|----------------|----------|------------|
| `blob` | `id` | bvtk:KeystoneCredentialAnonymisation | mnf:Deterministic, mnf:Lossy |

---

## keystone.region — endpoint geographic grouping

**URI:** `ks:region`
  
[BVT-K-GAP-1] Snapshot row count: 2. Real names retained: 'CSAIL_Stata', 'MOC_Kaizen'. NB: `id` IS the human-readable name, not a UUID.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/region`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `description` | mnf:Varchar |  | yes |
| `extra` | mnf:Varchar | bvtk:JSONInString | yes |
| `id` | mnf:Varchar | ks:RegionId | no |
| `parent_region_id` | mnf:Varchar | ks:RegionId | yes |

---

## keystone.service — OpenStack service catalogue

**URI:** `ks:service`
  
All 15 services are enabled. Service `type` values are real (NOT anonymised) — the canonical lookup key. The set of types tells consumers which OpenStack components ran in this deployment (nova / neutron / cinder / glance / keystone).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/service`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `enabled` | mnf:Integer | bvtk:MySQLBoolean | no |
| `extra` | mnf:Varchar |  | yes |
| `id` | mnf:Varchar |  | no |
| `type` | mnf:Varchar | ks:ServiceType | no |

---

## keystone.endpoint — service URL bindings per region

**URI:** `ks:endpoint`
  
[BVT-K-GAP-1] Snapshot row count: 46, all enabled. Three interfaces (public/internal/admin) per (service, region) in the typical pattern.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/endpoint`
  
**Entity key:** `id`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `enabled` | mnf:Integer | bvtk:MySQLBoolean | no |
| `extra` | mnf:Varchar | bvtk:JSONInString | yes |
| `id` | mnf:Varchar |  | no |
| `interface` | mnf:Varchar | ks:EndpointInterface | no |
| `legacy_endpoint_id` | mnf:Varchar |  | yes |
| `region_id` | mnf:Varchar | ks:RegionId | no |
| `service_id` | mnf:Varchar |  | no |
| `url` | mnf:Varchar |  | no |

---

## keystone.revocation_event — token revocation history

**URI:** `ks:revocation_event`
  
[BVT-K-GAP-1] Snapshot row count: 1. 13 columns, most of which are nullable polymorphic-ish references (domain_id, project_id, user_id, role_id, trust_id, consumer_id, access_token_id) — a revocation can target any of these. Only `id`, `revoked_at`, and `issued_before` are NOT NULL.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/revocation_event`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `audit_id` | mnf:Varchar |  | yes |
| `id` | mnf:Integer |  | no |
| `revoked_at` | mnf:Varchar |  | no |

---

## keystone.identity_provider — federation IdPs (EMPTY)

**URI:** `ks:identity_provider`
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/identity_provider`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `description` | mnf:Varchar |  | yes |
| `enabled` | mnf:Integer | bvtk:MySQLBoolean | no |
| `id` | mnf:Varchar |  | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Federation tables (federated_user, identity_provider, federation_protocol, mapping, idp_remote_ids) are schema-present but empty in this dump. Federation is not configured in this deployment. |

---

## keystone.federation_protocol — federation protocols (EMPTY)

**URI:** `ks:federation_protocol`
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/federation_protocol`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `id` | mnf:Varchar |  | no |
| `idp_id` | mnf:Varchar |  | no |
| `mapping_id` | mnf:Varchar |  | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Federation tables (federated_user, identity_provider, federation_protocol, mapping, idp_remote_ids) are schema-present but empty in this dump. Federation is not configured in this deployment. |

---

## keystone.mapping — federation attribute mapping (EMPTY)

**URI:** `ks:mapping`
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/mapping`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `id` | mnf:Varchar |  | no |
| `rules` | mnf:Varchar | bvtk:JSONInString | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Federation tables (federated_user, identity_provider, federation_protocol, mapping, idp_remote_ids) are schema-present but empty in this dump. Federation is not configured in this deployment. |

---

## keystone.idp_remote_ids — federation remote-id list (EMPTY)

**URI:** `ks:idp_remote_ids`
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://keystone/idp_remote_ids`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `idp_id` | mnf:Varchar |  | yes |
| `remote_id` | mnf:Varchar |  | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Federation tables (federated_user, identity_provider, federation_protocol, mapping, idp_remote_ids) are schema-present but empty in this dump. Federation is not configured in this deployment. |

---

## dw — database-level catalogue (synthetic)

**URI:** `dw:DatabaseCatalogue`
  
A synthetic "facts about DW" pseudo-dataset — captures the cluster taxonomy, the fac_*/fclt_* duality, prefix conventions, and per-table row counts that don't fit into any single real table. Stored conceptually in INFORMATION_SCHEMA + the dw_join_keys.json sidecar that ships with the upstream schema dump. Database shape (snapshot): * 97 tables, ~9.84M rows total * NO declared PKs / FKs in the upstream schema; all relationships are soft (annotated `mnf:declared false` in the FK records below) * 1,034 join-key pairs documented in upstream/dw_join_keys.json * 5 tables empty in this dump: estimated_surcharges_estonly, fund_center_hierarchy, opa_person_current, profit_center_group, subject_selector Cluster taxonomy: * Facilities (buildings, floors, rooms, space-*): ~24 tables * Subjects / courses / catalogues: ~16 tables * Library + TIP: ~9 tables * Moira / mailing lists: 5 tables * Departments / orgs: ~7 tables (DLC = Department / Lab / Center) * IAP (Independent Activities Period): 5 tables * People (employees / students / instructors): ~8 tables * Terms / academic calendar: 3 tables * Time dimensions: 4 tables * Geo (zip / domain lookups): 3 tables (zip_canada at 873K rows is surprisingly large) * Miscellaneous / staging / empty: ~13 tables Upstream-system prefix legend (the leading underscore-delimited token of a table name typically identifies its source system): * cip* — Classification of Instructional Programs (federal) * cis_ — Course Information System * drupal_ — Drupal CMS (publishable mirror feeds) * frc_ — Financial Reporting Cube * hr_ — HR system * iap_ — Independent Activities Period * ir_ — Institutional Research * mit_ — MIT-specific directories * moira_ — Moira (Athena identity / mailing lists) * se_ — Student Engagement * sis_ — Student Information System * time_ — date dimensions * tip_ — Textbook Information Project * zpm_ — SAP ZPM module The fac_* / fclt_* duality (see dw:fac_fclt_duality): * `buildings` (211 rows): only addressable buildings, simple shape * `fac_*` family (~9 tables): keyed by BUILDING_KEY, plain style * `fclt_*` family (~13 tables + _hist): keyed by FCLT_BUILDING_KEY, richer / more denormalised * `fclt_*_hist` are SCD-2 history tables; `fclt_rooms_hist` is ~5M rows — by far the largest table in dw Schema interpretation: each row of this conceptual dataset is one table in dw. The columns below describe per-table structural facts. Narrative cluster / prefix / duality material that doesn't fit a tabular schema lives in this rdfs:comment.
  
**Row semantics:** mnf:AggregateRow

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `cluster` | mnf:Varchar |  | yes |
| `column_count` | mnf:Integer |  | yes |
| `is_empty` | mnf:Integer | bvtk:MySQLBoolean | no |
| `prefix_namespace` | mnf:Varchar |  | yes |
| `row_count` | mnf:BigInt |  | yes |
| `table_name` | mnf:Varchar | bvtk:MySQLIdentifier | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| severe | [BVT-K-GAP-17] No PRIMARY KEY or FOREIGN KEY declarations are present in upstream/dev_tables.json for any dw table. Relationships have to be inferred from upstream/dw_join_keys.json (1034 join-key pairs) plus knowledge investigations. Every FK in the dw section above is a soft FK [BVT-K-GAP-4]. |
| moderate | [BVT-K-GAP-12] Column types in upstream/dev_tables.json use Oracle types (VARCHAR2, NUMBER, DATE) but the live database is MySQL (varchar, int, datetime). The CREATE TABLE strings the prompt builder renders are Oracle-flavoured even though they're executed against MySQL. Same root cause as the bvt_description.ttl deficiency_dialect_mismatch. |
| moderate | Some tables in dw are present as schema-only stubs (column names + types) without rich annotation — anonymisation flags, cross-namespace bridges, sentinel values, case conventions, etc. See PART X (Schema stubs) for the full list. |
| minor | [BVT-K-GAP-19] dw:DatabaseCatalogue is a Manifest Dataset by necessity, not by fit. mnf has no concept of "database-level metadata" (table list, cluster taxonomy, prefix legend, top-table-hit counts). We model it as a synthetic dataset where each row is one table in dw — the columns describe per-table structural facts, but no row-level data is loaded. The narrative facts (cluster sizes, prefix conventions) live in the rdfs:comment because they don't fit any column. |

---

## dw.buildings — addressable buildings (simple shape)

**URI:** `dw:buildings`
  
[BVT-K-GAP-1] Snapshot row count: 211. Smallest of the three building tables. Includes only addressable buildings (no wings/annexes — those folded into parents). Carries BUILDING_STREET_ADDRESS denormalised.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/buildings`
  
**Entity key:** `BUILDING_KEY`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `BLDG_ASSIGNABLE_SQUARE_FOOTAGE` | mnf:Double |  | yes |
| `BLDG_GROSS_SQUARE_FOOTAGE` | mnf:Double |  | yes |
| `BUILDING_COUNTER` | mnf:Integer |  | yes |
| `BUILDING_KEY` | mnf:Varchar | dw:BuildingNumber | no |
| `BUILDING_NAME` | mnf:Varchar |  | yes |
| `BUILDING_STREET_ADDRESS` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar | bvtk:OracleShortDateString | yes |

---

## dw.fac_building — buildings with rich attributes (FAC_-keyed)

**URI:** `dw:fac_building`
  
[BVT-K-GAP-1 / BVT-K-GAP-11] Snapshot row count: 242. Same data as fclt_building on all 32 shared columns; differs only in PK column name (FAC_BUILDING_KEY vs FCLT_BUILDING_KEY). See dw:fac_fclt_duality.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fac_building`
  
**Entity key:** `FAC_BUILDING_KEY`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `BUILDING_NAME` | mnf:Varchar |  | yes |
| `BUILDING_NAMED_FOR` | mnf:Varchar |  | yes |
| `BUILDING_NAME_LONG` | mnf:Varchar |  | yes |
| `BUILDING_NUMBER` | mnf:Varchar | dw:BuildingNumber | no |
| `BUILDING_TYPE` | mnf:Varchar | dw:BuildingType | yes |
| `BUILDING_USE` | mnf:Varchar | dw:BuildingUse | yes |
| `CAMPUS_SECTOR` | mnf:Varchar | dw:CampusSector | yes |
| `DATE_ACQUIRED` | mnf:Varchar | bvtk:USDateString | yes |
| `DATE_BUILT` | mnf:Varchar | bvtk:USDateString | yes |
| `DATE_OCCUPIED` | mnf:Varchar | bvtk:USDateString | yes |
| `FAC_BUILDING_KEY` | mnf:Varchar | dw:BuildingNumber | no |
| `OWNERSHIP_TYPE` | mnf:Varchar | dw:OwnershipType | yes |
| `PARENT_BUILDING_NUMBER` | mnf:Varchar | dw:BuildingNumber | yes |
| `SITE` | mnf:Varchar | dw:Site | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar | bvtk:OracleShortDateString | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| severe | [BVT-K-GAP-10] Many dw date columns are stored as VARCHAR with one of two formats: * MM/DD/YYYY ('07/01/1913') — DATE_BUILT, DATE_OCCUPIED, DATE_ACQUIRED * DD-MON-YY ('19-DEC-24') — WAREHOUSE_LOAD_DATE Filtering on a date range needs string parsing. Naive comparisons (DATE_BUILT < '1950-01-01') return wrong results because the column isn't a real date. |

---

## dw.fclt_building — buildings with rich attributes (FCLT_-keyed)

**URI:** `dw:fclt_building`
  
Same 32 columns and same data as fac_building; differs only in PK column name (FCLT_BUILDING_KEY vs FAC_BUILDING_KEY). A SQL author can use either family; see dw:fac_fclt_duality. The 32 columns mirror fac_building. Only key columns are explicitly declared below; the other 28 are denoted by dw:fclt_building_columns_match_fac.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_building`
  
**Entity key:** `FCLT_BUILDING_KEY`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `BUILDING_NUMBER` | mnf:Varchar | dw:BuildingNumber | no |
| `FCLT_BUILDING_KEY` | mnf:Varchar | dw:BuildingNumber | no |

---

## dw.fclt_building_address — addresses by purpose (FCLT-keyed)

**URI:** `dw:fclt_building_address`
  
[BVT-K-GAP-1] Snapshot row count: 785. One row per (building, ADDRESS_PURPOSE). Composite key FCLT_BUILDING_ADDRESS_KEY = '<BUILDING>-<ADDRESS_PURPOSE>' (see dw:derive_fclt_address_key). [BVT-K-GAP-15]
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_building_address`
  
**Entity key:** `FCLT_BUILDING_ADDRESS_KEY`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ADDRESS_PURPOSE` | mnf:Varchar | dw:AddressPurpose | no |
| `CITY` | mnf:Varchar |  | yes |
| `FCLT_BUILDING_ADDRESS_KEY` | mnf:Varchar |  | no |
| `FCLT_BUILDING_KEY` | mnf:Varchar | dw:BuildingNumber | no |
| `IS_E911_ADDRESS` | mnf:Varchar |  | yes |
| `POSTAL_CODE` | mnf:Varchar | dw:USPostalCodeStripped | yes |
| `POST_DIRECTIONAL` | mnf:Varchar |  | yes |
| `PRE_DIRECTIONAL` | mnf:Varchar |  | yes |
| `STATE` | mnf:Varchar |  | yes |
| `STREET_NAME` | mnf:Varchar |  | yes |
| `STREET_NUMBER` | mnf:Varchar |  | yes |
| `STREET_SUFFIX` | mnf:Varchar |  | yes |

### Derivations

| Derived Column | Source Columns | Function | Properties |
|----------------|----------------|----------|------------|
| `FCLT_BUILDING_ADDRESS_KEY` | `FCLT_BUILDING_KEY`, `ADDRESS_PURPOSE` | bvtk:DashConcat | mnf:Deterministic, mnf:Invertible |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | [BVT-K-GAP-10] POSTAL_CODE in fac_/fclt_building_address has leading zeros stripped: Cambridge MA 02139 stored as '2139'. Joining to zip_usa.ZIP_CODE (which probably stores '02139') would need zero-padding back via LPAD or string concatenation. |

---

## dw.fac_building_address — addresses by purpose (FAC-keyed)

**URI:** `dw:fac_building_address`
  
Parallel with fclt_building_address — same data, FAC-style key column names. The full table has 15 columns; only the heavily-trafficked key columns are explicitly declared here.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fac_building_address`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ADDRESS_PURPOSE` | mnf:Varchar | dw:AddressPurpose | no |
| `BUILDING_KEY` | mnf:Varchar | dw:BuildingNumber | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | [BVT-K-GAP-10] POSTAL_CODE in fac_/fclt_building_address has leading zeros stripped: Cambridge MA 02139 stored as '2139'. Joining to zip_usa.ZIP_CODE (which probably stores '02139') would need zero-padding back via LPAD or string concatenation. |

---

## dw.fac_rooms — room inventory (granular, includes service spaces)

**URI:** `dw:fac_rooms`
  
[BVT-K-GAP-1 / BVT-K-GAP-14] Snapshot row count: 43,175. Includes service / circulation / mechanical spaces. ~2× the size of fclt_rooms because it has more granular space breakdown and collapses the Stata Center's letter-prefixed floors ('D4' → '1'). For "rooms a department occupies" prefer fclt_rooms; for "all rooms including circulation" prefer fac_rooms.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fac_rooms`
  
**Entity key:** `FAC_ROOM_KEY`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `AREA` | mnf:Double |  | yes |
| `BUILDING_KEY` | mnf:Varchar | dw:BuildingNumber | no |
| `FAC_ROOM_KEY` | mnf:Varchar |  | no |
| `FLOOR` | mnf:Varchar |  | yes |
| `FLOOR_KEY` | mnf:Varchar |  | yes |
| `MAJOR_USE_DESC` | mnf:Varchar | dw:MajorUseDesc | yes |
| `ORGANIZATION_NAME` | mnf:Varchar |  | yes |
| `ROOM` | mnf:Varchar |  | no |
| `SPACE_ID` | mnf:Varchar |  | yes |

### Derivations

| Derived Column | Source Columns | Function | Properties |
|----------------|----------------|----------|------------|
| `FAC_ROOM_KEY` | `BUILDING_KEY`, `ROOM` | bvtk:DashConcat | mnf:Deterministic, mnf:Invertible |

---

## dw.fclt_rooms — curated room inventory (FCLT-keyed)

**URI:** `dw:fclt_rooms`
  
[BVT-K-GAP-1 / BVT-K-GAP-14] Snapshot row count: 20,000. Curated subset of rooms with department attribution. Adds BUILDING_ROOM denormalised column. Preserves Stata's letter- prefixed floors that fac_rooms collapses. ORGANIZATION_NAME is the actual department (e.g. 'CSAIL', 'LI&DS').
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_rooms`
  
**Entity key:** `FCLT_ROOM_KEY`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `AREA` | mnf:Double |  | yes |
| `BUILDING_ROOM` | mnf:Varchar |  | yes |
| `FCLT_BUILDING_KEY` | mnf:Varchar | dw:BuildingNumber | no |
| `FCLT_FLOOR_KEY` | mnf:Varchar |  | yes |
| `FCLT_ROOM_KEY` | mnf:Varchar |  | no |
| `FLOOR` | mnf:Varchar |  | yes |
| `MAJOR_USE_DESC` | mnf:Varchar | dw:MajorUseDesc | yes |
| `ORGANIZATION_NAME` | mnf:Varchar |  | yes |
| `ROOM` | mnf:Varchar |  | no |
| `SPACE_ID` | mnf:Varchar |  | yes |

### Derivations

| Derived Column | Source Columns | Function | Properties |
|----------------|----------------|----------|------------|
| `FCLT_ROOM_KEY` | `FCLT_BUILDING_KEY`, `ROOM` | bvtk:DashConcat | mnf:Deterministic, mnf:Invertible |

---

## dw.space_detail — leaner space inventory (third representation)

**URI:** `dw:space_detail`
  
[BVT-K-GAP-1 / BVT-K-GAP-14] Snapshot row count: 43,175 (same as fac_rooms). Different schema: 11 columns, lookup-keyed via SPACE_UNIT_KEY and SPACE_USAGE_KEY. Probably the older / simpler representation that fac_/fclt_ enrich.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/space_detail`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `BUILDING_KEY` | mnf:Varchar | dw:BuildingNumber | no |
| `BUILDING_ROOM` | mnf:Varchar |  | no |
| `FLOOR_KEY` | mnf:Varchar |  | yes |
| `ROOM_NUMBER` | mnf:Varchar |  | yes |
| `ROOM_SQUARE_FOOTAGE` | mnf:Double |  | yes |
| `SPACE_UNIT_KEY` | mnf:Varchar |  | yes |
| `SPACE_USAGE_KEY` | mnf:Varchar |  | yes |

---

## dw.fac_floor — floor records (FAC-keyed)

**URI:** `dw:fac_floor`
  
[BVT-K-GAP-1 / BVT-K-GAP-11] Row count: 1,079. Parallel with fclt_floor; differ only in key column names.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fac_floor`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `BUILDING_KEY` | mnf:Varchar | dw:BuildingNumber | no |
| `FLOOR` | mnf:Varchar |  | yes |
| `FLOOR_KEY` | mnf:Varchar |  | yes |

---

## dw.fclt_floor — floor records (FCLT-keyed)

**URI:** `dw:fclt_floor`
  
[BVT-K-GAP-1 / BVT-K-GAP-11] Row count: 1,079. Parallel with fac_floor.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_floor`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `FCLT_BUILDING_KEY` | mnf:Varchar | dw:BuildingNumber | no |
| `FCLT_FLOOR_KEY` | mnf:Varchar |  | no |
| `FLOOR` | mnf:Varchar |  | yes |

---

## dw.space_floor — floor-name dictionary

**URI:** `dw:space_floor`
  
[BVT-K-GAP-1] Row count: 49. Just a dictionary — for each FLOOR string in use ('0', '00', '000', '1', '2', ...) provides FLOOR_NAME = '<FLOOR> Floor'.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/space_floor`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `FLOOR` | mnf:Varchar |  | no |
| `FLOOR_NAME` | mnf:Varchar |  | yes |

---

## dw.fclt_major_use — MAJOR_USE_DESC code legend

**URI:** `dw:fclt_major_use`
  
[BVT-K-GAP-1] Row count: 14. Lookup table for the dw:MajorUseDesc allowed values.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_major_use`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DESCRIPTION` | mnf:Varchar |  | yes |
| `MAJOR_USE` | mnf:Varchar |  | no |

---

## dw.space_usage — granular room-purpose taxonomy

**URI:** `dw:space_usage`
  
[BVT-K-GAP-1] Row count: ~88+. Independent room-purpose taxonomy linked from space_detail. Some duplicates (e.g. 'RSRC RM' appears twice with different keys).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/space_usage`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `SPACE_USAGE` | mnf:Varchar |  | no |
| `SPACE_USAGE_KEY` | mnf:Integer |  | no |

---

## dw.space_unit — DLC mapping (proper-case names)

**URI:** `dw:space_unit`
  
[BVT-K-GAP-1 / BVT-K-GAP-11] Row count: ~150. Maps SPACE_UNIT_KEY → DLC_KEY with proper-case unit names. Has FCLT_ORGANIZATION_KEY (which space_unit2 lacks). Prefer this over space_unit2 when joining back to fclt_organization.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/space_unit`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DLC_KEY` | mnf:Varchar |  | yes |
| `FCLT_ORGANIZATION_KEY` | mnf:Varchar |  | yes |
| `SPACE_UNIT` | mnf:Varchar |  | yes |
| `SPACE_UNIT_KEY` | mnf:Varchar |  | no |

---

## dw.space_unit2 — DLC mapping (uppercase abbreviated)

**URI:** `dw:space_unit2`
  
[BVT-K-GAP-1 / BVT-K-GAP-11] Row count: ~150. Same SPACE_UNIT_KEY → DLC_KEY mapping as space_unit but UPPERCASE abbreviated SPACE_UNIT names. Two stylistic representations of the same logical entity. Lacks FCLT_ORGANIZATION_KEY.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/space_unit2`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DLC_KEY` | mnf:Varchar |  | yes |
| `SPACE_UNIT` | mnf:Varchar |  | yes |
| `SPACE_UNIT_KEY` | mnf:Varchar |  | no |

---

## dw.space_supervisor_usage — pre-aggregated per-supervisor metrics

**URI:** `dw:space_supervisor_usage`
  
[BVT-K-GAP-1] Row count: 2,135. Pre-aggregated metrics keyed by MIT_ID. Misleadingly-named — sole place where per-supervisor space totals + supervisee counts live.
  
**Row semantics:** mnf:AggregateRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/space_supervisor_usage`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DEPT_COUNT` | mnf:Integer |  | yes |
| `MIT_ID` | mnf:Varchar |  | no |
| `NUM_OF_SUPERVISEES` | mnf:Integer |  | yes |
| `RESEARCH_VOLUME` | mnf:Double |  | yes |
| `SQFT` | mnf:Double |  | yes |

---

## dw.master_dept_hierarchy — DLC org tree (5-level path)

**URI:** `dw:master_dept_hierarchy`
  
The canonical org tree, one row per DLC. Stores a flattened self-contained path through 5 hierarchy levels. Level 5 is NEVER populated in this dump. DLC_NAME is mixed-case; case-insensitive comparisons need LOWER()/UPPER().
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/master_dept_hierarchy`
  
**Entity key:** `DLC_KEY`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DLC_CODE` | mnf:Varchar | dw:DLCKey | no |
| `DLC_KEY` | mnf:Varchar | dw:DLCKey | no |
| `DLC_NAME` | mnf:Varchar |  | no |
| `HIERARCHY_TYPE` | mnf:Varchar |  | no |
| `MASTER_DEPT_HIER_LEVEL_1_CODE` | mnf:Varchar |  | yes |
| `MASTER_DEPT_HIER_LEVEL_1_NAME` | mnf:Varchar |  | yes |
| `MASTER_DEPT_HIER_LEVEL_2_CODE` | mnf:Varchar |  | yes |
| `MASTER_DEPT_HIER_LEVEL_2_NAME` | mnf:Varchar |  | yes |
| `MASTER_DEPT_HIER_LEVEL_3_CODE` | mnf:Varchar |  | yes |
| `MASTER_DEPT_HIER_LEVEL_3_NAME` | mnf:Varchar |  | yes |
| `MASTER_DEPT_HIER_LEVEL_4_CODE` | mnf:Varchar |  | yes |
| `MASTER_DEPT_HIER_LEVEL_4_NAME` | mnf:Varchar |  | yes |
| `MASTER_DEPT_HIER_LEVEL_5_CODE` | mnf:Varchar |  | yes |
| `MASTER_DEPT_HIER_LEVEL_5_NAME` | mnf:Varchar |  | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| minor | [BVT-K-GAP-2] master_dept_hierarchy.MASTER_DEPT_HIER_LEVEL_5_CODE/_NAME columns exist but are NULL for every row in this dump. |

---

## dw.master_dept_hierarchy_links — DLC↔external-system cross-refs

**URI:** `dw:master_dept_hierarchy_links`
  
[BVT-K-GAP-1] Snapshot row count: 42,089. Cross- references DLCs to identifiers in other systems via LINK_TYPE_CODE (FC=Funds Center 34555 rows, PMIT=Profit Center 4366, ORG2=New Org Unit 1096, ORGU=Old Org Unit 922, BAG=NIMBUS BAG 528, FORG=Facilities Org 330).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/master_dept_hierarchy_links`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DLC_KEY` | mnf:Varchar | dw:DLCKey | no |
| `LINKED_OBJECT_CODE` | mnf:Varchar |  | yes |
| `LINKED_OBJECT_KEY` | mnf:Varchar |  | yes |
| `LINK_TYPE` | mnf:Varchar |  | yes |
| `LINK_TYPE_CODE` | mnf:Varchar |  | no |

---

## dw.master_dept_dcode_parent — adjacency-list parent pointers

**URI:** `dw:master_dept_dcode_parent`
  
[BVT-K-GAP-1] Snapshot row count: 340. Same hierarchy as master_dept_hierarchy but expressed as numeric parent pointers — useful for recursive walks. 30-row gap vs master_dept_hierarchy (310) is hierarchy-level pseudo-departments (D_ALL, D_PROVOST_AREA) that don't have own hierarchy rows.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/master_dept_dcode_parent`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DEPT_ID` | mnf:Integer |  | no |
| `D_CODE` | mnf:Varchar | dw:DLCKey | no |
| `D_NAME` | mnf:Varchar |  | yes |
| `PARENT_D_CODE` | mnf:Varchar | dw:DLCKey | yes |
| `PARENT_D_NAME` | mnf:Varchar |  | yes |
| `PARENT_ID` | mnf:Integer |  | yes |

---

## dw.sis_department — academic-side department catalogue

**URI:** `dw:sis_department`
  
[BVT-K-GAP-1] Snapshot row count: 128. Student Information System view of departments. DEPARTMENT_CODE values mix numbers (MIT course codes like '13' = Ocean Engineering) and abbreviations (IDS, ESD, LFM). Joins to master_dept_hierarchy on DLC_KEY.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/sis_department`
  
**Entity key:** `DEPARTMENT_CODE`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DEPARTMENT_CODE` | mnf:Varchar |  | no |
| `DEPARTMENT_FULL_NAME` | mnf:Varchar |  | yes |
| `DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `DLC_KEY` | mnf:Varchar | dw:DLCKey | yes |
| `IS_DEGREE_GRANTING` | mnf:Varchar | dw:YNFlag | yes |
| `SCHOOL_CODE` | mnf:Varchar | dw:SchoolCode | yes |
| `SCHOOL_NAME` | mnf:Varchar |  | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | [BVT-K-GAP-8] sis_department.SCHOOL_NAME and master_dept_hierarchy.MASTER_DEPT_HIER_LEVEL_3_NAME spell the same school differently: sis_department: 'Hum, Arts & Social Sciences' master_dept_hierarchy: 'School of Humanities & Social Science' (singular!) Equality filters that use one spelling won't match rows in the other. |

---

## dw.sis_admin_department — admin-office catalogue

**URI:** `dw:sis_admin_department`
  
[BVT-K-GAP-1] Snapshot row count: 179. Distinct from sis_department; covers admin offices (ADM Admissions, BUR Bursar, CP Campus Police, DIN Dining, GSO Office of Graduate Education). Phone numbers are 7-digit no-area-code strings; AREA_CODE is consistently NULL.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/sis_admin_department`
  
**Entity key:** `SIS_ADMIN_DEPARTMENT_CODE`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CLEARING_COST_COLLECTOR` | mnf:Varchar |  | yes |
| `DEPARTMENT_PHONE_AREA_CODE` | mnf:Varchar |  | yes |
| `DEPARTMENT_PHONE_NUMBER` | mnf:Varchar |  | yes |
| `LAST_ACTIVITY_DATE` | mnf:Varchar | dw:OracleDateString | yes |
| `SIS_ADMIN_DEPARTMENT_CODE` | mnf:Varchar |  | no |
| `SIS_ADMIN_DEPARTMENT_NAME` | mnf:Varchar |  | yes |

---

## dw.fclt_organization — facilities org table (DLC-aware)

**URI:** `dw:fclt_organization`
  
[BVT-K-GAP-1] Snapshot row count: 180. Has DLC_KEY, DLC_NAME, plus FCLT_ORGANIZATION_KEY integer. Self-references via FCLT_ORG_PARENT_KEY for facilities tree.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_organization`
  
**Entity key:** `FCLT_ORGANIZATION_KEY`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DLC_KEY` | mnf:Varchar | dw:DLCKey | yes |
| `DLC_NAME` | mnf:Varchar |  | yes |
| `FCLT_ORGANIZATION_KEY` | mnf:Integer |  | no |
| `FCLT_ORG_PARENT_KEY` | mnf:Integer |  | yes |
| `ORGANIZATION_LEVEL` | mnf:Integer |  | yes |

---

## dw.fac_organization — facilities org table (D_CODE-style)

**URI:** `dw:fac_organization`
  
[BVT-K-GAP-1 / BVT-K-GAP-11] Snapshot row count: 169. Mirror of fclt_organization but uses D_CODE instead of DLC_KEY/DLC_NAME pair (older field-naming convention).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fac_organization`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `D_CODE` | mnf:Varchar | dw:DLCKey | yes |
| `FAC_ORGANIZATION_KEY` | mnf:Integer |  | no |

---

## dw.fclt_org_dlc_key — explicit FCLT_ORGANIZATION_KEY ↔ DLC_KEY bridge

**URI:** `dw:fclt_org_dlc_key`
  
The canonical bridge for navigating from rooms (which carry FCLT_ORGANIZATION_KEY) to departmental DLC codes.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_org_dlc_key`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DLC_KEY` | mnf:Varchar | dw:DLCKey | no |
| `FCLT_ORGANIZATION_KEY` | mnf:Integer |  | no |

---

## dw.hr_org_unit — HR org units (older system)

**URI:** `dw:hr_org_unit`
  
[BVT-K-GAP-1 / BVT-K-GAP-23] Snapshot row count: 641. 641 distinct ids; subset of hr_org_unit_new (691 ids — 50 added). HR hierarchy is SEPARATE from DLC hierarchy.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/hr_org_unit`
  
**Entity key:** `HR_ORG_UNIT_ID`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DLC_KEY` | mnf:Varchar | dw:DLCKey | yes |
| `HR_DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `HR_DEPARTMENT_NAME_ALPHA` | mnf:Varchar |  | yes |
| `HR_DEPARTMENT_NAME_LONG` | mnf:Varchar |  | yes |
| `HR_ORG_UNIT_ID` | mnf:Varchar |  | no |

---

## dw.hr_org_unit_new — HR org units (current; superset)

**URI:** `dw:hr_org_unit_new`
  
[BVT-K-GAP-1 / BVT-K-GAP-23] Snapshot row count: 691. Strict superset of hr_org_unit. Drops HR_DEPARTMENT_ID and levels 6/7; adds HR_DEPARTMENT_ABBR.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/hr_org_unit_new`
  
**Entity key:** `HR_ORG_UNIT_ID`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DLC_KEY` | mnf:Varchar | dw:DLCKey | yes |
| `HR_DEPARTMENT_ABBR` | mnf:Varchar |  | yes |
| `HR_DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `HR_ORG_UNIT_ID` | mnf:Varchar |  | no |

---

## dw.subject_offered — subject sections per term

**URI:** `dw:subject_offered`
  
[BVT-K-GAP-1] Snapshot row count: 649,440. One row per (term, subject, section). 47 columns total; the most information-rich subjects table. RESPONSIBLE_FACULTY_MIT_ID is in MIT_ID Namespace A.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/subject_offered`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CLUSTER_LIST` | mnf:Varchar | dw:CommaListString | yes |
| `CLUSTER_TYPE` | mnf:Varchar |  | yes |
| `COMPOSITE_SUBJECT_KEY` | mnf:Varchar |  | yes |
| `HGN_CODE` | mnf:Varchar | dw:HGNCode | yes |
| `HGN_CODE_DESC` | mnf:Varchar |  | yes |
| `IS_LECTURE_SECTION` | mnf:Varchar | dw:YNFlag | yes |
| `IS_MASTER_SECTION` | mnf:Varchar | dw:YNFlag | yes |
| `MASTER_SUBJECT_ID` | mnf:Varchar | dw:SubjectId | yes |
| `MEET_PLACE` | mnf:Varchar |  | yes |
| `MEET_TIME` | mnf:Varchar |  | yes |
| `NUM_ENROLLED_STUDENTS` | mnf:Integer |  | yes |
| `OFFER_DEPT_CODE` | mnf:Varchar |  | yes |
| `OFFER_DEPT_NAME` | mnf:Varchar |  | yes |
| `OFFER_SCHOOL_NAME` | mnf:Varchar |  | yes |
| `RESPONSIBLE_FACULTY_MIT_ID` | mnf:Varchar | dw:MITID_NamespaceA | yes |
| `RESPONSIBLE_FACULTY_NAME` | mnf:Varchar |  | yes |
| `SECTION_ENROLLMENT_NUMBER` | mnf:Varchar |  | yes |
| `SECTION_ID` | mnf:Varchar |  | yes |
| `SUBJECT_ENROLLMENT_NUMBER` | mnf:Integer |  | yes |
| `SUBJECT_GROUPING_KEY` | mnf:Varchar |  | yes |
| `SUBJECT_ID` | mnf:Varchar | dw:SubjectId | no |
| `SUBJECT_OFFERED_SUMMARY_KEY` | mnf:Varchar |  | yes |
| `SUBJECT_TITLE` | mnf:Varchar |  | yes |
| `TERM_CODE` | mnf:Varchar | dw:TermCode | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| minor | subject_offered.CLUSTER_TYPE has 268 rows with a single-space ' ' value — a data-quality blip distinct from NULL or any documented code. |

---

## dw.subject_offered_summary — per-(subject, term) summary

**URI:** `dw:subject_offered_summary`
  
[BVT-K-GAP-1 / BVT-K-GAP-26] Snapshot row count: 470,264. Per-(subject, term) summary; collapses sections from subject_offered. PK is concatenated SUBJECT_ID+TERM_CODE. Carries RESPONSIBLE_FACULTY_NAME and RESPONSIBLE_FACULTY_MIT_ID (Namespace A) at the per-subject grain.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/subject_offered_summary`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `RESPONSIBLE_FACULTY_MIT_ID` | mnf:Varchar | dw:MITID_NamespaceA | yes |
| `RESPONSIBLE_FACULTY_NAME` | mnf:Varchar |  | yes |
| `SUBJECT_ENROLLMENT_NUMBER` | mnf:Integer |  | yes |
| `SUBJECT_ID` | mnf:Varchar | dw:SubjectId | no |
| `SUBJECT_OFFERED_SUMMARY_KEY` | mnf:Varchar |  | no |
| `SUBJECT_TITLE` | mnf:Varchar |  | yes |
| `TERM_CODE` | mnf:Varchar | dw:TermCode | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | [BVT-K-GAP-26] Three nearly-identical per-(subject, term) summary tables exist: subject_offered (649K rows, 47 cols, base — per-section) subject_offered_summary (470K rows, 29 cols, per-subject; carries faculty) subject_summary (469K rows, 41 cols, per-subject; carries SUBJECT_OR_CLUSTER) Each table has a different grain (per-section vs per-subject) and a different column set. Picking the right one depends on the question — the manifest can't yet express table-selection rules (see GAP-26 in vocabulary-evolution.md). |

---

## dw.course_catalog_subject_offered — recent year-scoped catalogue

**URI:** `dw:course_catalog_subject_offered`
  
[BVT-K-GAP-1 / BVT-K-GAP-26] Snapshot row count: 20,000. Per-(academic_year, subject) row. 69 columns covering term-offering flags, units, attributes, prerequisites.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/course_catalog_subject_offered`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ACADEMIC_YEAR` | mnf:Varchar |  | yes |
| `DEPARTMENT_CODE` | mnf:Varchar |  | yes |
| `DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `FALL_INSTRUCTORS` | mnf:Varchar | dw:CommaListString | yes |
| `GIR_ATTRIBUTE` | mnf:Varchar | dw:GIRAttribute | yes |
| `HASS_ATTRIBUTE` | mnf:Varchar | dw:HASSAttribute | yes |
| `HGN_CODE` | mnf:Varchar | dw:HGNCode | yes |
| `IS_OFFERED_FALL_TERM` | mnf:Varchar | dw:YNFlag | yes |
| `IS_OFFERED_IAP` | mnf:Varchar | dw:YNFlag | yes |
| `IS_OFFERED_SPRING_TERM` | mnf:Varchar | dw:YNFlag | yes |
| `IS_OFFERED_SUMMER_TERM` | mnf:Varchar | dw:YNFlag | yes |
| `IS_OFFERED_THIS_YEAR` | mnf:Varchar | dw:YNFlag | yes |
| `LAB_UNITS` | mnf:Varchar |  | yes |
| `LECTURE_UNITS` | mnf:Varchar |  | yes |
| `RESPONSIBLE_FACULTY_MIT_ID` | mnf:Varchar | dw:MITID_NamespaceA | yes |
| `RESPONSIBLE_FACULTY_NAME` | mnf:Varchar |  | yes |
| `SPRING_INSTRUCTORS` | mnf:Varchar | dw:CommaListString | yes |
| `SUBJECT_CODE` | mnf:Varchar |  | yes |
| `SUBJECT_DESCRIPTION` | mnf:Varchar |  | yes |
| `SUBJECT_ID` | mnf:Varchar | dw:SubjectId | no |
| `SUBJECT_NUMBER` | mnf:Varchar |  | yes |
| `SUBJECT_TITLE` | mnf:Varchar |  | yes |
| `TOTAL_UNITS` | mnf:Varchar |  | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Three course-catalog tables exist with overlapping but different content: course_catalog_subject_offered (20K rows, recent year-scoped) cis_course_catalog (115K rows, longer history) drupal_course_catalog (122K rows, Drupal-published mirror) Core column names match across all three; swapping the FROM is a one-table change. |

---

## dw.cis_course_catalog — older CIS course catalogue

**URI:** `dw:cis_course_catalog`
  
[BVT-K-GAP-1 / BVT-K-GAP-26] Snapshot row count: 115,226. Older / broader Course Information System feed. 58 columns.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/cis_course_catalog`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ACADEMIC_YEAR` | mnf:Varchar |  | yes |
| `GIR_ATTRIBUTE` | mnf:Varchar | dw:GIRAttribute | yes |
| `HASS_ATTRIBUTE` | mnf:Varchar | dw:HASSAttribute | yes |
| `HGN_CODE` | mnf:Varchar | dw:HGNCode | yes |
| `SUBJECT_ID` | mnf:Varchar | dw:SubjectId | yes |
| `SUBJECT_TITLE` | mnf:Varchar |  | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | Three course-catalog tables exist with overlapping but different content: course_catalog_subject_offered (20K rows, recent year-scoped) cis_course_catalog (115K rows, longer history) drupal_course_catalog (122K rows, Drupal-published mirror) Core column names match across all three; swapping the FROM is a one-table change. |

---

## dw.cis_hass_attribute — HASS attribute taxonomy lookup

**URI:** `dw:cis_hass_attribute`
  
[BVT-K-GAP-1] Snapshot row count: 17. Authoritative lookup for HASS-D / GIR codes. CIS_ATTRIBUTE_GROUP='H' for post-2010 students, 'G' for pre-2010.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/cis_hass_attribute`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CIS_ATTRIBUTE_GROUP` | mnf:Varchar |  | yes |
| `DESCRIPTION_IN_BULLETIN` | mnf:Varchar |  | yes |
| `DESCRIPTION_ON_FORM` | mnf:Varchar |  | yes |
| `HASS_ATTRIBUTE` | mnf:Varchar | dw:HASSAttribute | no |

---

## dw.sis_course_description — canonical course descriptor (with TYPO COLUMN)

**URI:** `dw:sis_course_description`
  
[BVT-K-GAP-1 / BVT-K-GAP-28] Snapshot row count: 695. Per-(COURSE, COURSE_LEVEL). Notable: BOTH GRADAUTE_LEVEL (typo) and GRADUATE_LEVEL columns exist with identical values. Sentinel terms '000000' / '999999' for FROM_TERM / THRU_TERM.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/sis_course_description`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CIP_PROGRAM_CODE` | mnf:Varchar | dw:CIPCode | yes |
| `COURSE` | mnf:Varchar |  | no |
| `COURSE_DESCRIPTION` | mnf:Varchar |  | yes |
| `COURSE_DESCRIPTION_LONG` | mnf:Varchar |  | yes |
| `COURSE_LEVEL` | mnf:Varchar | dw:CourseLevel | yes |
| `COURSE_OPTION` | mnf:Varchar |  | yes |
| `DEFAULT_ULTIMATE_DEGREE` | mnf:Varchar |  | yes |
| `DEPARTMENT` | mnf:Varchar |  | yes |
| `DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `FROM_TERM` | mnf:Varchar | dw:SentinelTermCode | yes |
| `FROM_TERM_DESCRIPTION` | mnf:Varchar |  | yes |
| `GRADAUTE_LEVEL` | mnf:Varchar |  | yes |
| `GRADUATE_LEVEL` | mnf:Varchar |  | yes |
| `IS_DEGREE_GRANTING` | mnf:Varchar | dw:YNFlag | yes |
| `SCHOOL_NAME` | mnf:Varchar |  | yes |
| `SIS_COURSE_DESCRIPTION_KEY` | mnf:Varchar |  | no |
| `THRU_TERM` | mnf:Varchar | dw:SentinelTermCode | yes |
| `THRU_TERM_DESCRIPTION` | mnf:Varchar |  | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| minor | [BVT-K-GAP-28] sis_course_description has BOTH GRADAUTE_LEVEL (typo) and GRADUATE_LEVEL columns. Both contain identical values. Probably preserved for backwards- compatibility with old code. |

---

## dw.sis_subject_code — subject-code prefix → dept+school

**URI:** `dw:sis_subject_code`
  
[BVT-K-GAP-1] Snapshot row count: 221. Bridges subject-code prefixes ('21A', 'WCM', 'WGS') to departments.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/sis_subject_code`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DEPARTMENT_CODE` | mnf:Varchar |  | yes |
| `DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `SCHOOL_CODE` | mnf:Varchar | dw:SchoolCode | yes |
| `SCHOOL_NAME` | mnf:Varchar |  | yes |
| `SUBJECT_CODE` | mnf:Varchar |  | no |
| `SUBJECT_CODE_DESC` | mnf:Varchar |  | yes |

---

## dw.iap_subject_detail — IAP activity registry (2021JA snapshot only)

**URI:** `dw:iap_subject_detail`
  
[BVT-K-GAP-1 / BVT-K-GAP-24] Snapshot row count: 465. Central IAP table. ALL 465 rows have TERM_CODE='2021JA' — the whole table is a single-term snapshot. 105 distinct ACTIVITY_TITLE values; ~4.4 detail rows per activity (one per (activity, category) pair). Use SELECT DISTINCT ACTIVITY_TITLE.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/iap_subject_detail`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ACTIVITY_DESCRIPTION` | mnf:Varchar |  | yes |
| `ACTIVITY_TITLE` | mnf:Varchar |  | yes |
| `ATTENDANCE` | mnf:Varchar |  | yes |
| `CREATE_DATE` | mnf:Varchar | dw:OracleDateString | yes |
| `ENROLLMENT_TYPE` | mnf:Varchar |  | yes |
| `FEE` | mnf:Varchar |  | yes |
| `IAP_SUBJECT_CATEGORY_KEY` | mnf:Varchar |  | yes |
| `IAP_SUBJECT_PERSON_KEY` | mnf:Varchar |  | yes |
| `IAP_SUBJECT_SESSION_KEY` | mnf:Varchar |  | yes |
| `IAP_SUBJECT_SPONSOR_KEY` | mnf:Varchar |  | yes |
| `IS_CANCELLED` | mnf:Varchar | dw:YNFlag | yes |
| `IS_MULTIPLE_SESSION` | mnf:Varchar | dw:YNFlag | yes |
| `LAST_ACTIVITY_DATE` | mnf:Varchar | dw:OracleDateString | yes |
| `MAX_ENROLLMENT` | mnf:Integer |  | yes |
| `PREREQUISITES` | mnf:Varchar |  | yes |
| `TERM_CODE` | mnf:Varchar | dw:TermCode | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | [BVT-K-GAP-24] iap_subject_detail (and the rest of the IAP cluster) is a SINGLE-TERM SNAPSHOT — every row has TERM_CODE='2021JA'. Schema looks multi-term but data only covers IAP 2021. |

---

## dw.iap_subject_person — IAP person/role records

**URI:** `dw:iap_subject_person`
  
PERSON_NAME format is 'FirstName LastName' — the OUTLIER convention versus the 'LastName, FirstName' used by every other people-bearing table in dw. PERSON_ROLE distinguishes activity leaders, sponsors, and other associated roles.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/iap_subject_person`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `IAP_SUBJECT_PERSON_KEY` | mnf:Varchar |  | no |
| `PERSON_MIT_AFFILIATION` | mnf:Varchar |  | yes |
| `PERSON_NAME` | mnf:Varchar |  | yes |
| `PERSON_ROLE` | mnf:Varchar |  | yes |

---

## dw.iap_subject_session — IAP session schedule

**URI:** `dw:iap_subject_session`
  
[BVT-K-GAP-1] Snapshot row count: 1,199. SESSION_DATE in Oracle DD-MON-YY. SESSION_START_TIME / END_TIME in '0100PM'/'1100AM' format (NO COLON, no space before AM/PM).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/iap_subject_session`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `HAS_SESSION_INFO` | mnf:Varchar | dw:YNFlag | yes |
| `IAP_SUBJECT_SESSION_KEY` | mnf:Varchar |  | no |
| `SESSION_DATE` | mnf:Varchar | dw:OracleDateString | yes |
| `SESSION_END_TIME` | mnf:Varchar |  | yes |
| `SESSION_LOCATION` | mnf:Varchar |  | yes |
| `SESSION_START_TIME` | mnf:Varchar |  | yes |

---

## dw.iap_subject_sponsor — IAP activity sponsor catalogue

**URI:** `dw:iap_subject_sponsor`
  
[BVT-K-GAP-1] Snapshot row count: 68. Sponsor names retained (NOT anonymised).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/iap_subject_sponsor`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `IAP_SUBJECT_SPONSOR_KEY` | mnf:Varchar |  | no |
| `SPONSOR_NAME` | mnf:Varchar |  | yes |
| `SPONSOR_TYPE` | mnf:Varchar |  | yes |

---

## dw.iap_subject_category — IAP category labels

**URI:** `dw:iap_subject_category`
  
[BVT-K-GAP-1] Snapshot row count: 49. Real category labels (Climate, Global Opportunities, etc.).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/iap_subject_category`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `IAP_CATEGORY_DESC` | mnf:Varchar |  | yes |
| `IAP_CATEGORY_NAME` | mnf:Varchar |  | yes |
| `IAP_SUBJECT_CATEGORY_KEY` | mnf:Varchar |  | no |

---

## dw.library_subject_offered — library's per-(subject, term) view (2009-2021)

**URI:** `dw:library_subject_offered`
  
[BVT-K-GAP-1] Snapshot row count: 17,065. PK is concatenated SUBJECT_ID+TERM_CODE (no separator). RESPONSIBLE_FACULTY_MIT_ID is Namespace A.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/library_subject_offered`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `LIBRARY_SUBJECT_OFFERED_KEY` | mnf:Varchar |  | no |
| `MASTER_COURSE_NUMBER` | mnf:Varchar |  | yes |
| `RESPONSIBLE_FACULTY_MIT_ID` | mnf:Varchar | dw:MITID_NamespaceA | yes |
| `RESPONSIBLE_FACULTY_NAME` | mnf:Varchar |  | yes |
| `SUBJECT_ID` | mnf:Varchar | dw:SubjectId | yes |
| `SUBJECT_TITLE` | mnf:Varchar |  | yes |
| `TERM_CODE` | mnf:Varchar | dw:TermCode | yes |

---

## dw.library_course_instructor — instructor↔course assignments

**URI:** `dw:library_course_instructor`
  
[BVT-K-GAP-1] Snapshot row count: 18,691. Composite PK is self-describing string with course/instructor/term encoded. UNIT_CODE/UNIT identify physical libraries (Hayden, Barker, Dewey).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/library_course_instructor`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DATE_FROM` | mnf:Varchar | dw:OracleDateString | yes |
| `DATE_TO` | mnf:Varchar | dw:OracleDateString | yes |
| `DEPARTMENT` | mnf:Varchar |  | yes |
| `INSTRUCTOR_NAME` | mnf:Varchar |  | yes |
| `LIBRARY_COURSE_INSTRUCTOR_KEY` | mnf:Varchar |  | no |
| `SUBJECT_ID` | mnf:Varchar | dw:SubjectId | yes |
| `UNIT` | mnf:Varchar |  | yes |
| `UNIT_CODE` | mnf:Varchar |  | yes |

---

## dw.library_reserve_catalog — library catalogue records

**URI:** `dw:library_reserve_catalog`
  
[BVT-K-GAP-1] Snapshot row count: 99,999. MOST rows have NULL TITLE/AUTHOR — catalog stubs. CATALOG_YEAR='0' is the no-year placeholder (string '0', not numeric).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/library_reserve_catalog`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CATALOG_AUTHOR_NAME` | mnf:Varchar |  | yes |
| `CATALOG_ISBN` | mnf:Varchar |  | yes |
| `CATALOG_TITLE` | mnf:Varchar |  | yes |
| `CATALOG_YEAR` | mnf:Varchar |  | yes |
| `LIBRARY_RESERVE_CATALOG_KEY` | mnf:Varchar |  | no |

---

## dw.library_reserve_matrl_detail — pure linkage table (5 keys per row)

**URI:** `dw:library_reserve_matrl_detail`
  
[BVT-K-GAP-1] Snapshot row count: 58,377. Pure join table — no human-readable columns of its own.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/library_reserve_matrl_detail`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `LIBRARY_COURSE_INSTRUCTOR_KEY` | mnf:Varchar |  | yes |
| `LIBRARY_MATERIAL_STATUS_KEY` | mnf:Varchar |  | yes |
| `LIBRARY_RESERVE_CATALOG_KEY` | mnf:Varchar |  | yes |
| `LIBRARY_SUBJECT_OFFERED_KEY` | mnf:Varchar |  | yes |
| `SUBJECT_ID` | mnf:Varchar | dw:SubjectId | yes |
| `TERM_CODE` | mnf:Varchar | dw:TermCode | yes |

---

## dw.library_material_status — 6-value status lookup

**URI:** `dw:library_material_status`
  
[BVT-K-GAP-1] Snapshot row count: 6. KEY=CODE. 'R' has NULL description (data-quality blip). Codes: U/R/N/O/X/Y.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/library_material_status`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `LIBRARY_MATERIAL_STATUS` | mnf:Varchar |  | yes |
| `LIBRARY_MATERIAL_STATUS_KEY` | mnf:Varchar |  | no |

---

## dw.tip_subject_offered — TIP per-(subject, term) (2024+ only)

**URI:** `dw:tip_subject_offered`
  
TIP-side subjects-in-terms (newer system; 2024+).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/tip_subject_offered`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `IS_NO_COURSE_MATERIAL` | mnf:Varchar | dw:YNFlag | yes |
| `SUBJECT_ID` | mnf:Varchar | dw:SubjectId | yes |
| `SUBJECT_TITLE` | mnf:Varchar |  | yes |
| `TERM_CODE` | mnf:Varchar | dw:TermCode | yes |

---

## dw.tip_detail — TIP join table

**URI:** `dw:tip_detail`
  
[BVT-K-GAP-1] Snapshot row count: 83,902.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/tip_detail`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ISBN` | mnf:Varchar |  | yes |
| `SUBJECT_ID` | mnf:Varchar | dw:SubjectId | yes |
| `TERM_CODE` | mnf:Varchar | dw:TermCode | yes |
| `TIP_MATERIAL_KEY` | mnf:Varchar |  | yes |
| `TIP_MATERIAL_STATUS_KEY` | mnf:Varchar |  | yes |
| `TIP_SUBJECT_OFFERED_KEY` | mnf:Varchar |  | yes |

---

## dw.tip_material — textbook records with prices

**URI:** `dw:tip_material`
  
[BVT-K-GAP-1] Snapshot row count: 46,294. PK is ISBN + uppercase title + '0' suffix concatenated. AUTHOR may be right-padded with spaces. Real ISBNs and titles.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/tip_material`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `AUTHOR` | mnf:Varchar |  | yes |
| `ISBN` | mnf:Varchar |  | yes |
| `MATERIAL_INFO_SOURCE` | mnf:Varchar |  | yes |
| `NEW_SHELF_PRICE` | mnf:Integer |  | yes |
| `RENTAL_NEW_PRICE` | mnf:Integer |  | yes |
| `RENTAL_USED_PRICE` | mnf:Integer |  | yes |
| `TIP_MATERIAL_KEY` | mnf:Varchar |  | no |
| `TITLE` | mnf:Varchar |  | yes |
| `USED_SHELF_PRICE` | mnf:Integer |  | yes |

---

## dw.tip_material_status — 12-value status lookup with data-quality blips

**URI:** `dw:tip_material_status`
  
[BVT-K-GAP-1] Snapshot row count: 12. Multiple codes have NULL descriptions; one key is two literal spaces (' ').
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/tip_material_status`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `TIP_MATERIAL_STATUS` | mnf:Varchar |  | yes |
| `TIP_MATERIAL_STATUS_KEY` | mnf:Varchar |  | no |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| minor | tip_material_status has 12 rows but 4 of them ('NL', 'NS', 'NB', ' ') have NULL descriptions. One key is the literal two-space string ' '. |

---

## dw.employee_directory — MIT phonebook (Namespace A)

**URI:** `dw:employee_directory`
  
[BVT-K-GAP-1 / BVT-K-GAP-22] Snapshot row count: 17,763. THE canonical join target for subject_offered.RESPONSIBLE_FACULTY_MIT_ID (Namespace A). Email domains all anonymised (worker.com, gmail.business.com, etc.) — NO @mit.edu addresses survive.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/employee_directory`
  
**Entity key:** `MIT_ID`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DEPARTMENT_NUMBER` | mnf:Varchar |  | yes |
| `EMAIL_ADDRESS` | mnf:Varchar |  | yes |
| `EMAIL_ADDRESS_UPPERCASE` | mnf:Varchar |  | yes |
| `FIRST_NAME` | mnf:Varchar |  | yes |
| `FULL_NAME` | mnf:Varchar |  | yes |
| `HR_ORG_UNIT_ID` | mnf:Varchar |  | yes |
| `HR_ORG_UNIT_TITLE` | mnf:Varchar |  | yes |
| `KRB_NAME` | mnf:Varchar | dw:KrbName | yes |
| `KRB_NAME_UPPERCASE` | mnf:Varchar |  | yes |
| `LAST_NAME` | mnf:Varchar |  | yes |
| `MIT_ID` | mnf:Varchar | dw:MITID_NamespaceA | no |
| `OFFICE_LOCATION` | mnf:Varchar |  | yes |
| `OFFICE_PHONE` | mnf:Varchar |  | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| minor | employee_directory.EMAIL_ADDRESS values are anonymised — no @mit.edu addresses survive. Domains: worker.com (12K), gmail.business.com (4K), employee.com, hotmail.com, referer.com. |

---

## dw.drupal_employee_directory — Drupal-published mirror

**URI:** `dw:drupal_employee_directory`
  
[BVT-K-GAP-1 / BVT-K-GAP-23] Snapshot row count: 17,811. Mirror of employee_directory with Drupal-flavoured columns. Same MIT_ID Namespace A.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/drupal_employee_directory`
  
**Entity key:** `MIT_ID`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `EMPLOYEE_GROUP` | mnf:Varchar |  | yes |
| `EMPLOYEE_TYPE` | mnf:Varchar |  | yes |
| `FULL_NAME` | mnf:Varchar |  | yes |
| `MIT_ID` | mnf:Varchar | dw:MITID_NamespaceA | no |

---

## dw.mit_student_directory — student phonebook (NO MIT_ID)

**URI:** `dw:mit_student_directory`
  
NO MIT_ID column — students aren't joinable by ID via this table. Match on FULL_NAME or EMAIL_ADDRESS.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/mit_student_directory`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DEPARTMENT` | mnf:Varchar |  | yes |
| `EMAIL_ADDRESS` | mnf:Varchar |  | yes |
| `FULL_NAME` | mnf:Varchar |  | yes |
| `STUDENT_YEAR` | mnf:Varchar |  | yes |

---

## dw.se_person — payroll-flavoured people (Namespace B)

**URI:** `dw:se_person`
  
[BVT-K-GAP-1 / BVT-K-GAP-22] Snapshot row count: 18,710. MIT_ID is Namespace B — do NOT join to employee_directory.MIT_ID (returns 0 rows). All IS_ACTIVE='Y'.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/se_person`
  
**Entity key:** `MIT_ID`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `EMPLOYEE_TYPE` | mnf:Varchar |  | yes |
| `FULL_NAME` | mnf:Varchar |  | yes |
| `IS_ACTIVE` | mnf:Varchar | dw:YNFlag | no |
| `KRB_NAME` | mnf:Varchar | dw:KrbName | yes |
| `MIT_ID` | mnf:Varchar | dw:MITID_NamespaceB | no |
| `PAYROLL_RANK` | mnf:Varchar |  | yes |

---

## dw.hr_faculty_roster — faculty-only HR view (Namespace B)

**URI:** `dw:hr_faculty_roster`
  
[BVT-K-GAP-1 / BVT-K-GAP-22] Snapshot row count: 681. MIT_ID Namespace B.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/hr_faculty_roster`
  
**Entity key:** `MIT_ID`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `APPOINTMENT_TYPE` | mnf:Varchar |  | yes |
| `FIRST_NAME` | mnf:Varchar |  | yes |
| `JOB_TITLE` | mnf:Varchar |  | yes |
| `LAST_NAME` | mnf:Varchar |  | yes |
| `MIT_ID` | mnf:Varchar | dw:MITID_NamespaceB | no |

---

## dw.warehouse_users — staff + students union (Namespace B)

**URI:** `dw:warehouse_users`
  
[BVT-K-GAP-1 / BVT-K-GAP-22] Snapshot row count: 28,406. The largest people-bearing table. Namespace B.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/warehouse_users`
  
**Entity key:** `MIT_ID`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `KRB_NAME` | mnf:Varchar | dw:KrbName | yes |
| `MIT_ID` | mnf:Varchar | dw:MITID_NamespaceB | no |
| `OFFICE_LOCATION` | mnf:Varchar |  | yes |
| `TITLE` | mnf:Varchar |  | yes |
| `TYPE` | mnf:Varchar |  | yes |
| `UNIT_ID` | mnf:Varchar |  | yes |
| `UNIT_NAME` | mnf:Varchar |  | yes |
| `YEAR` | mnf:Varchar |  | yes |

---

## dw.person_auth_area — auth flags by KRB_NAME (UPPERCASE)

**URI:** `dw:person_auth_area`
  
[BVT-K-GAP-1 / BVT-K-GAP-25] Snapshot row count: 32,803. Keyed by USER_NAME (UPPERCASE Kerberos name). Cross-namespace bridge: same person can be looked up here regardless of MIT_ID namespace.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/person_auth_area`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `HAS_FINANCIAL_AUTH` | mnf:Varchar | dw:YNFlag | yes |
| `HAS_HR_FULL_AUTH` | mnf:Varchar | dw:YNFlag | yes |
| `HAS_HR_LIMITED_AUTH` | mnf:Varchar | dw:YNFlag | yes |
| `HAS_PAYROLL_AUTH` | mnf:Varchar | dw:YNFlag | yes |
| `USER_NAME` | mnf:Varchar | dw:KrbName | no |

---

## dw.student_department — student-side dept catalogue

**URI:** `dw:student_department`
  
[BVT-K-GAP-1] Snapshot row count: 79. Distinct from sis_department; covers programs (FOR Foreign Study, ASP, SDM).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/student_department`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DEPARTMENT_CODE` | mnf:Varchar |  | no |
| `DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `SCHOOL_CODE` | mnf:Varchar | dw:SchoolCode | yes |
| `SCHOOL_NAME` | mnf:Varchar |  | yes |

---

## dw.academic_terms_all — canonical term catalogue (300 rows, 1951-2030)

**URI:** `dw:academic_terms_all`
  
[BVT-K-GAP-1] Snapshot row count: 300. One row per (year, season). Date columns are Oracle DD-MON-YY strings.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/academic_terms_all`
  
**Entity key:** `TERM_CODE`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ACADEMIC_YEAR` | mnf:Varchar |  | yes |
| `FINANCIAL_AID_YEAR` | mnf:Varchar |  | yes |
| `FIRST_DAY_OF_CLASSES` | mnf:Varchar | dw:OracleDateString | yes |
| `IS_CURRENT_TERM` | mnf:Varchar | dw:YNFlag | yes |
| `LAST_DAY_OF_CLASSES` | mnf:Varchar | dw:OracleDateString | yes |
| `TERM_CODE` | mnf:Varchar | dw:TermCode | no |
| `TERM_DESCRIPTION` | mnf:Varchar |  | yes |
| `TERM_END_DATE` | mnf:Varchar | dw:OracleDateString | yes |
| `TERM_SELECTOR` | mnf:Varchar |  | yes |
| `TERM_START_DATE` | mnf:Varchar | dw:OracleDateString | yes |
| `TERM_STATUS_INDICATOR` | mnf:Varchar |  | yes |

---

## dw.academic_terms — current-relevant term subset (144 rows)

**URI:** `dw:academic_terms`
  
[BVT-K-GAP-1] Snapshot row count: 144. Strict subset of academic_terms_all. Adds IS_REGULAR_TERM, TERM_STATUS, ADD_DATE, DROP_DATE columns.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/academic_terms`
  
**Entity key:** `TERM_CODE`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ADD_DATE` | mnf:Varchar | dw:OracleDateString | yes |
| `DROP_DATE` | mnf:Varchar | dw:OracleDateString | yes |
| `IS_REGULAR_TERM` | mnf:Varchar | dw:YNFlag | yes |
| `TERM_CODE` | mnf:Varchar | dw:TermCode | no |
| `TERM_DESCRIPTION` | mnf:Varchar |  | yes |
| `TERM_STATUS` | mnf:Varchar |  | yes |

---

## dw.academic_term_parameter — pointer to current/previous/upcoming terms

**URI:** `dw:academic_term_parameter`
  
[BVT-K-GAP-1] Snapshot row count: 3. Single-row-per-pointer table.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/academic_term_parameter`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `IS_CURRENT_TERM` | mnf:Varchar | dw:YNFlag | yes |
| `TERM_CODE` | mnf:Varchar | dw:TermCode | no |
| `TERM_INDICATOR` | mnf:Varchar |  | yes |
| `TERM_PARAMETER` | mnf:Varchar |  | no |

---

## dw.time_day — daily fact table with fiscal/calendar/academic context

**URI:** `dw:time_day`
  
[BVT-K-GAP-1] Snapshot row count: 31,227. ~85 years of daily rows. NB: DAY_OF_WEEK is char(9) — values are space-padded ('Friday ').
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/time_day`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ACADEMIC_TERM_CODE` | mnf:Varchar | dw:TermCode | yes |
| `CALENDAR_DATE` | mnf:Varchar | dw:OracleDateString | no |
| `CALENDAR_PERIOD` | mnf:Varchar |  | yes |
| `CALENDAR_PERIOD_DESCRIPTION` | mnf:Varchar |  | yes |
| `DAY_OF_WEEK` | mnf:Varchar |  | no |
| `FISCAL_PERIOD` | mnf:Varchar |  | yes |
| `FISCAL_YEAR` | mnf:Varchar |  | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | [BVT-K-GAP-20] time_day.DAY_OF_WEEK is stored as char(9) padded with trailing spaces ('Friday ', 'Sunday '). WHERE DAY_OF_WEEK = 'Friday' returns 0 rows; needs RTRIM, LIKE 'Friday%', or the literal padded form. |

---

## dw.time_month — monthly granularity with fiscal context

**URI:** `dw:time_month`
  
[BVT-K-GAP-1] Snapshot row count: 640. 23 columns.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/time_month`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CALENDAR_PERIOD` | mnf:Varchar |  | yes |
| `FISCAL_PERIOD` | mnf:Varchar |  | yes |

---

## dw.time_quarter — quarterly granularity (fiscal + calendar)

**URI:** `dw:time_quarter`
  
[BVT-K-GAP-1] Snapshot row count: 144.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/time_quarter`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CY_QUARTER_CODE` | mnf:Varchar |  | yes |
| `FY_QUARTER_CODE` | mnf:Varchar |  | yes |

---

## dw.mit_holiday_closing_calendar — MIT closures

**URI:** `dw:mit_holiday_closing_calendar`
  
[BVT-K-GAP-1] Snapshot row count: 580. Standard Holiday descriptions all start with 'MIT ' (capital M, space). Emergency / Special closings have description = literal 'EMER' or 'SHOL'.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/mit_holiday_closing_calendar`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `HOLIDAY_CLOSING_DATE` | mnf:Varchar | dw:OracleDateString | no |
| `HOLIDAY_CLOSING_DESCRIPTION` | mnf:Varchar |  | yes |
| `HOLIDAY_CLOSING_TYPE` | mnf:Varchar |  | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | mit_holiday_closing_calendar.HOLIDAY_CLOSING_DESCRIPTION prepends 'MIT ' to every Standard Holiday name ('MIT Christmas Day'). Filtering on 'Christmas Day' without the prefix returns 0 rows. Emergency / Special closings have description set to the literal 'EMER' or 'SHOL' instead. |

---

## dw.frc_fiscal_periods — FY 2025 fiscal periods (incl. adjustments 13-16)

**URI:** `dw:frc_fiscal_periods`
  
[BVT-K-GAP-1 / BVT-K-GAP-27] Snapshot row count: 10. Includes adjustment-period rows for FY-end month June 2024 (FY periods 13-16).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/frc_fiscal_periods`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CALENDAR_PERIOD_DESCRIPTION` | mnf:Varchar |  | yes |
| `FISCAL_PERIOD` | mnf:Varchar |  | no |

---

## dw.moira_list — Moira mailing-list catalogue (with DUPLICATES)

**URI:** `dw:moira_list`
  
Only 58,071 distinct MOIRA_LIST_KEY values across the 100,000 rows — duplicates appear up to 4× with different flag combos (SCD-style snapshots folded together). USE DISTINCT before joining. MOIRA_LIST_DESCRIPTION is uniformly NULL.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/moira_list`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `IS_ACTIVE` | mnf:Varchar | dw:YNFlag | yes |
| `IS_HIDDEN` | mnf:Varchar | dw:YNFlag | yes |
| `IS_MOIRA_GROUP` | mnf:Varchar | dw:YNFlag | yes |
| `IS_MOIRA_MAILING_LIST` | mnf:Varchar | dw:YNFlag | yes |
| `IS_NFS_GROUP` | mnf:Varchar | dw:YNFlag | yes |
| `IS_PUBLIC` | mnf:Varchar | dw:YNFlag | yes |
| `MOIRA_LIST_DESCRIPTION` | mnf:Varchar |  | yes |
| `MOIRA_LIST_KEY` | mnf:Varchar |  | no |
| `MOIRA_LIST_NAME` | mnf:Varchar |  | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| moderate | [BVT-K-GAP-1] moira_list has 100,000 rows but only 58,071 distinct MOIRA_LIST_KEY values — same list appears up to 4× with different flag combinations (looks like SCD-style snapshots folded together). USE SELECT DISTINCT before joining. |
| minor | [BVT-K-GAP-13] moira_list.IS_ACTIVE is constant 'Y' (filter is no-op); IS_HIDDEN is constant 'N' (filter is no-op). |

---

## dw.moira_list_detail — list memberships (one (list, member) per row)

**URI:** `dw:moira_list_detail`
  
Half of all rows are non-person members (NULL MIT_ID + NULL FULL_NAME). 8,023 list keys appear here but NOT in moira_list (orphan memberships). MEMBER_MIT_ID is Namespace A.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/moira_list_detail`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `LAST_UPDATE_DATE` | mnf:Varchar | dw:OracleDateString | yes |
| `MOIRA_LIST_KEY` | mnf:Varchar |  | yes |
| `MOIRA_LIST_MEMBER` | mnf:Varchar | dw:KrbName | yes |
| `MOIRA_LIST_MEMBER_FULL_NAME` | mnf:Varchar |  | yes |
| `MOIRA_LIST_MEMBER_MIT_ID` | mnf:Varchar | dw:MITID_NamespaceA | yes |
| `MOIRA_LIST_OWNER_KEY` | mnf:Varchar |  | yes |

### Known Deficiencies

| Severity | Description |
|----------|-------------|
| minor | 8,023 list keys appear in moira_list_detail but not in moira_list (orphan memberships). Conversely, 39,511 list keys (68% of distinct moira_list keys) have ZERO member rows in detail. |

---

## dw.moira_list_owner — owner identity catalogue (NOT keyed by list)

**URI:** `dw:moira_list_owner`
  
[BVT-K-GAP-1 / BVT-K-GAP-29] Snapshot row count: 46,427. PK = OWNER_TYPE + owner-name CONCATENATED (no delimiter): 'LIST56.928-tangerine-snake', 'USER74.097-...', 'KERBEROSorange-quokka', 'NONENONE'. dw/118 references one such literal exactly.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/moira_list_owner`
  
**Entity key:** `MOIRA_LIST_OWNER_KEY`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `MOIRA_LIST_OWNER_KEY` | mnf:Varchar |  | no |
| `OWNER` | mnf:Varchar |  | yes |
| `OWNER_TYPE` | mnf:Varchar | dw:OwnerType | yes |

---

## dw.cip — Federal CIP program taxonomy (4 editions stacked)

**URI:** `dw:cip`
  
[BVT-K-GAP-1] Snapshot row count: 3,059. US Department of Education taxonomy. VERSION values stack 1990, 2000, 2010, 2020 in one table.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/cip`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `PROGRAM_CODE` | mnf:Varchar | dw:CIPCode | no |
| `PROGRAM_TITLE` | mnf:Varchar |  | yes |
| `VERSION` | mnf:Varchar |  | yes |

---

## dw.zpm_rooms_load — SAP ZPM room/HR-org-unit binding

**URI:** `dw:zpm_rooms_load`
  
[BVT-K-GAP-1] Snapshot row count: 43,174. Links building-rooms to HR-org-units (who occupies what room).
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/zpm_rooms_load`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `BUILDING_ROOM` | mnf:Varchar |  | no |
| `FLOOR` | mnf:Varchar |  | yes |
| `HR_ORG_UNIT_ID` | mnf:Varchar |  | yes |
| `SPACE_UNIT_CODE` | mnf:Varchar |  | yes |

---

## dw.roles_fin_pa — financial-PA roles by user (lowercase KRB)

**URI:** `dw:roles_fin_pa`
  
[BVT-K-GAP-1 / BVT-K-GAP-25] Snapshot row count: 1,395. USERNAME is lowercase here vs UPPERCASE in person_auth_area.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/roles_fin_pa`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DLC_KEY` | mnf:Varchar | dw:DLCKey | no |
| `USERNAME` | mnf:Varchar | dw:KrbName | no |

---

## dw.estimated_surcharges_estonly — schema stub (empty in this dump)

**URI:** `dw:estimated_surcharges_estonly`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/estimated_surcharges_estonly`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `AMOUNT` | mnf:Double |  | yes |
| `ANNUAL_FORECAST_BUDGET` | mnf:Double |  | yes |
| `COMMITMENT_AMOUNT` | mnf:Double |  | yes |
| `COMMITMENT_AMOUNT_FY` | mnf:Double |  | yes |
| `COST_COLLECTOR_FP_KEY` | mnf:Varchar |  | yes |
| `COST_COLLECTOR_FY_KEY` | mnf:Varchar |  | yes |
| `COST_COLLECTOR_KEY` | mnf:Varchar |  | yes |
| `CUMULATIVE_AMOUNT` | mnf:Double |  | yes |
| `DEPARTMENT_BUDGET` | mnf:Double |  | yes |
| `FYTD_AMOUNT` | mnf:Double |  | yes |
| `FYTD_DEPARTMENT_BUDGET` | mnf:Double |  | yes |
| `FYTD_INSTITUTE_BUDGET` | mnf:Double |  | yes |
| `GL_ACCOUNT_KEY` | mnf:Varchar |  | yes |
| `INSTITUTE_BUDGET` | mnf:Double |  | yes |
| `NON_BL_ORDER_COMMITMENT_AMOUNT` | mnf:Double |  | yes |
| `NON_BL_ORDER_COMMIT_AMOUNT_FY` | mnf:Double |  | yes |
| `RECORD_COUNTER` | mnf:Double |  | yes |
| `RECORD_TYPE` | mnf:Varchar |  | yes |
| `TIME_MONTH_KEY` | mnf:Varchar |  | yes |
| `TOTAL_DEPARTMENT_BUDGET` | mnf:Double |  | yes |
| `TOTAL_INSTITUTE_BUDGET` | mnf:Double |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.fund_center_hierarchy — schema stub (empty in this dump)

**URI:** `dw:fund_center_hierarchy`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fund_center_hierarchy`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `FUND_CENTER_ID` | mnf:Varchar |  | yes |
| `FUND_CENTER_ID_LEVEL1` | mnf:Varchar |  | yes |
| `FUND_CENTER_ID_LEVEL10` | mnf:Varchar |  | yes |
| `FUND_CENTER_ID_LEVEL2` | mnf:Varchar |  | yes |
| `FUND_CENTER_ID_LEVEL3` | mnf:Varchar |  | yes |
| `FUND_CENTER_ID_LEVEL4` | mnf:Varchar |  | yes |
| `FUND_CENTER_ID_LEVEL5` | mnf:Varchar |  | yes |
| `FUND_CENTER_ID_LEVEL6` | mnf:Varchar |  | yes |
| `FUND_CENTER_ID_LEVEL7` | mnf:Varchar |  | yes |
| `FUND_CENTER_ID_LEVEL8` | mnf:Varchar |  | yes |
| `FUND_CENTER_ID_LEVEL9` | mnf:Varchar |  | yes |
| `FUND_CENTER_KEY` | mnf:Varchar |  | yes |
| `FUND_CENTER_NAME` | mnf:Varchar |  | yes |
| `FUND_CENTER_NAME_LEVEL1` | mnf:Varchar |  | yes |
| `FUND_CENTER_NAME_LEVEL10` | mnf:Varchar |  | yes |
| `FUND_CENTER_NAME_LEVEL2` | mnf:Varchar |  | yes |
| `FUND_CENTER_NAME_LEVEL3` | mnf:Varchar |  | yes |
| `FUND_CENTER_NAME_LEVEL4` | mnf:Varchar |  | yes |
| `FUND_CENTER_NAME_LEVEL5` | mnf:Varchar |  | yes |
| `FUND_CENTER_NAME_LEVEL6` | mnf:Varchar |  | yes |
| `FUND_CENTER_NAME_LEVEL7` | mnf:Varchar |  | yes |
| `FUND_CENTER_NAME_LEVEL8` | mnf:Varchar |  | yes |
| `FUND_CENTER_NAME_LEVEL9` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.opa_person_current — schema stub (empty in this dump)

**URI:** `dw:opa_person_current`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/opa_person_current`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ADMIN_EMPLOYEE_TYPE` | mnf:Varchar |  | yes |
| `ADMIN_ORG_UNIT_TITLE` | mnf:Varchar |  | yes |
| `ADMIN_POSITION_TITLE` | mnf:Varchar |  | yes |
| `EMAIL_ADDRESS` | mnf:Varchar |  | yes |
| `EMPLOYMENT_PERCENT` | mnf:Double |  | yes |
| `FIRST_NAME` | mnf:Varchar |  | yes |
| `FORM_OF_ADDRESS_SHORT` | mnf:Varchar |  | yes |
| `FULL_NAME` | mnf:Varchar |  | yes |
| `HR_DEPARTMENT_CODE_OLD` | mnf:Varchar |  | yes |
| `HR_DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `HR_ORG_UNIT_ID` | mnf:Varchar |  | yes |
| `IS_6MO_APPT` | mnf:Varchar |  | yes |
| `IS_CONSULT_PRIV` | mnf:Varchar |  | yes |
| `IS_FACULTY` | mnf:Varchar |  | yes |
| `IS_OPA_REQUIRED` | mnf:Varchar |  | yes |
| `IS_PAID_APPT` | mnf:Varchar |  | yes |
| `IS_SABBATICAL` | mnf:Varchar |  | yes |
| `IS_SUMMER_SESSION_APPT` | mnf:Varchar |  | yes |
| `JOB_ID` | mnf:Varchar |  | yes |
| `JOB_TITLE` | mnf:Varchar |  | yes |
| `KRB_NAME_UPPERCASE` | mnf:Varchar |  | yes |
| `LAST_NAME` | mnf:Varchar |  | yes |
| `MIDDLE_NAME` | mnf:Varchar |  | yes |
| `MIT_ID` | mnf:Varchar |  | yes |
| `PAYROLL_RANK` | mnf:Varchar |  | yes |
| `PERSONNEL_SUBAREA` | mnf:Varchar |  | yes |
| `PERSONNEL_SUBAREA_CODE` | mnf:Varchar |  | yes |
| `SABBATICAL_BEGIN_DATE` | mnf:Varchar |  | yes |
| `SABBATICAL_END_DATE` | mnf:Varchar |  | yes |
| `SUMMER_SESSION_MONTHS` | mnf:Double |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.profit_center_group — schema stub (empty in this dump)

**URI:** `dw:profit_center_group`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/profit_center_group`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DLC_KEY` | mnf:Varchar |  | yes |
| `DLC_NAME` | mnf:Varchar |  | yes |
| `PC_LEVEL1_CATEGORY` | mnf:Varchar |  | yes |
| `PC_LEVEL1_SORT` | mnf:Double |  | yes |
| `PC_LEVEL2_CATEGORY` | mnf:Varchar |  | yes |
| `PC_LEVEL2_SORT` | mnf:Double |  | yes |
| `PC_LEVEL3_CATEGORY` | mnf:Varchar |  | yes |
| `PC_LEVEL3_SORT` | mnf:Double |  | yes |
| `PC_LEVEL4_CATEGORY` | mnf:Varchar |  | yes |
| `PC_LEVEL4_SORT` | mnf:Double |  | yes |
| `PC_LEVEL5_CATEGORY` | mnf:Varchar |  | yes |
| `PC_LEVEL5_SORT` | mnf:Double |  | yes |
| `PC_LEVEL6_CATEGORY` | mnf:Varchar |  | yes |
| `PC_LEVEL6_SORT` | mnf:Double |  | yes |
| `PC_LEVEL7_CATEGORY` | mnf:Varchar |  | yes |
| `PC_LEVEL7_SORT` | mnf:Double |  | yes |
| `PC_LEVEL8_CATEGORY` | mnf:Varchar |  | yes |
| `PC_LEVEL8_SORT` | mnf:Varchar |  | yes |
| `PROFIT_CENTER_GROUP_CODE` | mnf:Varchar |  | yes |
| `PROFIT_CENTER_GROUP_NAME` | mnf:Varchar |  | yes |
| `PROFIT_CENTER_ID` | mnf:Double |  | yes |
| `PROFIT_CENTER_KEY` | mnf:Varchar |  | yes |
| `PROFIT_CENTER_NAME` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.subject_selector — schema stub (empty in this dump)

**URI:** `dw:subject_selector`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/subject_selector`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CLUSTER_LIST` | mnf:Varchar |  | yes |
| `CLUSTER_TYPE` | mnf:Varchar |  | yes |
| `CLUSTER_TYPE_DESC` | mnf:Varchar |  | yes |
| `DEPARTMENT_CODE` | mnf:Varchar |  | yes |
| `DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `MASTER_SUBJECT_ID` | mnf:Varchar |  | yes |
| `SCHOOL_CODE` | mnf:Varchar |  | yes |
| `SCHOOL_NAME` | mnf:Varchar |  | yes |
| `SUBJECT_GROUP_ID` | mnf:Varchar |  | yes |
| `SUBJECT_ID` | mnf:Varchar |  | yes |
| `SUBJECT_ID_SORT` | mnf:Varchar |  | yes |
| `SUBJECT_OR_CLUSTER` | mnf:Varchar |  | yes |
| `SUBJECT_SUMMARY_KEY` | mnf:Varchar |  | yes |
| `TERM_CODE` | mnf:Varchar |  | yes |
| `ULT_MASTER_SUBJECT_ID` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.fclt_building_address_hist — schema stub (SCD-2 history table — vocab gap (GAP-16))

**URI:** `dw:fclt_building_address_hist`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_building_address_hist`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ADDRESS_CITY_ID` | mnf:Varchar |  | yes |
| `ADDRESS_PURPOSE` | mnf:Varchar |  | yes |
| `BUILDING_NUMBER` | mnf:Varchar |  | yes |
| `CITY` | mnf:Varchar |  | yes |
| `FCLT_BUILDING_ADDRESS_HIST_KEY` | mnf:Varchar |  | yes |
| `FCLT_BUILDING_ADDRESS_KEY` | mnf:Varchar |  | yes |
| `FCLT_BUILDING_KEY` | mnf:Varchar |  | yes |
| `FISCAL_PERIOD` | mnf:Varchar |  | yes |
| `IS_E911_ADDRESS` | mnf:Varchar |  | yes |
| `POSTAL_CODE` | mnf:Varchar |  | yes |
| `POST_DIRECTIONAL` | mnf:Varchar |  | yes |
| `PRE_DIRECTIONAL` | mnf:Varchar |  | yes |
| `STATE` | mnf:Varchar |  | yes |
| `STREET_NAME` | mnf:Varchar |  | yes |
| `STREET_NUMBER` | mnf:Varchar |  | yes |
| `STREET_NUMBER_SUFFIX` | mnf:Varchar |  | yes |
| `STREET_SUFFIX` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.fclt_building_hist — schema stub (SCD-2 history table — vocab gap (GAP-16))

**URI:** `dw:fclt_building_hist`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_building_hist`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ACCESS_LEVEL_CODE` | mnf:Double |  | yes |
| `ACCESS_LEVEL_NAME` | mnf:Varchar |  | yes |
| `ASSIGNABLE_AREA` | mnf:Double |  | yes |
| `BUILDING_HEIGHT` | mnf:Varchar |  | yes |
| `BUILDING_NAME` | mnf:Varchar |  | yes |
| `BUILDING_NAMED_FOR` | mnf:Varchar |  | yes |
| `BUILDING_NAME_LONG` | mnf:Varchar |  | yes |
| `BUILDING_NUMBER` | mnf:Varchar |  | yes |
| `BUILDING_SORT` | mnf:Varchar |  | yes |
| `BUILDING_TYPE` | mnf:Varchar |  | yes |
| `BUILDING_USE` | mnf:Varchar |  | yes |
| `CAMPUS_SECTOR` | mnf:Varchar |  | yes |
| `COST_CENTER_CODE` | mnf:Varchar |  | yes |
| `COST_COLLECTOR_KEY` | mnf:Varchar |  | yes |
| `DATE_ACQUIRED` | mnf:Varchar |  | yes |
| `DATE_BUILT` | mnf:Varchar |  | yes |
| `DATE_OCCUPIED` | mnf:Varchar |  | yes |
| `EASTING_X_SPCS` | mnf:Double |  | yes |
| `EXT_GROSS_AREA` | mnf:Double |  | yes |
| `FCLT_BUILDING_HIST_KEY` | mnf:Varchar |  | yes |
| `FCLT_BUILDING_KEY` | mnf:Varchar |  | yes |
| `FISCAL_PERIOD` | mnf:Varchar |  | yes |
| `LATITUDE_WGS` | mnf:Double |  | yes |
| `LONGITUDE_WGS` | mnf:Double |  | yes |
| `NON_ASSIGNABLE_AREA` | mnf:Double |  | yes |
| `NORTHING_Y_SPCS` | mnf:Double |  | yes |
| `NUM_OF_ROOMS` | mnf:Double |  | yes |
| `OCCUPANCY_CLASS` | mnf:Varchar |  | yes |
| `OWNERSHIP_TYPE` | mnf:Varchar |  | yes |
| `PARENT_BUILDING_NAME` | mnf:Varchar |  | yes |
| `PARENT_BUILDING_NAME_LONG` | mnf:Varchar |  | yes |
| `PARENT_BUILDING_NUMBER` | mnf:Varchar |  | yes |
| `SITE` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.fclt_building_hist_1 — schema stub (SCD-2 history table — vocab gap (GAP-16))

**URI:** `dw:fclt_building_hist_1`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_building_hist_1`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ACCESS_LEVEL_CODE` | mnf:Double |  | yes |
| `ACCESS_LEVEL_NAME` | mnf:Varchar |  | yes |
| `ASSIGNABLE_AREA` | mnf:Double |  | yes |
| `BUILDING_HEIGHT` | mnf:Varchar |  | yes |
| `BUILDING_NAME` | mnf:Varchar |  | yes |
| `BUILDING_NAMED_FOR` | mnf:Varchar |  | yes |
| `BUILDING_NAME_LONG` | mnf:Varchar |  | yes |
| `BUILDING_NUMBER` | mnf:Varchar |  | yes |
| `BUILDING_SORT` | mnf:Varchar |  | yes |
| `BUILDING_TYPE` | mnf:Varchar |  | yes |
| `BUILDING_USE` | mnf:Varchar |  | yes |
| `CAMPUS_SECTOR` | mnf:Varchar |  | yes |
| `COST_CENTER_CODE` | mnf:Varchar |  | yes |
| `COST_COLLECTOR_KEY` | mnf:Varchar |  | yes |
| `DATE_ACQUIRED` | mnf:Varchar |  | yes |
| `DATE_BUILT` | mnf:Varchar |  | yes |
| `DATE_OCCUPIED` | mnf:Varchar |  | yes |
| `EASTING_X_SPCS` | mnf:Double |  | yes |
| `EXT_GROSS_AREA` | mnf:Double |  | yes |
| `FCLT_BUILDING_HIST_KEY` | mnf:Varchar |  | yes |
| `FCLT_BUILDING_KEY` | mnf:Varchar |  | yes |
| `FISCAL_PERIOD` | mnf:Varchar |  | yes |
| `LATITUDE_WGS` | mnf:Double |  | yes |
| `LONGITUDE_WGS` | mnf:Double |  | yes |
| `NON_ASSIGNABLE_AREA` | mnf:Double |  | yes |
| `NORTHING_Y_SPCS` | mnf:Double |  | yes |
| `NUM_OF_ROOMS` | mnf:Double |  | yes |
| `OCCUPANCY_CLASS` | mnf:Varchar |  | yes |
| `OWNERSHIP_TYPE` | mnf:Varchar |  | yes |
| `PARENT_BUILDING_NAME` | mnf:Varchar |  | yes |
| `PARENT_BUILDING_NAME_LONG` | mnf:Varchar |  | yes |
| `PARENT_BUILDING_NUMBER` | mnf:Varchar |  | yes |
| `SITE` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.fclt_floor_hist — schema stub (SCD-2 history table — vocab gap (GAP-16))

**URI:** `dw:fclt_floor_hist`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_floor_hist`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ACCESS_LEVEL` | mnf:Varchar |  | yes |
| `ASSIGNABLE_AREA` | mnf:Double |  | yes |
| `BUILDING_WINGS_ID` | mnf:Varchar |  | yes |
| `EXT_GROSS_AREA` | mnf:Double |  | yes |
| `FCLT_BUILDING_KEY` | mnf:Varchar |  | yes |
| `FCLT_FLOOR_HIST_KEY` | mnf:Varchar |  | yes |
| `FCLT_FLOOR_KEY` | mnf:Varchar |  | yes |
| `FISCAL_PERIOD` | mnf:Varchar |  | yes |
| `FLOOR` | mnf:Varchar |  | yes |
| `FLOOR_SORT_SEQUENCE` | mnf:Varchar |  | yes |
| `LEVEL_ID` | mnf:Varchar |  | yes |
| `NON_ASSIGNABLE_AREA` | mnf:Double |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.fclt_major_use_hist — schema stub (SCD-2 history table — vocab gap (GAP-16))

**URI:** `dw:fclt_major_use_hist`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_major_use_hist`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ASSIGNABLE` | mnf:Varchar |  | yes |
| `DESCRIPTION` | mnf:Varchar |  | yes |
| `FCLT_MAJOR_USE_HIST_KEY` | mnf:Varchar |  | yes |
| `FCLT_MAJOR_USE_KEY` | mnf:Varchar |  | yes |
| `FISCAL_PERIOD` | mnf:Varchar |  | yes |
| `MAJOR_USE` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.fclt_organization_hist — schema stub (SCD-2 history table — vocab gap (GAP-16))

**URI:** `dw:fclt_organization_hist`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_organization_hist`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ASSIGNABLE` | mnf:Varchar |  | yes |
| `COURSE` | mnf:Varchar |  | yes |
| `DESCRIPTION` | mnf:Varchar |  | yes |
| `DLC_KEY` | mnf:Varchar |  | yes |
| `DLC_NAME` | mnf:Varchar |  | yes |
| `FCLT_MAJOR_ORG_KEY` | mnf:Varchar |  | yes |
| `FCLT_ORGANIZATION_HIST_KEY` | mnf:Varchar |  | yes |
| `FCLT_ORGANIZATION_KEY` | mnf:Varchar |  | yes |
| `FCLT_ORG_PARENT_KEY` | mnf:Varchar |  | yes |
| `FISCAL_PERIOD` | mnf:Varchar |  | yes |
| `HR_DEPARTMENT_CODE_OLD` | mnf:Varchar |  | yes |
| `HR_DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `HR_ORG_UNIT_ID` | mnf:Varchar |  | yes |
| `MAJOR_ORG` | mnf:Varchar |  | yes |
| `ORGANIZATION` | mnf:Varchar |  | yes |
| `ORGANIZATION_ID` | mnf:Varchar |  | yes |
| `ORGANIZATION_LEVEL` | mnf:Varchar |  | yes |
| `ORGANIZATION_NAME` | mnf:Varchar |  | yes |
| `ORGANIZATION_NUMBER` | mnf:Varchar |  | yes |
| `ORGANIZATION_SORT` | mnf:Varchar |  | yes |
| `ORG_PARENT` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.fclt_rooms_hist — schema stub (SCD-2 history table — vocab gap (GAP-16))

**URI:** `dw:fclt_rooms_hist`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fclt_rooms_hist`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ACCESS_LEVEL` | mnf:Varchar |  | yes |
| `AREA` | mnf:Double |  | yes |
| `BUILDING_ROOM` | mnf:Varchar |  | yes |
| `DEPT_CODE` | mnf:Varchar |  | yes |
| `EASTING_SPCS` | mnf:Double |  | yes |
| `FCLT_BUILDING_KEY` | mnf:Varchar |  | yes |
| `FCLT_FLOOR_KEY` | mnf:Varchar |  | yes |
| `FCLT_MAJOR_USE_KEY` | mnf:Varchar |  | yes |
| `FCLT_MINOR_ORGANIZATION_KEY` | mnf:Varchar |  | yes |
| `FCLT_MINOR_USE_KEY` | mnf:Varchar |  | yes |
| `FCLT_ORGANIZATION_KEY` | mnf:Varchar |  | yes |
| `FCLT_ROOM_HIST_KEY` | mnf:Varchar |  | yes |
| `FCLT_ROOM_KEY` | mnf:Varchar |  | yes |
| `FCLT_USE_KEY` | mnf:Varchar |  | yes |
| `FISCAL_PERIOD` | mnf:Varchar |  | yes |
| `FLOOR` | mnf:Varchar |  | yes |
| `LATITUDE_WGS` | mnf:Double |  | yes |
| `LONGITUDE_WGS` | mnf:Double |  | yes |
| `MAJOR_USE_DESC` | mnf:Varchar |  | yes |
| `MINOR_ORGANIZATION` | mnf:Varchar |  | yes |
| `MINOR_USE_DESC` | mnf:Varchar |  | yes |
| `NORTHING_SPCS` | mnf:Double |  | yes |
| `ORGANIZATION_NAME` | mnf:Varchar |  | yes |
| `ROOM` | mnf:Varchar |  | yes |
| `ROOM_FULL_NAME` | mnf:Varchar |  | yes |
| `SPACE_ID` | mnf:Varchar |  | yes |
| `USE_DESC` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.drupal_course_catalog — schema stub (cross-system mirror (see GAP-23))

**URI:** `dw:drupal_course_catalog`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/drupal_course_catalog`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ACADEMIC_YEAR` | mnf:Varchar |  | yes |
| `COMM_REQ_ATTRIBUTE` | mnf:Varchar |  | yes |
| `COMM_REQ_ATTRIBUTE_DESC` | mnf:Varchar |  | yes |
| `DEPARTMENT_CODE` | mnf:Varchar |  | yes |
| `DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `DESIGN_UNITS` | mnf:Double |  | yes |
| `EFFECTIVE_TERM_CODE` | mnf:Varchar |  | yes |
| `EQUIVALENT_SUBJECTS` | mnf:Varchar |  | yes |
| `FALL_INSTRUCTORS` | mnf:Varchar |  | yes |
| `GIR_ATTRIBUTE` | mnf:Varchar |  | yes |
| `GIR_ATTRIBUTE_DESC` | mnf:Varchar |  | yes |
| `GLOBAL_COUNTRIES` | mnf:Varchar |  | yes |
| `GLOBAL_REGIONS` | mnf:Varchar |  | yes |
| `GRADE_RULE` | mnf:Varchar |  | yes |
| `GRADE_RULE_DESC` | mnf:Varchar |  | yes |
| `GRADE_TYPE` | mnf:Varchar |  | yes |
| `GRADE_TYPE_DESC` | mnf:Varchar |  | yes |
| `HASS_ATTRIBUTE` | mnf:Varchar |  | yes |
| `HASS_ATTRIBUTE_DESC` | mnf:Varchar |  | yes |
| `HGN_CODE` | mnf:Varchar |  | yes |
| `HGN_DESC` | mnf:Varchar |  | yes |
| `HGN_EXCEPT` | mnf:Varchar |  | yes |
| `IS_DESIGN_SECTION` | mnf:Varchar |  | yes |
| `IS_LAB_SECTION` | mnf:Varchar |  | yes |
| `IS_LECTURE_SECTION` | mnf:Varchar |  | yes |
| `IS_MASTER_SECTION` | mnf:Varchar |  | yes |
| `IS_OFFERED_FALL_TERM` | mnf:Varchar |  | yes |
| `IS_OFFERED_IAP` | mnf:Varchar |  | yes |
| `IS_OFFERED_SPRING_TERM` | mnf:Varchar |  | yes |
| `IS_OFFERED_SUMMER_TERM` | mnf:Varchar |  | yes |
| `IS_OFFERED_THIS_YEAR` | mnf:Varchar |  | yes |
| `IS_PRINTED_IN_BULLETIN` | mnf:Varchar |  | yes |
| `IS_RECITATION_SECTION` | mnf:Varchar |  | yes |
| `IS_VARIABLE_UNITS` | mnf:Varchar |  | yes |
| `JOINT_SUBJECTS` | mnf:Varchar |  | yes |
| `LAB_UNITS` | mnf:Double |  | yes |
| `LAST_ACTIVITY_DATE` | mnf:Varchar |  | yes |
| `LECTURE_UNITS` | mnf:Double |  | yes |
| `MASTER_SUBJECT_ID` | mnf:Varchar |  | yes |
| `MEETS_WITH_SUBJECTS` | mnf:Varchar |  | yes |
| `MEET_PLACE` | mnf:Varchar |  | yes |
| `MEET_TIME` | mnf:Varchar |  | yes |
| `ON_LINE_PAGE_NUMBER` | mnf:Varchar |  | yes |
| `PREPARATION_UNITS` | mnf:Double |  | yes |
| `PREREQUISITES` | mnf:Varchar |  | yes |
| `PRINT_SUBJECT_ID` | mnf:Varchar |  | yes |
| `RESPONSIBLE_FACULTY_MIT_ID` | mnf:Varchar |  | yes |
| `RESPONSIBLE_FACULTY_NAME` | mnf:Varchar |  | yes |
| `SCHOOL_WIDE_ELECTIVES` | mnf:Varchar |  | yes |
| `SECTION_ID` | mnf:Varchar |  | yes |
| `SOURCE_SUBJECT_ID` | mnf:Varchar |  | yes |
| `SO_CLUSTER_TYPE` | mnf:Varchar |  | yes |
| `SO_SUBJECT_ID` | mnf:Varchar |  | yes |
| `SO_TERM_CODE` | mnf:Varchar |  | yes |
| `SO_TERM_DESCRIPTION` | mnf:Varchar |  | yes |
| `SPRING_INSTRUCTORS` | mnf:Varchar |  | yes |
| `STATUS_CHANGE` | mnf:Varchar |  | yes |
| `SUBJECT_CODE` | mnf:Varchar |  | yes |
| `SUBJECT_DESCRIPTION` | mnf:Varchar |  | yes |
| `SUBJECT_ID` | mnf:Varchar |  | yes |
| `SUBJECT_NUMBER` | mnf:Varchar |  | yes |
| `SUBJECT_SHORT_TITLE` | mnf:Varchar |  | yes |
| `SUBJECT_TITLE` | mnf:Varchar |  | yes |
| `SUPERVISOR_ATTRIBUTE` | mnf:Varchar |  | yes |
| `SUPERVISOR_ATTRIBUTE_DESC` | mnf:Varchar |  | yes |
| `TERM_DURATION` | mnf:Varchar |  | yes |
| `TOTAL_UNITS` | mnf:Double |  | yes |
| `TUITION_ATTRIBUTE` | mnf:Varchar |  | yes |
| `TUITION_ATTRIBUTE_DESC` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |
| `WRITE_REQ_ATTRIBUTE` | mnf:Varchar |  | yes |
| `WRITE_REQ_ATTRIBUTE_DESC` | mnf:Varchar |  | yes |

---

## dw.cip_with_version — schema stub (reference / lookup)

**URI:** `dw:cip_with_version`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/cip_with_version`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CATEGORY_CODE` | mnf:Varchar |  | yes |
| `CATEGORY_TITLE` | mnf:Varchar |  | yes |
| `CIP_WITH_VERSION_KEY` | mnf:Varchar |  | yes |
| `FOUR_DIGIT_CODE` | mnf:Varchar |  | yes |
| `FOUR_DIGIT_TITLE` | mnf:Varchar |  | yes |
| `PROGRAM_CODE` | mnf:Varchar |  | yes |
| `PROGRAM_TITLE` | mnf:Varchar |  | yes |
| `VERSION` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.fac_major_use — schema stub (reference / lookup)

**URI:** `dw:fac_major_use`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/fac_major_use`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ASSIGNABLE` | mnf:Varchar |  | yes |
| `DESCRIPTION` | mnf:Varchar |  | yes |
| `MAJOR_USE` | mnf:Varchar |  | yes |
| `MAJOR_USE_KEY` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.ir_institution — schema stub (reference / lookup)

**URI:** `dw:ir_institution`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/ir_institution`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ALTERNATE_INSTITUTION_NAME` | mnf:Varchar |  | yes |
| `CITY` | mnf:Varchar |  | yes |
| `COUNTRY` | mnf:Varchar |  | yes |
| `COUNTRY_CODE` | mnf:Varchar |  | yes |
| `INSTITUTION_CATEGORY_LABEL` | mnf:Varchar |  | yes |
| `INSTITUTION_CATEGORY_VALUE` | mnf:Double |  | yes |
| `INSTITUTION_ID` | mnf:Varchar |  | yes |
| `INSTITUTION_NAME` | mnf:Varchar |  | yes |
| `INSTITUTION_SORT_ORDER` | mnf:Varchar |  | yes |
| `RECORD_CREATED_DATE` | mnf:Varchar |  | yes |
| `STATE` | mnf:Varchar |  | yes |
| `STREET_ADDRESS` | mnf:Varchar |  | yes |
| `ZIP` | mnf:Varchar |  | yes |

---

## dw.sis_lookup — schema stub (reference / lookup)

**URI:** `dw:sis_lookup`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/sis_lookup`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CODE` | mnf:Varchar |  | yes |
| `DESCRIPTION` | mnf:Varchar |  | yes |
| `LOOKUP_TYPE` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.sis_term_address_category — schema stub (reference / lookup)

**URI:** `dw:sis_term_address_category`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/sis_term_address_category`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `LAST_ACTIVITY_DATE` | mnf:Varchar |  | yes |
| `LIVING_GROUP_TYPE` | mnf:Varchar |  | yes |
| `LIVING_GROUP_TYPE_DESC` | mnf:Varchar |  | yes |
| `TERM_ADDRESS_CATEGORY` | mnf:Varchar |  | yes |
| `TERM_ADDRESS_CATEGORY_CODE` | mnf:Varchar |  | yes |
| `VALID_FROM_DATE` | mnf:Varchar |  | yes |
| `VALID_THRU_DATE` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.student_degree_program — schema stub (reference / lookup)

**URI:** `dw:student_degree_program`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/student_degree_program`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `COMMENCEMENT_BK_COURSE_ROMAN` | mnf:Varchar |  | yes |
| `COMMENCEMENT_BK_SEE_ALSO` | mnf:Varchar |  | yes |
| `COURSE` | mnf:Varchar |  | yes |
| `COURSE_LAST_ACTIVITY_DATE` | mnf:Varchar |  | yes |
| `COURSE_LEVEL` | mnf:Varchar |  | yes |
| `DEGREE_CODE` | mnf:Varchar |  | yes |
| `DEGREE_DESC` | mnf:Varchar |  | yes |
| `DEGREE_DESC_SHORT` | mnf:Varchar |  | yes |
| `DEGREE_LAST_ACTIVITY_DATE` | mnf:Varchar |  | yes |
| `DEGREE_TYPE` | mnf:Varchar |  | yes |
| `DEGREE_TYPE_DESC` | mnf:Varchar |  | yes |
| `DEGREE_WEIGHT` | mnf:Double |  | yes |
| `DEPARTMENT` | mnf:Varchar |  | yes |
| `DEPT_NAME_IN_COMMENCEMENT_BK` | mnf:Varchar |  | yes |
| `FROM_TERM` | mnf:Varchar |  | yes |
| `IS_DOUBLE_MAJOR` | mnf:Varchar |  | yes |
| `SCHOOL_NAME_IN_COMMENCEMENT_BK` | mnf:Varchar |  | yes |
| `THRU_TERM` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.student_ethnic_subgroup — schema stub (reference / lookup)

**URI:** `dw:student_ethnic_subgroup`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/student_ethnic_subgroup`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `ETHNIC_CODE` | mnf:Varchar |  | yes |
| `ETHNIC_GROUP_NAME` | mnf:Varchar |  | yes |
| `ETHNIC_SUBGROUP_CODE` | mnf:Varchar |  | yes |
| `ETHNIC_SUBGROUP_NAME` | mnf:Varchar |  | yes |
| `STUDENT_ETHNIC_SUBGROUP_KEY` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.subject_attribute — schema stub (reference / lookup)

**URI:** `dw:subject_attribute`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/subject_attribute`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `LAST_ACTIVITY_DATE` | mnf:Varchar |  | yes |
| `SUBJECT_ATTRIBUTE_CODE` | mnf:Varchar |  | yes |
| `SUBJECT_ATTRIBUTE_DESC` | mnf:Varchar |  | yes |
| `SUBJECT_ATTRIBUTE_REPORT_DESC` | mnf:Varchar |  | yes |
| `SUBJECT_ATTRIBUTE_SHORT_DESC` | mnf:Varchar |  | yes |
| `SUBJECT_ATTRIBUTE_TYPE` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.subject_enrollable — schema stub (reference / lookup)

**URI:** `dw:subject_enrollable`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/subject_enrollable`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CLUSTER_LIST` | mnf:Varchar |  | yes |
| `MASTER_SUBJECT_ID` | mnf:Varchar |  | yes |
| `OFFER_DEPT_CODE` | mnf:Varchar |  | yes |
| `OFFER_SCHOOL_CODE` | mnf:Varchar |  | yes |
| `SUBJECT_GROUP_ID` | mnf:Varchar |  | yes |
| `SUBJECT_ID` | mnf:Varchar |  | yes |
| `SUBJECT_TITLE` | mnf:Varchar |  | yes |
| `SUBJECT_TITLE_LONG` | mnf:Varchar |  | yes |
| `TERM_CODE` | mnf:Varchar |  | yes |
| `ULT_MASTER_SUBJECT_ID` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.subject_grouping — schema stub (reference / lookup)

**URI:** `dw:subject_grouping`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/subject_grouping`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `DEPARTMENT_CODE` | mnf:Varchar |  | yes |
| `DEPARTMENT_FULL_NAME` | mnf:Varchar |  | yes |
| `DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `SCHOOL_NAME` | mnf:Varchar |  | yes |
| `SUBJECT_GROUPING_KEY` | mnf:Varchar |  | yes |
| `TERM_CODE` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.subject_iap_schedule — schema stub (reference / lookup)

**URI:** `dw:subject_iap_schedule`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/subject_iap_schedule`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `IAP_DATE` | mnf:Varchar |  | yes |
| `IAP_DAY` | mnf:Varchar |  | yes |
| `MEET_END_TIME` | mnf:Varchar |  | yes |
| `MEET_PLACE` | mnf:Varchar |  | yes |
| `MEET_START_TIME` | mnf:Varchar |  | yes |
| `REMARKS` | mnf:Varchar |  | yes |
| `SESSION_NUMBER` | mnf:Double |  | yes |
| `SUBJECT_ID` | mnf:Varchar |  | yes |
| `TERM_CODE` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.subject_summary — schema stub (reference / lookup)

**URI:** `dw:subject_summary`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/subject_summary`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CLUSTER_ENROLLMENT_1ST_CREDIT` | mnf:Double |  | yes |
| `CLUSTER_ENROLLMENT_1ST_LISTEN` | mnf:Double |  | yes |
| `CLUSTER_ENROLLMENT_5TH_CREDIT` | mnf:Double |  | yes |
| `CLUSTER_ENROLLMENT_5TH_LISTEN` | mnf:Double |  | yes |
| `CLUSTER_ENROLLMENT_CREDIT` | mnf:Double |  | yes |
| `CLUSTER_ENROLLMENT_FIFTH_WEEK` | mnf:Double |  | yes |
| `CLUSTER_ENROLLMENT_FIRST_WEEK` | mnf:Double |  | yes |
| `CLUSTER_ENROLLMENT_LISTEN` | mnf:Double |  | yes |
| `CLUSTER_ENROLLMENT_NUMBER` | mnf:Double |  | yes |
| `CLUSTER_LIST` | mnf:Varchar |  | yes |
| `CLUSTER_TYPE` | mnf:Varchar |  | yes |
| `CLUSTER_TYPE_DESC` | mnf:Varchar |  | yes |
| `DEPARTMENT_CODE` | mnf:Varchar |  | yes |
| `DEPARTMENT_NAME` | mnf:Varchar |  | yes |
| `DESIGN_UNITS` | mnf:Double |  | yes |
| `LAB_UNITS` | mnf:Double |  | yes |
| `LECTURE_UNITS` | mnf:Double |  | yes |
| `MASTER_SUBJECT_ID` | mnf:Varchar |  | yes |
| `MASTER_SUBJECT_ID_SORT` | mnf:Varchar |  | yes |
| `PREP_UNITS` | mnf:Double |  | yes |
| `SCHOOL_CODE` | mnf:Varchar |  | yes |
| `SCHOOL_NAME` | mnf:Varchar |  | yes |
| `SUBJECT_ENROLLMENT_1ST_CREDIT` | mnf:Double |  | yes |
| `SUBJECT_ENROLLMENT_1ST_LISTEN` | mnf:Double |  | yes |
| `SUBJECT_ENROLLMENT_5TH_CREDIT` | mnf:Double |  | yes |
| `SUBJECT_ENROLLMENT_5TH_LISTEN` | mnf:Double |  | yes |
| `SUBJECT_ENROLLMENT_CREDIT` | mnf:Double |  | yes |
| `SUBJECT_ENROLLMENT_FIFTH_WEEK` | mnf:Double |  | yes |
| `SUBJECT_ENROLLMENT_FIRST_WEEK` | mnf:Double |  | yes |
| `SUBJECT_ENROLLMENT_LISTEN` | mnf:Double |  | yes |
| `SUBJECT_ENROLLMENT_NUMBER` | mnf:Double |  | yes |
| `SUBJECT_GROUP_ID` | mnf:Varchar |  | yes |
| `SUBJECT_ID` | mnf:Varchar |  | yes |
| `SUBJECT_ID_SORT` | mnf:Varchar |  | yes |
| `SUBJECT_OR_CLUSTER` | mnf:Varchar |  | yes |
| `SUBJECT_SUMMARY_KEY` | mnf:Varchar |  | yes |
| `SUBJECT_TITLE` | mnf:Varchar |  | yes |
| `TERM_CODE` | mnf:Varchar |  | yes |
| `TOTAL_UNITS` | mnf:Double |  | yes |
| `ULT_MASTER_SUBJECT_ID` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.top_level_domain — schema stub (reference / lookup)

**URI:** `dw:top_level_domain`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/top_level_domain`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `TOP_LEVEL_DOMAIN` | mnf:Varchar |  | yes |
| `TOP_LEVEL_DOMAIN_DESCRIPTION` | mnf:Varchar |  | yes |
| `TOP_LEVEL_DOMAIN_KEY` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.zip_canada — schema stub (reference / lookup)

**URI:** `dw:zip_canada`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/zip_canada`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CITY_NAME` | mnf:Varchar |  | yes |
| `CITY_TYPE` | mnf:Varchar |  | yes |
| `POSTAL_CODE` | mnf:Varchar |  | yes |
| `PROVINCE_ABBR` | mnf:Varchar |  | yes |
| `PROVINCE_NAME` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |

---

## dw.zip_usa — schema stub (reference / lookup)

**URI:** `dw:zip_usa`
  
Schema stub. Awaits richer description.
  
**Row semantics:** mnf:EventRow
  
**Schema:** mnf:FixedSchema
  
**Path template:** `mysql://dw/zip_usa`

### Columns

| Name | Physical Type | Semantic Type | Nullable |
|------|---------------|---------------|----------|
| `CITY_NAME` | mnf:Varchar |  | yes |
| `CITY_TYPE` | mnf:Varchar |  | yes |
| `COUNTY_NAME` | mnf:Varchar |  | yes |
| `STATE_ABBR` | mnf:Varchar |  | yes |
| `STATE_NAME` | mnf:Varchar |  | yes |
| `WAREHOUSE_LOAD_DATE` | mnf:Varchar |  | yes |
| `ZIP_CODE` | mnf:Varchar |  | yes |
| `ZIP_TYPE` | mnf:Varchar |  | yes |

---

## Semantic Types Reference

| Type | Label | Physical Type | Range | Unit | Description |
|------|-------|---------------|-------|------|-------------|
| bvtk:JSONInString | JSON encoded as Varchar | mnf:Varchar |  |  | Open-shape JSON stored in a string column. Used by `extra` columns across keystone (`user.extra`, `trust.extra`, `service.extra`, etc.) and `credential.blob`. |
| bvtk:MySQLBoolean | MySQL tinyint(1) used as boolean | mnf:Integer |  |  | 0 = false, 1 = true. Stored as `tinyint(1)`. |
| bvtk:MySQLIdentifier | MySQL Identifier (table or column name) | mnf:Varchar |  |  | Bare unquoted identifier as it appears in MySQL DDL. |
| bvtk:OracleShortDateString | Date as Oracle short string (DD-MON-YY) | mnf:Varchar |  |  | [BVT-K-GAP-10] Date stored as varchar in `DD-MON-YY` format. Example in dw: WAREHOUSE_LOAD_DATE='19-DEC-24'. 2-digit year — ambiguous past 2049. |
| bvtk:Sha256Hex | SHA-256 Hex (64 lowercase chars) | mnf:Varchar |  |  | [BVT-K-GAP-L] Same shape as bvt:Sha256Hex from bvt_description.ttl — used here for keystone.credential.id, which is uniquely shaped this way (every other id column is 32 hex). |
| bvtk:USDateString | Date as US-format string (MM/DD/YYYY) | mnf:Varchar |  |  | [BVT-K-GAP-10] Date stored as varchar in `MM/DD/YYYY` format. Examples in dw: DATE_BUILT='07/01/1913', DATE_OCCUPIED='12/31/1916'. A query that compares this to a real date will silently return wrong results. |
| dw:AddressPurpose | Address-Purpose Code | mnf:Varchar |  |  | 13 distinct values. STREET is the physical-location address (242 of 242 buildings have one). MAIL is the mailing address (often '77 Massachusetts Ave' for central MIT delivery). E911_<n> are emergency-response addresses. PARCL<n> are property/ parcel-records addresses. DELIVERY appears once. |
| dw:BuildingNumber | MIT Building Number | mnf:Varchar |  |  | Old-school MIT building identifier. Three patterns: pure numeric ('1'–'77', main campus core, 45 buildings); compass-prefixed ('W32', 'NW17', 'E40', 114 buildings); compass- and-suffixed ('W61A', 'W85ABC', nested annexes, 68 buildings). Stored as varchar — `'2'` not `2` numerically. |
| dw:BuildingType | Building Type Code | mnf:Varchar |  |  | Three-value categorical. NB: 'RESIDENT', not 'RESIDENTIAL' — a model writing the latter returns no rows. |
| dw:BuildingUse | Building Use Code (3-4 char) | mnf:Varchar |  |  | Abbreviated codes; not human-friendly without a legend. |
| dw:CIPCode | Federal CIP Program Code (6-digit) | mnf:Varchar |  |  | US Department of Education Classification of Instructional Programs. 6-digit string. Editions: 1990, 2000, 2010, 2020. |
| dw:CampusSector | Campus Sector | mnf:Varchar |  |  | Eight values; note 'WESTWEST' (not 'WEST WEST') and 'OFFCAMPUS' (not 'OFF CAMPUS'). |
| dw:CommaListString | Comma-separated list in a varchar | mnf:Varchar |  |  | [BVT-K-GAP-21] Varchar containing a comma-separated list (often comma-space). Used by space_supervisor_usage. DEPT_NAMES, subject_offered.CLUSTER_LIST, course_catalog.JOINT_SUBJECTS, etc. Splitting needs SUBSTRING_INDEX or string-array unnesting. |
| dw:CourseLevel | Course Level | mnf:Varchar |  |  | G = Graduate, U = Undergraduate. |
| dw:DLCKey | DLC Key (Department/Lab/Center) | mnf:Varchar |  |  | Always 'D_<UPPERCASE>'. Real institutional codes (D_HISTORY, D_CSAIL, D_PHYSICS, D_DOF). DLC_KEY = DLC_CODE in master_dept_hierarchy. A few oddities: D_BF&T (ampersand), D_PROVOST_AREA (more a hierarchy marker), D_OBSOLETE / D_UNDEF_DEFUNCT (catch-all buckets). |
| dw:GIRAttribute | General Institute Requirement Attribute | mnf:Varchar |  |  | REST (Rest Elec in Sci & Tech), LAB (Institute Lab), CHEM, CAL1, CAL2, BIOL, PHY1, PHY2, plus the older HD1-HD5 for pre-Fall-2010 students. |
| dw:HASSAttribute | HASS / GIR Attribute Code | mnf:Varchar |  |  | Distribution-requirement codes. 17 values across post-2010 HASS_ATTRIBUTE (HE, HS, HA, HH, etc.) and pre-2010 GIR_ATTRIBUTE (HD1-HD5, HDL). Some codes (e.g. 'HE') appear in BOTH systems. Comma-list values like 'HA,HH' are also valid for cross-attributed subjects. |
| dw:HGNCode | Hierarchical Group Number (graduate-credit classification) | mnf:Varchar |  |  | G = Graduate program, H = Higher-level graduate, N = Not for graduate credit. Sometimes 'U' (Undergraduate) appears in cis_course_catalog. |
| dw:KrbName | Kerberos / Athena Username | mnf:Varchar |  |  | [BVT-K-GAP-25] 2-9 char username. Casing inconsistent across tables: lowercase in employee_directory, moira_list_detail, roles_fin_pa; UPPERCASE in person_auth_area.USER_NAME. Joins need UPPER() or LOWER() normalisation. |
| dw:MITID_NamespaceA | MIT_ID — Namespace A (employee_directory etc.) | mnf:Varchar |  |  | 9-digit anonymised MIT identifier. Namespace A appears in: employee_directory, drupal_employee_directory, subject_offered.RESPONSIBLE_FACULTY_MIT_ID, subject_offered_summary.RESPONSIBLE_FACULTY_MIT_ID, moira_list_detail.MOIRA_LIST_MEMBER_MIT_ID, space_supervisor_usage.MIT_ID. Do NOT join to Namespace B — returns 0 rows. |
| dw:MITID_NamespaceB | MIT_ID — Namespace B (se_person etc.) | mnf:Varchar |  |  | 9-digit anonymised MIT identifier, DISJOINT from Namespace A. Appears in: se_person, hr_faculty_roster, warehouse_users. Cross-walk to Namespace A only via KRB_NAME or FULL_NAME. |
| dw:MajorUseDesc | Major Use Description (8-char abbreviation) | mnf:Varchar |  |  | Room categorisation codes from fclt_major_use. NB: codes are 8-char abbreviations, NOT human-friendly. Filtering on 'Office' or 'Classroom' returns 0 rows; use 'OFFICES' / 'CLASSRMS'. |
| dw:OracleDateString | Date as Oracle DD-MON-YY string | mnf:Varchar |  |  | [BVT-K-GAP-10] Same shape as bvtk:OracleShortDateString. Used by TERM_START_DATE, WAREHOUSE_LOAD_DATE, HOLIDAY_CLOSING_DATE, SESSION_DATE (IAP), LAST_ACTIVITY_DATE, etc. Parse via STR_TO_DATE(col, '%d-%b-%y'). |
| dw:OwnerType | Moira Owner Type | mnf:Varchar |  |  | 4 distinct values. Concatenated as a prefix to OWNER name in MOIRA_LIST_OWNER_KEY (no delimiter — see BVT-K-GAP-29). |
| dw:OwnershipType | Building Ownership | mnf:Varchar |  |  |  |
| dw:SchoolCode | MIT School Code (single letter) | mnf:Varchar |  |  | Single-letter school code. A=Architecture+Planning, E=Engineering, H=HASS, M=Sloan/Mgmt, S=Science, W=Schwarzman College of Computing, T=Whitaker/HST, Y=MIT-academic-other, X=MIT-non-academic, Z=Non-MIT. |
| dw:SentinelTermCode | TERM_CODE with '000000' / '999999' sentinels | mnf:Varchar |  |  | [BVT-K-GAP-5] Most TERM_CODE columns hold <YEAR><SEASON> values, but FROM_TERM and THRU_TERM in sis_course_description and student_degree_program use '000000' (Beginning of Time) and '999999' (End of Time) sentinel strings. The companion *_DESCRIPTION columns spell these out literally. |
| dw:Site | MIT Site Code | mnf:Varchar |  |  | Site code identifying the campus location. The main MIT campus is 'MIT'; satellite sites have other codes (Lincoln Lab, Bates, etc.). |
| dw:SubjectId | MIT Subject ID | mnf:Varchar |  |  | Format <COURSE>.<NUMBER>. Course codes can be numeric ('6', '12') or alphabetic ('EC', 'HAA', 'STS', 'PE'). Subject numbers can have letter prefixes ('UR' Undergraduate Research, 'S' Special). Examples: '6.147', '12.UR', 'HAA.6824'. The dot is part of the identifier; LIKE '6.%' overmatches. |
| dw:TermCode | Academic Term Code | mnf:Varchar |  |  | Format <YEAR><SEASON_2CHAR>. Seasons: FA (Fall), JA (January/IAP), SP (Spring), SU (Summer). 133 distinct values in subject_offered ranging '1986FA' through '2025SP'. Used by subject_offered, library_subject_offered, tip_subject_offered, academic_terms_all, etc. Don't do arithmetic on this — convert via academic_terms_all. |
| dw:USPostalCodeStripped | US Postal Code, leading-zero stripped | mnf:Varchar |  |  | [BVT-K-GAP-10] varchar storing the postal code with leading zeros REMOVED. Cambridge MA 02139 is stored as '2139'. Joining to zip_usa.ZIP_CODE requires zero-padding back. |
| dw:YNFlag | 'Y'/'N' string flag | mnf:Varchar |  |  | Single-char string boolean used pervasively in dw. Values are LITERAL 'Y' and 'N' strings, not booleans. Filtering on `= 1` or `= TRUE` returns 0 rows. |
| ks:AnonymisedName | Anonymised Name (synthetic word-pair) | mnf:Varchar |  |  | Synthetic name pattern `word_word.numword` (e.g. `prime_helix.306sonic`, `blaze_orbit_glyph`). Used by local_user.name, role.name, project.name, group.name. Length cluster 17–22 chars. |
| ks:AnonymisedPassword | Anonymised Password | mnf:Varchar |  |  | Pattern `replaced_password.<n>` where n is local_user_id. NOT a hash, NOT a real credential — anonymisation artefact only. |
| ks:AssignmentType | Assignment Polymorphic Type | mnf:Varchar |  |  | Discriminator for the polymorphic FKs in `assignment(actor_id, target_id)`. Determines which target table actor_id and target_id reference. See ks:fk_assignment_*. |
| ks:CredentialType | Credential Type | mnf:Varchar |  |  | In this dump, only 'ec2' appears. Other keystone deployments may use 'cert', 'totp', 'application_credential'. |
| ks:DomainId | Keystone Domain ID | mnf:Varchar |  |  | Either a 32-char hex UUID, the literal 'default' sentinel, or '<<keystone.domain.root>>'. See [BVT-K-GAP-5]. |
| ks:EndpointInterface | Endpoint Interface Tier | mnf:Varchar |  |  | Three-tier visibility: public/internal/admin. |
| ks:GroupId | Keystone Group ID | mnf:Varchar |  |  | 32-char hex UUID, PK of `group` (note: reserved word — see [BVT-K-GAP-7]). |
| ks:LocalUserSurrogateId | Local-User Surrogate ID | mnf:Integer |  |  | Auto-increment integer PK of `local_user`. NB: this is NOT the same as ks:UserId. The chain is: user.id (varchar, hex) → local_user.user_id (varchar, hex, FK) local_user.id (int) ← password.local_user_id (int, FK) Joining password directly to user.id will fail. |
| ks:ProjectId | Keystone Project ID | mnf:Varchar |  |  | 32-char hex UUID, plus 3 sentinel rows: 'default', '<<keystone.domain.root>>', and one per Heat domain. See ks:domain_project_duality for the cross-table identity. |
| ks:RegionId | Keystone Region ID (NOT a UUID) | mnf:Varchar |  |  | `region.id` is the human-readable name itself, not a generated id. Closed set in this dump: 'CSAIL_Stata', 'MOC_Kaizen'. |
| ks:RoleId | Keystone Role ID | mnf:Varchar |  |  |  |
| ks:ServiceType | OpenStack Service Type | mnf:Varchar |  |  | Real-name OpenStack service type (NOT anonymised) — the canonical lookup key clients use. Set is closed by OpenStack convention. |
| ks:UserId | Keystone User ID | mnf:Varchar |  |  | 32-char lowercase hex UUID, primary key of `user`. |

## Cross-Dataset Relationships

### Foreign Keys

| Relationship | From (Dataset.Column) | To (Dataset.Column) | Integrity |
|-------------|----------------------|---------------------|-----------|
| local_user.user_id → user.id (declared, UNIQUE) | keystone.local_user — local-identity specialisation.`user_id` | keystone.user — abstract user identity.`id` | mnf:StrictIntegrity |
| federated_user.user_id → user.id (declared) | keystone.federated_user — federated-identity specialisation (EMPTY).`user_id` | keystone.user — abstract user identity.`id` | mnf:StrictIntegrity |
| password.local_user_id → local_user.id (declared) | keystone.password — credentials (heavily anonymised).`local_user_id` | keystone.local_user — local-identity specialisation.`id` | mnf:StrictIntegrity |
| user_group_membership.user_id → user.id (declared) | keystone.user_group_membership — group memberships.`user_id` | keystone.user — abstract user identity.`id` | mnf:StrictIntegrity |
| user_group_membership.group_id → group.id (declared) | keystone.user_group_membership — group memberships.`group_id` | keystone.group — identity groups (MySQL RESERVED WORD).`id` | mnf:StrictIntegrity |
| endpoint.service_id → service.id (declared) | keystone.endpoint — service URL bindings per region.`service_id` | keystone.service — OpenStack service catalogue.`id` | mnf:StrictIntegrity |
| endpoint.region_id → region.id (declared) | keystone.endpoint — service URL bindings per region.`region_id` | keystone.region — endpoint geographic grouping.`id` | mnf:StrictIntegrity |
| project.domain_id → project.id (self-FK; declared) | keystone.project — tenants (and domains, see duality).`domain_id` | keystone.project — tenants (and domains, see duality).`id` | mnf:StrictIntegrity |
| project.parent_id → project.id (self-FK; declared) | keystone.project — tenants (and domains, see duality).`parent_id` | keystone.project — tenants (and domains, see duality).`id` | mnf:StrictIntegrity |
| user.default_project_id → project.id (SOFT, BROKEN) | keystone.user — abstract user identity.`default_project_id` | keystone.project — tenants (and domains, see duality).`id` | mnf:PartialIntegrity |
| assignment.role_id → role.id (SOFT) | keystone.assignment — authorisation edges (polymorphic).`role_id` | keystone.role — named roles.`id` | mnf:StrictIntegrity |
| assignment.actor_id → user.id (when type LIKE 'User%') — POLYMORPHIC SOFT | keystone.assignment — authorisation edges (polymorphic).`actor_id` | keystone.user — abstract user identity.`id` | mnf:StrictIntegrity |
| assignment.actor_id → group.id (when type LIKE 'Group%') — POLYMORPHIC SOFT | keystone.assignment — authorisation edges (polymorphic).`actor_id` | keystone.group — identity groups (MySQL RESERVED WORD).`id` | mnf:StrictIntegrity |
| assignment.target_id → project.id (when type LIKE '%Project') — POLYMORPHIC SOFT | keystone.assignment — authorisation edges (polymorphic).`target_id` | keystone.project — tenants (and domains, see duality).`id` | mnf:StrictIntegrity |
| assignment.target_id → domain.id (when type LIKE '%Domain') — POLYMORPHIC SOFT | keystone.assignment — authorisation edges (polymorphic).`target_id` | keystone.domain — top-level identity containers (domain-as-project duality).`id` | mnf:StrictIntegrity |
| credential.user_id → user.id (SOFT, partial) | keystone.credential — additional credentials (EC2 only here).`user_id` | keystone.user — abstract user identity.`id` | mnf:PartialIntegrity |
| credential.project_id → project.id (SOFT) | keystone.credential — additional credentials (EC2 only here).`project_id` | keystone.project — tenants (and domains, see duality).`id` | mnf:PartialIntegrity |
| trust.trustor_user_id → user.id (SOFT) | keystone.trust — time-bounded role delegations.`trustor_user_id` | keystone.user — abstract user identity.`id` | mnf:StrictIntegrity |
| trust.trustee_user_id → user.id (SOFT) | keystone.trust — time-bounded role delegations.`trustee_user_id` | keystone.user — abstract user identity.`id` | mnf:StrictIntegrity |
| trust.project_id → project.id (SOFT, partial) | keystone.trust — time-bounded role delegations.`project_id` | keystone.project — tenants (and domains, see duality).`id` | mnf:PartialIntegrity |
| trust_role.trust_id → trust.id (SOFT) | keystone.trust_role — roles granted within a trust.`trust_id` | keystone.trust — time-bounded role delegations.`id` | mnf:StrictIntegrity |
| trust_role.role_id → role.id (SOFT) | keystone.trust_role — roles granted within a trust.`role_id` | keystone.role — named roles.`id` | mnf:StrictIntegrity |
| subject_offered.RESPONSIBLE_FACULTY_MIT_ID → employee_directory.MIT_ID (Namespace A) | dw.subject_offered — subject sections per term.`RESPONSIBLE_FACULTY_MIT_ID` | dw.employee_directory — MIT phonebook (Namespace A).`MIT_ID` | mnf:PartialIntegrity |
| subject_offered_summary.RESPONSIBLE_FACULTY_MIT_ID → employee_directory.MIT_ID | dw.subject_offered_summary — per-(subject, term) summary.`RESPONSIBLE_FACULTY_MIT_ID` | dw.employee_directory — MIT phonebook (Namespace A).`MIT_ID` | mnf:PartialIntegrity |
| moira_list_detail.MEMBER_MIT_ID → employee_directory.MIT_ID (Namespace A) | dw.moira_list_detail — list memberships (one (list, member) per row).`MOIRA_LIST_MEMBER_MIT_ID` | dw.employee_directory — MIT phonebook (Namespace A).`MIT_ID` | mnf:PartialIntegrity |
| moira_list_detail.OWNER_KEY → moira_list_owner.OWNER_KEY (clean — no orphans) | dw.moira_list_detail — list memberships (one (list, member) per row).`MOIRA_LIST_OWNER_KEY` | dw.moira_list_owner — owner identity catalogue (NOT keyed by list).`MOIRA_LIST_OWNER_KEY` | mnf:StrictIntegrity |
| moira_list_detail.LIST_KEY → moira_list.LIST_KEY (PARTIAL — orphans both ways) | dw.moira_list_detail — list memberships (one (list, member) per row).`MOIRA_LIST_KEY` | dw.moira_list — Moira mailing-list catalogue (with DUPLICATES).`MOIRA_LIST_KEY` | mnf:PartialIntegrity |
| sis_department.DLC_KEY → master_dept_hierarchy.DLC_KEY | dw.sis_department — academic-side department catalogue.`DLC_KEY` | dw.master_dept_hierarchy — DLC org tree (5-level path).`DLC_KEY` | mnf:StrictIntegrity |
| fclt_org_dlc_key.DLC_KEY → master_dept_hierarchy.DLC_KEY | dw.fclt_org_dlc_key — explicit FCLT_ORGANIZATION_KEY ↔ DLC_KEY bridge.`DLC_KEY` | dw.master_dept_hierarchy — DLC org tree (5-level path).`DLC_KEY` | mnf:StrictIntegrity |
| fclt_org_dlc_key.FCLT_ORGANIZATION_KEY → fclt_organization.FCLT_ORGANIZATION_KEY | dw.fclt_org_dlc_key — explicit FCLT_ORGANIZATION_KEY ↔ DLC_KEY bridge.`FCLT_ORGANIZATION_KEY` | dw.fclt_organization — facilities org table (DLC-aware).`FCLT_ORGANIZATION_KEY` | mnf:StrictIntegrity |
| subject_offered.TERM_CODE → academic_terms_all.TERM_CODE | dw.subject_offered — subject sections per term.`TERM_CODE` | dw.academic_terms_all — canonical term catalogue (300 rows, 1951-2030).`TERM_CODE` | mnf:StrictIntegrity |
| iap_subject_detail.TERM_CODE → academic_terms_all.TERM_CODE | dw.iap_subject_detail — IAP activity registry (2021JA snapshot only).`TERM_CODE` | dw.academic_terms_all — canonical term catalogue (300 rows, 1951-2030).`TERM_CODE` | mnf:StrictIntegrity |
| academic_terms.TERM_CODE → academic_terms_all.TERM_CODE (subset) | dw.academic_terms — current-relevant term subset (144 rows).`TERM_CODE` | dw.academic_terms_all — canonical term catalogue (300 rows, 1951-2030).`TERM_CODE` | mnf:StrictIntegrity |
| person_auth_area.USER_NAME → employee_directory.KRB_NAME_UPPERCASE | dw.person_auth_area — auth flags by KRB_NAME (UPPERCASE).`USER_NAME` | dw.employee_directory — MIT phonebook (Namespace A).`KRB_NAME_UPPERCASE` | mnf:PartialIntegrity |

### Same Entity

| Identity | Dataset | Column |
|----------|---------|--------|
| Domain identity is also a project (where is_domain=1) | keystone.domain — top-level identity containers (domain-as-project duality) | `id` |
| Domain identity is also a project (where is_domain=1) | keystone.project — tenants (and domains, see duality) | `id` |
| user → local_user / federated_user (1:1, mutually exclusive) | keystone.user — abstract user identity | `id` |
| user → local_user / federated_user (1:1, mutually exclusive) | keystone.local_user — local-identity specialisation | `user_id` |
| user → local_user / federated_user (1:1, mutually exclusive) | keystone.federated_user — federated-identity specialisation (EMPTY) | `user_id` |
| BUILDING_NUMBER ≡ BUILDING_KEY ≡ FAC_BUILDING_KEY ≡ FCLT_BUILDING_KEY | dw.buildings — addressable buildings (simple shape) | `BUILDING_KEY` |
| BUILDING_NUMBER ≡ BUILDING_KEY ≡ FAC_BUILDING_KEY ≡ FCLT_BUILDING_KEY | dw.fac_building — buildings with rich attributes (FAC_-keyed) | `FAC_BUILDING_KEY` |
| BUILDING_NUMBER ≡ BUILDING_KEY ≡ FAC_BUILDING_KEY ≡ FCLT_BUILDING_KEY | dw.fac_building — buildings with rich attributes (FAC_-keyed) | `BUILDING_NUMBER` |
| BUILDING_NUMBER ≡ BUILDING_KEY ≡ FAC_BUILDING_KEY ≡ FCLT_BUILDING_KEY | dw.fclt_building — buildings with rich attributes (FCLT_-keyed) | `FCLT_BUILDING_KEY` |
| BUILDING_NUMBER ≡ BUILDING_KEY ≡ FAC_BUILDING_KEY ≡ FCLT_BUILDING_KEY | dw.fclt_building — buildings with rich attributes (FCLT_-keyed) | `BUILDING_NUMBER` |
| BUILDING_NUMBER ≡ BUILDING_KEY ≡ FAC_BUILDING_KEY ≡ FCLT_BUILDING_KEY | dw.fac_rooms — room inventory (granular, includes service spaces) | `BUILDING_KEY` |
| BUILDING_NUMBER ≡ BUILDING_KEY ≡ FAC_BUILDING_KEY ≡ FCLT_BUILDING_KEY | dw.fclt_rooms — curated room inventory (FCLT-keyed) | `FCLT_BUILDING_KEY` |
| BUILDING_NUMBER ≡ BUILDING_KEY ≡ FAC_BUILDING_KEY ≡ FCLT_BUILDING_KEY | dw.space_detail — leaner space inventory (third representation) | `BUILDING_KEY` |
| BUILDING_NUMBER ≡ BUILDING_KEY ≡ FAC_BUILDING_KEY ≡ FCLT_BUILDING_KEY | dw.fclt_building_address — addresses by purpose (FCLT-keyed) | `FCLT_BUILDING_KEY` |
| DLC_KEY identifies the same DLC across all dw tables | dw.master_dept_hierarchy — DLC org tree (5-level path) | `DLC_KEY` |
| DLC_KEY identifies the same DLC across all dw tables | dw.master_dept_hierarchy — DLC org tree (5-level path) | `DLC_CODE` |
| DLC_KEY identifies the same DLC across all dw tables | dw.master_dept_hierarchy_links — DLC↔external-system cross-refs | `DLC_KEY` |
| DLC_KEY identifies the same DLC across all dw tables | dw.master_dept_dcode_parent — adjacency-list parent pointers | `D_CODE` |
| DLC_KEY identifies the same DLC across all dw tables | dw.sis_department — academic-side department catalogue | `DLC_KEY` |
| DLC_KEY identifies the same DLC across all dw tables | dw.fclt_organization — facilities org table (DLC-aware) | `DLC_KEY` |
| DLC_KEY identifies the same DLC across all dw tables | dw.fac_organization — facilities org table (D_CODE-style) | `D_CODE` |
| DLC_KEY identifies the same DLC across all dw tables | dw.fclt_org_dlc_key — explicit FCLT_ORGANIZATION_KEY ↔ DLC_KEY bridge | `DLC_KEY` |
| DLC_KEY identifies the same DLC across all dw tables | dw.hr_org_unit — HR org units (older system) | `DLC_KEY` |
| DLC_KEY identifies the same DLC across all dw tables | dw.hr_org_unit_new — HR org units (current; superset) | `DLC_KEY` |
| DLC_KEY identifies the same DLC across all dw tables | dw.roles_fin_pa — financial-PA roles by user (lowercase KRB) | `DLC_KEY` |
| DLC_KEY identifies the same DLC across all dw tables | dw.space_unit — DLC mapping (proper-case names) | `DLC_KEY` |
| DLC_KEY identifies the same DLC across all dw tables | dw.space_unit2 — DLC mapping (uppercase abbreviated) | `DLC_KEY` |
| TERM_CODE identifies the same academic term across dw tables | dw.academic_terms_all — canonical term catalogue (300 rows, 1951-2030) | `TERM_CODE` |
| TERM_CODE identifies the same academic term across dw tables | dw.academic_terms — current-relevant term subset (144 rows) | `TERM_CODE` |
| TERM_CODE identifies the same academic term across dw tables | dw.academic_term_parameter — pointer to current/previous/upcoming terms | `TERM_CODE` |
| TERM_CODE identifies the same academic term across dw tables | dw.subject_offered — subject sections per term | `TERM_CODE` |
| TERM_CODE identifies the same academic term across dw tables | dw.subject_offered_summary — per-(subject, term) summary | `TERM_CODE` |
| TERM_CODE identifies the same academic term across dw tables | dw.iap_subject_detail — IAP activity registry (2021JA snapshot only) | `TERM_CODE` |
| TERM_CODE identifies the same academic term across dw tables | dw.library_subject_offered — library's per-(subject, term) view (2009-2021) | `TERM_CODE` |
| TERM_CODE identifies the same academic term across dw tables | dw.library_reserve_matrl_detail — pure linkage table (5 keys per row) | `TERM_CODE` |
| TERM_CODE identifies the same academic term across dw tables | dw.tip_subject_offered — TIP per-(subject, term) (2024+ only) | `TERM_CODE` |
| TERM_CODE identifies the same academic term across dw tables | dw.tip_detail — TIP join table | `TERM_CODE` |
| TERM_CODE identifies the same academic term across dw tables | dw.time_day — daily fact table with fiscal/calendar/academic context | `ACADEMIC_TERM_CODE` |
| MIT_ID Namespace A — joinable across these columns | dw.employee_directory — MIT phonebook (Namespace A) | `MIT_ID` |
| MIT_ID Namespace A — joinable across these columns | dw.drupal_employee_directory — Drupal-published mirror | `MIT_ID` |
| MIT_ID Namespace A — joinable across these columns | dw.subject_offered — subject sections per term | `RESPONSIBLE_FACULTY_MIT_ID` |
| MIT_ID Namespace A — joinable across these columns | dw.subject_offered_summary — per-(subject, term) summary | `RESPONSIBLE_FACULTY_MIT_ID` |
| MIT_ID Namespace A — joinable across these columns | dw.course_catalog_subject_offered — recent year-scoped catalogue | `RESPONSIBLE_FACULTY_MIT_ID` |
| MIT_ID Namespace A — joinable across these columns | dw.library_subject_offered — library's per-(subject, term) view (2009-2021) | `RESPONSIBLE_FACULTY_MIT_ID` |
| MIT_ID Namespace A — joinable across these columns | dw.moira_list_detail — list memberships (one (list, member) per row) | `MOIRA_LIST_MEMBER_MIT_ID` |
| MIT_ID Namespace A — joinable across these columns | dw.space_supervisor_usage — pre-aggregated per-supervisor metrics | `MIT_ID` |
| MIT_ID Namespace B — joinable across these columns (DISJOINT from Namespace A) | dw.se_person — payroll-flavoured people (Namespace B) | `MIT_ID` |
| MIT_ID Namespace B — joinable across these columns (DISJOINT from Namespace A) | dw.hr_faculty_roster — faculty-only HR view (Namespace B) | `MIT_ID` |
| MIT_ID Namespace B — joinable across these columns (DISJOINT from Namespace A) | dw.warehouse_users — staff + students union (Namespace B) | `MIT_ID` |
| KRB_NAME identifies the same person across namespaces (case varies) | dw.employee_directory — MIT phonebook (Namespace A) | `KRB_NAME` |
| KRB_NAME identifies the same person across namespaces (case varies) | dw.employee_directory — MIT phonebook (Namespace A) | `KRB_NAME_UPPERCASE` |
| KRB_NAME identifies the same person across namespaces (case varies) | dw.se_person — payroll-flavoured people (Namespace B) | `KRB_NAME` |
| KRB_NAME identifies the same person across namespaces (case varies) | dw.warehouse_users — staff + students union (Namespace B) | `KRB_NAME` |
| KRB_NAME identifies the same person across namespaces (case varies) | dw.moira_list_detail — list memberships (one (list, member) per row) | `MOIRA_LIST_MEMBER` |
| KRB_NAME identifies the same person across namespaces (case varies) | dw.person_auth_area — auth flags by KRB_NAME (UPPERCASE) | `USER_NAME` |
| KRB_NAME identifies the same person across namespaces (case varies) | dw.roles_fin_pa — financial-PA roles by user (lowercase KRB) | `USERNAME` |
| SUBJECT_ID identifies the same MIT subject across dw tables | dw.subject_offered — subject sections per term | `SUBJECT_ID` |
| SUBJECT_ID identifies the same MIT subject across dw tables | dw.subject_offered_summary — per-(subject, term) summary | `SUBJECT_ID` |
| SUBJECT_ID identifies the same MIT subject across dw tables | dw.course_catalog_subject_offered — recent year-scoped catalogue | `SUBJECT_ID` |
| SUBJECT_ID identifies the same MIT subject across dw tables | dw.cis_course_catalog — older CIS course catalogue | `SUBJECT_ID` |
| SUBJECT_ID identifies the same MIT subject across dw tables | dw.library_subject_offered — library's per-(subject, term) view (2009-2021) | `SUBJECT_ID` |
| SUBJECT_ID identifies the same MIT subject across dw tables | dw.library_course_instructor — instructor↔course assignments | `SUBJECT_ID` |
| SUBJECT_ID identifies the same MIT subject across dw tables | dw.library_reserve_matrl_detail — pure linkage table (5 keys per row) | `SUBJECT_ID` |
| SUBJECT_ID identifies the same MIT subject across dw tables | dw.tip_subject_offered — TIP per-(subject, term) (2024+ only) | `SUBJECT_ID` |
| SUBJECT_ID identifies the same MIT subject across dw tables | dw.tip_detail — TIP join table | `SUBJECT_ID` |

---

## Notes for AI Agents

This section explains Manifest concepts used in the tables above, to help you write correct queries against this data.

**Row semantics** determine how to interpret rows:

- **Event rows** (`mnf:EventRow`) — each row is an independent event or observation. No deduplication needed.
- **Aggregate rows** (`mnf:AggregateRow`) — each row summarises a group of source rows. Check the Aggregation table for how columns relate to the source dataset.

**Entity key** — the column that identifies which entity a snapshot row describes. Within a single release, each entity key value should be unique. Across releases, the same entity appears in each snapshot.

**Schema stability** affects query robustness:

- **Fixed** (`mnf:FixedSchema`) — all files have identical columns and types. Query without defensive casting.

**Foreign keys** — the From and To columns are joinable across datasets, even when column names differ. Check the Integrity column: `mnf:PartialIntegrity` means some values may not resolve in the target (use LEFT JOIN rather than INNER JOIN if you need all rows).

**Same entity** — these columns across different datasets refer to the same real-world entity and are joinable. Unlike foreign keys, same-entity is symmetric — neither side is the "reference" table.

**Known deficiencies** — documented data quality issues that may affect query correctness. Read these before writing queries that involve aggregation, deduplication, or cross-file joins.

**Notation** — `mnf:` prefixed terms are Manifest vocabulary concepts. Domain-specific prefixes (e.g. `ais:`, `pm:`) identify semantic types and domain entities. Physical types like `mnf:Varchar`, `mnf:Double`, `mnf:Integer` map directly to DuckDB/Parquet types.

