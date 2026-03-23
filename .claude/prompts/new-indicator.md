# Prompts pour Trading Indicator Factory

## Prompt: Nouveau projet d'indicateur

Tu vas créer un nouvel indicateur de trading multi-plateforme. Suis le workflow GSD:

### Étape 1: Brief utilisateur
Demande à l'utilisateur de décrire:
- Le nom de l'indicateur
- Sa fonctionnalité principale
- Les paramètres souhaités
- Les plateformes cibles

### Étape 2: Exécution des skills
Pour chaque phase:

**Phase 1 - Foundation:**
1. Exécute `brief_intake_skill` → PRODUCT_SPEC.md
2. Exécute `rules_formalizer_skill` → RULES_SPEC.md
3. Pour chaque plateforme: doc_guard → DOCS_CHECKED.md

**Phase 2 - Pipeline:**
4. Exécute `architecture_skill` → ARCHITECTURE.md
5. Exécute `test_design_skill` → TEST_CASES.md

**Phase 3 - Codegen:**
6. Pour chaque plateforme: codegen → code source

**Phase 4 - QC:**
7. Pour chaque plateforme: review → REVIEW_REPORT.md
8. Exécute `cross_platform_review` → CROSS_PLATFORM_REVIEW.md

**Phase 5 - Delivery:**
9. Exécute `doc_sync_skill` → DOC_SYNC_REPORT.md
10. Exécute `decision_logger_skill` → DECISIONS.md
11. Exécute `packaging_skill` → livrable final

### Étape 3: Validation
- Vérifie que chaque phase produce les fichiers attendus
- Valide que les skills trouvent au moins un problème
- Confirme que le package est auto-suffisant