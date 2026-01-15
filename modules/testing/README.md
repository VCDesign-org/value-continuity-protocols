# VCDesign Testing Module

This module provides a minimal, practical bridge from VCDesign design outputs to executable tests.

## What’s inside
- `schemas/`: VCDesign Test Pack schema (format contract)
- `examples/`: sample packs + OpenAPI + executable tests
- `runners/`: runnable environments (pytest, etc.)

## Design principle
This module intentionally constrains only:
- external contracts (OpenAPI shape)
- observable invariants (properties)

It does NOT constrain:
- database schema
- internal architecture
- implementation language/framework

## Quick start (Python runner)
```bash
cd modules/testing/examples/maintenance_ticket/runners/python-pytest
pip install -r requirements.txt
export BASE_URL=http://localhost:8080
pytest -q
When to extend
Add fields to API only when you need to make "stop/defer" observable.

Keep internal workflows (approval, escalation) out of OpenAPI unless truly required.

yaml
コードをコピーする

---

## 4) prompts は「あなたの狙い」に合わせて命名済みでOK
案Aで行くなら、promptsはこの3枚で固定が強いです。

- `vcdesign_bootstrap.prompt.md`（無料版対策：1手順起動）
- `vcdesign_to_testpack.prompt.md`（設計→Packの“厳格変換”）
- `testpack_to_tests.prompt.md`（Pack→テスト生成）

※ 中身は、すでにこのスレッドで作ったものを貼ればOKです。

---

## 5) schema ファイルは “YAMLスキーマ” を置く（最初はコメント中心で十分）
最初は「機械で検証するSchema」より、**人とAIが崩さないための“枠”**が大事なので、
`schemas/vcdesign_test_pack.schema.yaml` は v0.1 をコメント化しておくのが現実的です。

（厳密なJSON Schema化は後でOK）

例：

```yaml
# VCDesign Test Pack Schema (v0.1)
# This is a format contract for exchanging design intent with tools/AI.
# Keep this stable. Introduce changes via versioning.

vcdesign_test_pack:
  meta: { name: "", system_under_test: "", version: "", created_at: "", author: "" }
  value_definition: { primary_value: "", success_criteria: [], unacceptable_outcomes: [] }
  boundaries:
    forbidden: [{ id: "", description: "", reason: "" }]
    stop_conditions: [{ condition: "", action: "stop_and_defer_to_human" }]
    optimization_allowed: [{ description: "" }]
  responsibility: { decision_owner: "", escalation_target: "", approval_required: true }
  contracts:
    api: [{ name: "", type: "openapi|graphql|asyncapi", source: "", critical_endpoints: [] }]
  intents: { bdd_scenarios: [{ id: "", given: "", when: "", then: "", notes: "" }] }
  environment_model:
    assumptions: []
    external_dependencies: [{ name: "", behavior: "" }]
    non_determinism: [{ source: "", handling: "" }]
  properties: { safety_properties: [], liveness_properties: [], defer_properties: [] }
  telemetry:
    signals: [{ name: "", meaning: "" }]
    regression_candidates: [{ from_signal: "", test_focus: "" }]