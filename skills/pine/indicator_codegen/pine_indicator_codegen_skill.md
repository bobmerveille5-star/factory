# Pine Indicator Codegen Skill

## Purpose
Générer du code Pine Script optimisé et conforme aux spécifications pour un indicateur TradingView.

## Trigger
Ce skill doit être invoqué après `pine_doc_guard_skill` et avant `pine_review_skill`. Il utilise RULES_SPEC.md, ARCHITECTURE.md et PINE_DOCS_CHECKED.md pour produire le code source.

## Inputs
- `RULES_SPEC.md`: Spécification technique détaillée
- `ARCHITECTURE.md`: Architecture de l'indicateur
- `PINE_DOCS_CHECKED.md`: Validation des APIs Pine Script
- `TEST_CASES.md`: Cas de test à valider

## Outputs
- Fichier source `...pine` dans le dossier `projects/[nom]/pine/src/`
- Code conforme aux standards Pine Script v5
- Code compatible avec TradingView

## Process

### 1. Préparation de l'en-tête
- Déclarer la version Pine (`//@version=5`)
- Définir l'identifiant de stratégie/indicateur
- Importer les bibliothèques nécessaires

### 2. Définition des paramètres d'entrée
Pour chaque paramètre de RULES_SPEC:
- Utiliser `input.<type>()` pour les paramètres ajustables
- Définir les valeurs par défaut
- Ajouter les tooltips
- Spécifier les options pour les enums

### 3. Calculs avec ta.\* et les fonctions Pine
- Utiliser `ta.sma()`, `ta.rma()`, `ta.wma()`, `ta.ema()`
- Utiliser `ta.rsi()`, `ta.macd()`, etc.
- Combiner avec les opérateurs Pine
- Gérer les calculs complexes

### 4. Implémentation du plot
- Utiliser `plot()` pour les lignes
- Utiliser `plotshape()` pour les marqueurs
- Utiliser `plotbar()`, `plotcandle()`
- Configurer les couleurs, styles, largeurs
- Utiliser `fill()` pour les zones

### 5. Gestion des états avec var
- Utiliser `var` pour les variables persistantes
- Gérer les changements d'état
- Implémenter les compteurs et accumulateurs

### 6. Sécurité et bonnes pratiques
- Limiter l'utilisation de `security()` (appels réseau)
- Utiliser `max_bars_back` si nécessaire
- Optimiser les calculs coûteux
- Éviter les références futures

### 7. Standards Pine v5
- Type declarations explicites
- Utiliser les constantes de couleur
-Commentaires pour la documentation
- Respecter les limites de Pine (30k lignes)

## Validation
- Le code est syntaxiquement valide Pine v5
- Aucune fonction DEPRECATED ou INVALID utilisée
- Compatible avec l'éditeur TradingView
- Tous les TEST_CASES sont implémentables

## Example
```
Input: RULES_SPEC swingPeriod=14, confirmationBars=1
Output:
//@version=5
indicator("Swing High/Low", overlay=true)
input.int(14, "Swing Period")
input.int(1, "Confirmation Bars")

// Calculate swing highs
swingHigh = ta.pivothigh(...)
plotshape(swingHigh, title="Swing High", ...)
```