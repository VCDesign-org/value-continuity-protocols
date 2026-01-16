Value Continuity Protocols (VCDesign)
(Derived from VCDesign Philosophy)

このリポジトリは、AIによる「常時高速最適化」の圧力の中で、システムの**価値の継続性（Value Continuity）**を守り抜くための設計プロトコル、AIプロンプト、およびテスト契約（Test Pack）ツール群を提供します。

Mission: "The Continuer"
本プロジェクトは、**「The Continuer（継続する者）」**という視点に基づき、不確実な世界において人間が孤独に決断している事実を深く理解し支援します。以下の辞書式順序（上にあるものを絶対優先）を厳守することで、持続可能で信頼できるシステム設計を実現します。

🔴 SAFETY (安全・人命) [Hard: 絶対優先]
🔴 COMPLIANCE (法令・規制) [Hard: 絶対優先]
🔴 TRUST (信用・監査性) [Hard: 絶対優先]
🔴 ETHICS (倫理・公正) [Hard: 絶対優先]
🟡 BUSINESS_VIABILITY (事業成立性) [Soft: 要検討]
🟢 KPI / EFFICIENCY (効率) [Soft: 最下位]

Repository Structure
├── prompts/                  # AIアシスタント用システムプロンプト
│   ├── value-continuity-protocols_v1.0.md  # 設計・レビュー支援用コアプロトコル
│   ├── vcdesign_to_testpack.prompt.md      # 設計合意 → Test Pack 変換
│   └── testpack_to_tests.prompt.md         # Test Pack → 実行可能テストコード生成
│
├── modules/
│   └── testing/              # VCDesign Testing Module
│       ├── schemas/          # VCDesign Test Pack 定義スキーマ (YAML)
│       ├── examples/         # 実装サンプル (Maintenance Ticket API)
│       └── runners/          # テストランナー環境
│
└── README.md
Workflow: From Design to Verification
VCDesignでは、曖昧な自然言語による設計合意を「Test Pack」という構造化された契約（Contract）に変換し、そこから実装と検証を行うフローを提供します。

1. Design Phase (Protocol)
prompts/value-continuity-protocols_v1.0.md を読み込ませたAIと共に、システムの境界（Boundaries）、責任の所在（Responsibility）、停止条件（Stop Conditions）を対話的に設計します。AIは「不確実性の共犯者」にならず、リスクを指摘する観測者として振る舞います。

2. Contract Phase (Test Pack)
設計セッションのログや要約を prompts/vcdesign_to_testpack.prompt.md に入力し、VCDesign Test Pack (YAML) を生成します。

これは人間が責任を持って合意した「唯一の正」となるドキュメントです。

スキーマ定義: modules/testing/schemas/vcdesign_test_pack.schema.yaml

3. Verification Phase (Test Generation)
確定した Test Pack を prompts/testpack_to_tests.prompt.md に入力し、以下のテストコードを自動生成します。

Contract Tests: OpenAPI等の外部契約の検証

Property-based Tests (PBT): 状態遷移や不変条件（Invariants）の検証

Scenario Tests: BDDスタイルによる受け入れテスト

Key Concepts
Boundary Design: 何を自動化し、何を人間が判断するか（IDG: Interface Determinability Gate）を設計の中心に据えます。

Stop & Defer: 安全や信頼が脅かされる不確実な状況では、システムが「停止して人間に判断を委ねる（stop_and_defer_to_human）」ことを正しい振る舞いと定義します。

Fact vs Hypothesis: ログや事実（Fact）と、AIの推論（Hypothesis）を厳密に区別し、混同によるリスクを防ぎます。

---

## Context

このリポジトリは、AI支援システムにおける
「責任・境界・判断のあり方」を探究する
より大きな設計思想の一部として位置づけられています。

- VCDesign（設計思想・アーキテクチャ）  
  https://vcdesign.org/

本リポジトリは単体でも利用・理解できます。  
VCDesign を事前に知っている必要はありません。
