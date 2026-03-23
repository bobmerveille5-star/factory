# Doc Sync Skill

## Purpose
Synchroniser et valider la documentation d'un projet d'indicateur multi-plateforme, assurant que tous les documents sont cohérents et à jour.

## Trigger
Ce skill doit être invoqué après `cross_platform_review_skill` et avant `packaging_skill`. Il produit le DOC_SYNC_REPORT.md.

## Inputs
- `PRODUCT_SPEC.md`: Spécification produit originale
- `RULES_SPEC.md`: Spécification technique
- `ARCHITECTURE.md`: Documentation architecturale
- `CROSS_PLATFORM_REVIEW.md`: Revue multi-plateforme
- Tous les fichiers `..._REVIEW_REPORT.md`
- Fichiers source générés (mt5, mt4, pine, ninjatrader)

## Outputs
- `DOC_SYNC_REPORT.md`: Rapport de synchronisation contenant:
  - Statut de sync par document
  - Incohérences documentielles identifiées
  - Liste des corrections à appliquer
  - Checklist de validation finale

## Process

### 1. Inventaire des documents
- Lister tous les documents du projet
- Identifier leur dernier auteur (skill qui les a générés)
- Vérifier leur existence

### 2. Vérification de cohérence croisée
Pour chaque document:
- Les paramètres listés sont-ils cohérents avec RULES_SPEC?
- Les APIs documentées existent-elles dans les sources?
- Les descriptions fonctionnelles correspondent-elles au code?

### 3. Vérification de complétude
- PRODUCT_SPEC ↔ RULES_SPEC: Toutes les fonctionnalités couvertes?
- RULES_SPEC ↔ ARCHITECTURE: Toutes les règles architecturales?
- ARCHITECTURE ↔ Code: Toutes les classes/modules implémentés?

### 4. Vérification des références
- CROSS_PLATFORM_REFERENCE: Les stats sont-elles correctes?
- Les suggestions de correction ont-elles été appliquées?
- Les scores de qualité sont-ils cohérents avec les rapports?

### 5. Identification des problèmes
Pour chaque problème:
- Document source
- Problème identifié
- Correction recommandée
- Priorité (blocant, warning, info)

### 6. Génération du rapport
Structurer selon:
```
# Doc Sync Report - [INDICATEUR]

## Statut de synchronisation
| Document | Statut | Dernière maj |
|----------|--------|--------------|
| PRODUCT_SPEC | OK | ... |
| RULES_SPEC | OK | ... |
| MT5_REVIEW_REPORT | OK | ... |

## Incohérences identifiées
### D-001: [Titre]
- Document: [nom]
- Problème: [description]
- Correction: [suggestion]
- Priorité: [blocant/warning/info]

## Checklist de validation
- [ ] Tous les paramètres documentés dans RULES_SPEC
- [ ] Toutes les APIs validées dans DOCS_CHECKED
- [ ] Tous les tests implémentables
- [ ] Cross-platform cohérence vérifiée
- [ ] Documentation synchronisée

## Recommandations
- [Recommandation 1]
- [Recommandation 2]
```

## Validation
- Chaque document doit être vérifié
- Au moins une incohérence doit être identifiée
- La checklist doit être complète

## Example
```
Input: Tous docs + codes sources
Output:
- D-001: swingPeriod max=100 en MT5 code, mais docs disent 50
- D-002: Pine REVIEW utilise fonction deprecated
- Checklist: 4/5 complète
```