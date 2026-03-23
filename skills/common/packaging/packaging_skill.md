# Packaging Skill

## Purpose
Préparer et assembler le livrable final d'un indicateur de trading multi-plateforme, incluant tous les fichiers nécessaires pour distribution et utilisation.

## Trigger
Ce skill doit être invoqué en dernier du workflow, après `decision_logger_skill`. Il produit le package final prêt à distribuer.

## Inputs
- `PRODUCT_SPEC.md`: Spécification produit
- `RULES_SPEC.md`: Spécification technique
- Tous les fichiers source (mt5, mt4, pine, ninjatrader)
- `DECISIONS.md`: Journal des décisions
- `CROSS_PLATFORM_REVIEW.md`: Revue finale
- `DOC_SYNC_REPORT.md`: Rapport de sync

## Outputs
- Package complet dans le dossier du projet:
  - Code source pour chaque plateforme
  - Documentation utilisateur
  - Fichiers de configuration
  - Archive zip prête à distribuer

## Process

### 1. Vérification pré-package
- Tous les fichiers source compilent-ils?
- Toutes les reviews ont-elles APPROVED ou NEED_REVISION?
- La documentation est-elle synchronisée?
- Les décisions sont-elles documentées?

### 2. Préparation de la structure
Créer la structure standard:
```
[indicateur]/
├── README.md
├── CHANGELOG.md
├── LICENSE
├── docs/
│   ├── USER_GUIDE.md
│   ├── PARAMETERS.md
│   └── CHART_EXAMPLES.md
├── mt5/
│   └── [indicateur].mq5
├── mt4/
│   └── [indicateur].mq4
├── pine/
│   └── [indicateur].pine
└── ninjatrader/
    └── [indicateur].cs
```

### 3. Génération du README
- Description courte de l'indicateur
- Installation par plateforme
- Paramètres
- Exemples d'utilisation
- Avertissements

### 4. Génération du CHANGELOG
- Version actuelle
- Historique des versions
- breaking changes
- new features
- fixes

### 5. Génération des guides
- USER_GUIDE: Guide d'utilisation
- PARAMETERS: Référence des paramètres
- CHART_EXAMPLES: Exemples de graphiques

### 6. Création de l'archive
- Créer le zip du package
- Vérifier le contenu
- Générer le hash SHA256

### 7. Checklist finale
- [ ] Code MT5 compile
- [ ] Code MT4 compile
- [ ] Code Pine valide
- [ ] Code NinjaTrader compile
- [ ] Documentation complète
- [ ] Package zip créé

## Validation
- Le package doit être auto sufisant
- Un utilisateur doit pouvoir installer sans aide externe
- Tous les fichiers doivent être présents

## Example
```
Input: Tous documents + codes
Output:
- SwingHighLow/
  ├── README.md (2 pages)
  ├── CHANGELOG.md
  ├── mt5/SwingHighLow.mq5
  ├── mt4/SwingHighLow.mq4
  ├── pine/SwingHighLow.pine
  ├── ninjatrader/SwingHighLow.cs
  ├── docs/USER_GUIDE.md
  └── SwingHighLow_v1.0.0.zip (hash: abc123...)
```