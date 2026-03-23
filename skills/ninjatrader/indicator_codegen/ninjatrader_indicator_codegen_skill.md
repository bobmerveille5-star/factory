# NinjaTrader Indicator Codegen Skill

## Purpose
Générer du code NinjaScript optimisé et conforme aux spécifications pour un indicateur NinjaTrader.

## Trigger
Ce skill doit être invoqué après `ninjatrader_doc_guard_skill` et avant `ninjatrader_review_skill`. Il utilise RULES_SPEC.md, ARCHITECTURE.md et NINJATRADER_DOCS_CHECKED.md pour produire le code source.

## Inputs
- `RULES_SPEC.md`: Spécification technique détaillée
- `ARCHITECTURE.md`: Architecture de l'indicateur
- `NINJATRADER_DOCS_CHECKED.md`: Validation des APIs NinjaTrader
- `TEST_CASES.md`: Cas de test à valider

## Outputs
- Fichier source `...cs` dans le dossier `projects/[nom]/ninjatrader/src/`
- Code conforme aux standards NinjaScript
- Code compatible avec NinjaTrader 8 ou 9

## Process

### 1. Préparation de la structure
- Créer la classe héritant de `Indicator`
- Définir les propriétés Name, Description
- Configurer les entrées utilisateur avec `[Parameter]`

### 2. Définition des entrées utilisateur
Pour chaque paramètre de RULES_SPEC:
- Utiliser `[Parameter]` pour les paramètres
- Utiliser `[Input]` pour les données d'entrée
- Définir les valeurs par défaut
- Spécifier les ranges avec MinValue/MaxValue

### 3. Déclaration des plots
- Utiliser `[Output]` pour les buffers de sortie
- Spécifier les couleurs et styles
- Définir les options de rendu

### 4. Implémentation de OnStateChange
Gérer les états:
- `SetState.State.Configure`: Configurer l'indicateur
- `SetState.State.DataLoaded`: Préparer les calculs
- Allouer les tableaux nécessaires

### 5. Implémentation de OnBarUpdate
Pour chaque calcul:
- Accéder aux données via `BarsArray`
- Utiliser les fonctions d'indicateurs intégrés (SMA, RSI)
- Implémenter la logique métier
- Écrire dans les outputs

### 6. Différences NT8 vs NT9
- NT8: API historique
- NT9: Nouvelles APIs, async operations
- Choisir la version cible

### 7. Standards NinjaScript
- Conventions: PascalCase pour propriétés
- Using statements pour les namespaces
- Gestion des erreurs avec try-catch
- Documentation XML pour les propriétés

## Validation
- Le code compile sans erreur dans NinjaTrader
- Aucune méthode INVALID de NINJATRADER_DOCS_CHECKED utilisée
- Code respecte les patterns NinjaScript
- Compatible avec la version ciblée (NT8 ou NT9)

## Example
```
Input: RULES_SPEC swingPeriod=14
Output: SwingHighLow.cs:
- public class SwingHighLow : Indicator
- [Parameter(DefaultValue = 14)]
- public int SwingPeriod { get; set; }
- [Output]
- public DataSeries SwingHighs { get; }
- OnBarUpdate: calculate swing highs using High series
```