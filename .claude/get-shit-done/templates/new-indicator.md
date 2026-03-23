# Template: New Indicator Project

## Structure créée

```
projects/[INDICATOR_NAME]/
├── PRODUCT_SPEC.md          # Brief formalisé
├── RULES_SPEC.md            # Spécification technique
├── OPEN_QUESTIONS.md         # Questions ouvertes
├── ARCHITECTURE.md           # Architecture technique
├── TEST_CASES.md             # Cas de test
├── DECISIONS.md              # Journal des décisions
├── CROSS_PLATFORM_REVIEW.md  # Revue croisée
├── DOC_SYNC_REPORT.md        # Sync documentation
├── mt5/
│   ├── MT5_DOCS_CHECKED.md
│   ├── MT5_REVIEW_REPORT.md
│   └── src/[indicateur].mq5
├── mt4/
│   ├── MT4_DOCS_CHECKED.md
│   ├── MT4_REVIEW_REPORT.md
│   └── src/[indicateur].mq4
├── pine/
│   ├── PINE_DOCS_CHECKED.md
│   ├── PINE_REVIEW_REPORT.md
│   └── src/[indicateur].pine
└── ninjatrader/
    ├── NINJATRADER_DOCS_CHECKED.md
    ├── NINJATRADER_REVIEW_REPORT.md
    └── src/[indicateur].cs
```

## Ordre d'exécution

1. brief_intake_skill → PRODUCT_SPEC.md
2. rules_formalizer_skill → RULES_SPEC.md
3. architecture_skill → ARCHITECTURE.md
4. test_design_skill → TEST_CASES.md
5. [platform]_doc_guard → [PLATFORM]_DOCS_CHECKED.md
6. [platform]_codegen → code source
7. [platform]_review → [PLATFORM]_REVIEW_REPORT.md
8. cross_platform_review → CROSS_PLATFORM_REVIEW.md
9. doc_sync_skill → DOC_SYNC_REPORT.md
10. decision_logger_skill → DECISIONS.md
11. packaging_skill → livrable final