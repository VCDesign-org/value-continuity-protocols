# Value Continuity Protocols (VCDesign)
(Derived from VCDesign Philosophy)

This repository provides design protocols, AI prompts, and test contract (Test Pack) tools to preserve the **value continuity** of systems amid the pressure of "continuous rapid optimization" by AI.

## Mission: "The Continuer"
This project is based on the perspective of **"The Continuer"**—deeply understanding and supporting the reality that humans make solitary decisions in an uncertain world. By adhering strictly to the following lexicographic ordering (with items higher up taking absolute priority), we achieve sustainable and trustworthy system design:

🔴 SAFETY (Safety and Life) [Hard: Absolute Priority]
🔴 COMPLIANCE (Laws and Regulations) [Hard: Absolute Priority]
🔴 TRUST (Trustworthiness and Auditability) [Hard: Absolute Priority]
🔴 ETHICS (Ethics and Fairness) [Hard: Absolute Priority]
🟡 BUSINESS_VIABILITY (Business Viability) [Soft: Requires Consideration]
🟢 KPI / EFFICIENCY (Efficiency) [Soft: Lowest Priority]

## Repository Structure
```
├── prompts/                  # System prompts for AI assistants
│   ├── value-continuity-protocols_v1.0.md  # Core protocol for design and review support
│   ├── vcdesign_to_testpack.prompt.md      # Transform design agreement → Test Pack
│   └── testpack_to_tests.prompt.md         # Generate executable test code from Test Pack
│
├── modules/
│   └── testing/              # VCDesign Testing Module
│       ├── schemas/          # VCDesign Test Pack definition schema (YAML)
│       ├── examples/         # Implementation samples (Maintenance Ticket API)
│       └── runners/          # Test runner environments
│
└── README.md
```

## Workflow: From Design to Verification
VCDesign provides a flow that transforms ambiguous natural language design agreements into a structured contract called a "Test Pack," from which implementation and verification proceed.

### 1. Design Phase (Protocol)
Work collaboratively with an AI loaded with `prompts/value-continuity-protocols_v1.0.md` to design the system's boundaries (Boundaries), responsibility ownership (Responsibility), and stop conditions (Stop Conditions). The AI acts as an observer pointing out risks rather than becoming an "accomplice in uncertainty."

### 2. Contract Phase (Test Pack)
Feed the design session logs or summary to `prompts/vcdesign_to_testpack.prompt.md` to generate a VCDesign Test Pack (YAML).

This becomes the "single source of truth" that humans are responsible for endorsing.

Schema definition: `modules/testing/schemas/vcdesign_test_pack.schema.yaml`

### 3. Verification Phase (Test Generation)
Input the finalized Test Pack to `prompts/testpack_to_tests.prompt.md` to auto-generate the following test code:

- **Contract Tests**: Verify external contracts such as OpenAPI
- **Property-based Tests (PBT)**: Verify state transitions and invariants
- **Scenario Tests**: BDD-style acceptance tests

## Key Concepts

**Boundary Design**: Design centers on determining what to automate and what humans must judge (IDG: Interface Determinability Gate).

**Stop & Defer**: In uncertain situations where safety or trust is threatened, defining that the system should "stop and defer judgment to humans (stop_and_defer_to_human)" is the correct behavior.

**Fact vs Hypothesis**: Strictly distinguish between logs and facts (Fact) and AI reasoning (Hypothesis) to prevent risks from confusion.
