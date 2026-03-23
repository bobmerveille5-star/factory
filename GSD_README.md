# GSD - Trading Indicator Factory

Ce projet est configuré pour fonctionner avec **GSD (Get Shit Done)** de Claude Code.

## Installation

```bash
# Installer Node.js si nécessaire
# Puis exécuter depuis le dossier trading-indicator-factory:
npm install
```

## Commandes disponibles

```bash
# Lister tous les skills disponibles
npm run list-skills
# ou
node .claude/get-shit-done/bin/gsd-tools.cjs list-skills

# Créer un nouveau projet d'indicateur
npm run new <nom> <description>
# ou
node .claude/get-shit-done/bin/gsd-tools.cjs new my-indicator "Description"

# Voir le statut d'un projet
npm run status <projet>
# ou
node .claude/get-shit-done/bin/gsd-tools.cjs status my-indicator
```

## Workflow GSD

### 1. Nouveau projet
```bash
node .claude/get-shit-done/bin/gsd-tools.cjs new my-indicator "Mon nouvel indicateur"
```

### 2. Phase 1 - Foundation
Les skills valident les APIs et formalisent les règles:
- `rules_formalizer` → RULES_SPEC.md
- `mt5/mt4/pine/ninjatrader_doc_guard` → DOCS_CHECKED.md

### 3. Phase 2 - Pipeline
- `brief_intake` → PRODUCT_SPEC.md
- `architecture` → ARCHITECTURE.md
- `test_design` → TEST_CASES.md

### 4. Phase 3 - Codegen
Génère le code source pour chaque plateforme:
- `mt5_indicator_codegen` → src/*.mq5
- `mt4_indicator_codegen` → src/*.mq4
- `pine_indicator_codegen` → src/*.pine
- `ninjatrader_indicator_codegen` → src/*.cs

### 5. Phase 4 - QC
- Reviews individuelles par plateforme → REVIEW_REPORT.md
- `cross_platform_review` → CROSS_PLATFORM_REVIEW.md

### 6. Phase 5 - Delivery
- `doc_sync` → DOC_SYNC_REPORT.md
- `decision_logger` → DECISIONS.md
- `packaging` → Archive zip finale

## Structure GSD

```
.claude/
├── get-shit-done/
│   ├── settings.json      # Configuration GSD
│   ├── bin/
│   │   └── gsd-tools.cjs  # CLI tools
│   └── templates/
│       └── new-indicator.md
├── agents/
│   └── project-researcher.md
└── prompts/
    └── new-indicator.md
```

## Utilisation avec Claude Code

Pour invoquer un skill avec Claude Code, utiliser la commande `/test` ou exécuter directement les fichiers de skill markdown.

Les skills sont situés dans `skills/` et suivent la structure:
```
skills/
├── common/
│   ├── brief_intake/
│   ├── rules_formalizer/
│   ├── architecture/
│   ├── test_design/
│   ├── cross_platform_review/
│   ├── doc_sync/
│   ├── decision_logger/
│   └── packaging/
├── mt5/
│   ├── doc_guard/
│   ├── indicator_codegen/
│   └── review/
├── mt4/
├── pine/
└── ninjatrader/
```