# Decision Logger Skill

## Purpose
Enregistrer et tracer toutes les décisions architecturales et techniques prises durant le développement d'un indicateur de trading multi-plateforme.

## Trigger
Ce skill doit être invoqué après `doc_sync_skill` et avant `packaging_skill`. Il produit le DECISIONS.md.

## Inputs
- `PRODUCT_SPEC.md`: Spécification produit
- `RULES_SPEC.md`: Spécification technique
- `ARCHITECTURE.md`: Architecture
- `CROSS_PLATFORM_REVIEW.md`: Revue multi-plateforme
- Tous les `..._REVIEW_REPORT.md`
- `DOC_SYNC_REPORT.md`: Rapport de sync
- Sessions de travail (notes, conversations)

## Outputs
- `DECISIONS.md`: Journal des décisions contenant:
  - Liste chronologique des décisions
  - Contexte de chaque décision
  - Alternatives considérées
  - Justification du choix
  - Implications futures

## Process

### 1. Collecte des décisions implicites
Parcourir tous les documents et extraire:
- Choix de paramètres par défaut
- Choix algorithmiques
- Choix d'architecture
- Résolution des conflits

### 2. Classification des décisions
Catégoriser chaque décision:
- **Design**: Choix fonctionnel (paramètres, comportements)
- **Technique**: Choix d'implémentation (algorithmes, structures)
- **Plateforme**: Choix spécifiques à une plateforme
- **Revue**: Corrections issues des reviews

### 3. Documentation de chaque décision
Pour chaque décision:
- Titre et描述
- Contexte (pourquoi la question s'est posée)
- Options considérées (au moins 2)
- Décision prise
- Justification
- Date/timestamp

### 4. Identification des décisions réversibles
- Quelles décisions peuvent être modifiées?
- Quel impact aurait un changement?
- Dependencies entre décisions

### 5. Génération du DECISIONS.md
Structurer selon:
```
# Décisions - [INDICATEUR]

## Décisions de Design
### D-001: [Titre]
- Date: [YYYY-MM-DD]
- Contexte: [Pourquoi cette question]
- Options:
  1. [Option A]
  2. [Option B]
- Décision: [Option choisie]
- Justification: [Pourquoi ce choix]
- Réversible: [OUI/NON - conditions]

## Décisions Techniques
### T-001: [Titre]
- ...

## Décisions par Plateforme
### P-001: [Titre]
- ...

## Décisions de Revue
### R-001: [Titre]
- ...

## Dépendances entre décisions
- [D-001] affecte [D-002]
- [T-001] dépend de [D-001]

## Recommandations futures
- [Recommandation 1]
```

## Validation
- Chaque décision significative doit être documentée
- Au moins 5 décisions doivent être identifiées
- Les justifications doivent être claires

## Example
```
Input: Documents + reviews
Output:
- D-001: swingPeriod default = 14 (vs 20)
- D-002: Confirmation bars = 1 (vs 2)
- T-001: Buffer circulaire vs recalcul complet
- R-001: Correction handle MT5 non libéré
- Total: 12 décisions documentées
```