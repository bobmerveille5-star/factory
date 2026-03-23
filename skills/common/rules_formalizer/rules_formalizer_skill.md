# Rules Formalizer Skill

## Purpose
Transformer une description fonctionnelle brute en spécification technique précise et non ambiguë pour la génération de code d'indicateurs de trading.

## Trigger
Ce skill doit être invoqué après `brief_intake_skill` et avant `architecture_skill`. Il transforme le PRODUCT_SPEC.md en RULES_SPEC.md avec des règles techniques exactes.

## Inputs
- `PRODUCT_SPEC.md`: Spécification produit contenant la description fonctionnelle de l'indicateur
- `brief_notes`: Notes additionnelles du brief d'entrée (optionnel)

## Outputs
- `RULES_SPEC.md`: Spécification des règles techniques内容包括:
  - Définitions précises des paramètres d'entrée
  - Logique algorithmique détaillée
  - Conditions de déclenchement et calculs
  - Comportement aux bords (border cases)
  - Valeurs par défaut validées

## Process

### 1. Extraction des composants fonctionnels
- Identifier les éléments visuels (lignes, zones, flèches, labels)
- Identifier les données d'entrée nécessaires (prix, volumes, indicateurs)
- Identifier les seuils et constantes

### 2. Formalisation des règles de calcul
Pour chaque calcul:
- Définir la formule mathématique exacte
- Définir la période/fenêtre temporelle
- Définir le type de données (double, int, datetime)
- Définir l'arrondi requis

### 3. Définition des paramètres
Pour chaque paramètre:
- Nom technique (CamelCase ou snake_case selon plateforme)
- Type primitif
- Plage de valeurs valides
- Valeur par défaut
- Description fonctionnelle

### 4. Identification des border cases
- Valeurs nulles ou manquantes
- Périodes invalides (négatives, zéro)
- Premiers barres (données insuffisantes)
- Division par zéro potentielle

### 5. Validation de complétude
- Toutes les règles sont vérifiables
- Aucune ambiguïté fonctionnelle
- Toutes les formules sont auto-suffisantes

## Validation
- Le RULES_SPEC.md doit permettre à un développeur de coder l'indicateur sans poser de questions
- Chaque paramètre doit avoir une plage de validité explicite
- Chaque formule doit pouvoir être testée unitairement

## Example
```
Input: PRODUCT_SPEC décrivant "afficher les swing highs avec confirmation"
Output: RULES_SPEC avec:
- Param: swingPeriod (int, 1-100, défaut: 14)
- Param: confirmationType (enum: close, high_low, candle)
- Règle: Swing High = highest[high, swingPeriod] où high > tous les highs période-1 précédente et suivante
- Border case: handle période insuffisante
```