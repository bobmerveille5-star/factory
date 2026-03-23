# MT5 Indicator Codegen Skill

## Purpose
Générer du code MQL5 optimisé et conforme aux spécifications pour un indicateur de trading.

## Trigger
Ce skill doit être invoqué après `mt5_doc_guard_skill` et avant `mt5_review_skill`. Il utilise RULES_SPEC.md, ARCHITECTURE.md et MT5_DOCS_CHECKED.md pour produire le code source.

## Inputs
- `RULES_SPEC.md`: Spécification technique détaillée
- `ARCHITECTURE.md`: Architecture de l'indicateur
- `MT5_DOCS_CHECKED.md`: Validation des APIs MQL5
- `TEST_CASES.md`: Cas de test à valider

## Outputs
- Fichier source `...mq5` dans le dossier `projects/[nom]/mt5/src/`
- Code conforme aux standards MQL5
- Code testable et maintenable

## Process

### 1. Préparation de l'environnement
- Créer la structure de fichier standard MQL5
- Définir les includes nécessaires
- Configurer les propriétés du programme (#property)

### 2. Définition des paramètres
Pour chaque paramètre de RULES_SPEC:
- Créer les variables `input`
- Définir les plages de validité
- Initialiser avec les valeurs par défaut
- Ajouter les descriptions pour l'input dialog

### 3. Implémentation des buffers
- Créer les buffers d'indicateur avec `SetIndexBuffer`
- Configurer les styles de plot (ligne, histo, flèche)
- Définir les labels

### 4. Implémentation de OnInit
- Initialiser les indicateurs techniques (`iMA`, `iRSI`, etc.)
- Configurer les paramètres de dessin
- Valider les paramètres d'entrée

### 5. Implémentation de OnCalculate
Pour chaque calcul de RULES_SPEC:
- Récupérer les données nécessaires (prix, indicateurs)
- Implémenter la logique avec les validations de MT5_DOCS_CHECKED
- Gérer les border cases (premières barres, données manquantes)
- Écrire dans les buffers

### 6. Optimisation
- Utiliser les buffers comme.circular pour les lookbacks
- Minimiser les appels redondants aux indicateurs
- Éviter les allocations mémoire inutiles

### 7. Standards de codage MQL5
- Conventions de nommage: `camelCase` pour variables, `PascalCase` pour classes
- Commentaires JSDoc pour les fonctions publiques
- Gestion stricte des types
- Pas de code mort

## Validation
- Le code compile sans erreur dans MetaEditor
- Tous les TEST_CASES sont implémentables
- Aucune fonction INVALID de MT5_DOCS_CHECKED utilisée
- Code respecte les standards MQL5

## Example
```
Input: RULES_SPEC swingPeriod=14, confirmationBars=1
Output: SwingHighLow.mq5:
- input int SwingPeriod = 14;
- input int ConfirmationBars = 1;
- #property indicator_chart_window
- SetIndexBuffer(0, swingHighBuffer);
- OnCalculate: calculate swing highs with confirmation
```