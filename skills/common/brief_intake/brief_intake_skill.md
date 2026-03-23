# Brief Intake Skill

## Purpose
Capturer et formaliser la demande initiale d'un utilisateur pour un indicateur de trading, produisant une spécification produit structurée.

## Trigger
Ce skill est le point d'entrée du workflow. Il doit être invoqué dès qu'un utilisateur décrit une idée d'indicateur de trading.

## Inputs
- `user_input`: Description brute de l'indicateur (texte libre, capture d'écran, ou conversation)
- `existing_docs`: Documentation existante sur des indicateurs similaires (optionnel)

## Outputs
- `PRODUCT_SPEC.md`: Spécification produit structurée contenant:
  - Nom de l'indicateur
  - Résumé fonctionnel (1-2 phrases)
  - Cas d'usage principaux
  - Comportement visuel souhaité
  - Données d'entrée nécessaires
  - Paramètres ajustables
  - Contraintes identifiées

## Process

### 1. Analyse de la demande
- Identifier l'intention principale (analyse technique, signal,过滤)
- Extraire les mots-clés fonctionnels
- Distinguer les exigences des suggestions

### 2. Classification
Déterminer le type d'indicateur:
- **Trend**: Suivi de tendance (Moving Averages, ADX)
- **Momentum**: Force du mouvement (RSI, MACD, Stochastic)
- **Volatility**: Volatilité (Bollinger Bands, ATR)
- **Volume**: Volume (OBV, VWAP)
- **Custom**: Combinaison ou unique

### 3. Extraction des composants
Pour chaque composant identifié:
- Nom du composant
- Rôle fonctionnel
- Dépendances (autres indicateurs, données)
- Comportement désiré

### 4. Définition des paramètres ajustables
Pour chaque paramètre:
- Nom lisible (pour UI)
- Rôle fonctionnel
- Plage de valeurs raisonnable
- Valeur par défaut recommandée
- Sensibilité (impact sur le résultat)

### 5. Identification des questions ouvertes
- Éléments non spécifiés clairement
- Ambiguïtés nécessitant clarification
- Choix architecturaux à décider

### 6. Génération PRODUCT_SPEC
Structurer selon le template standard:
```
# [NOM]

## Résumé
[Description fonctionnelle en 1-2 phrases]

## Cas d'usage
- [Usage 1]
- [Usage 2]

## Comportement
[Description du comportement visuel et technique]

## Données d'entrée
- [Donnée 1:OHLCV, timeframe, etc.]

## Paramètres
| Nom | Type | Défaut | Plage | Description |
|-----|------|--------|-------|-------------|
| ... | ... | ... | ... | ... |

## Questions ouvertes
- [Question 1]
- [Question 2]
```

## Validation
- Le PRODUCT_SPEC doit être compréhensible par un utilisateur non technique
- Toutes les questions ouvertes doivent être documentées
- Le résumé doit permettre de comprendre l'indicateur en 10 secondes

## Example
```
Input: "Je veux un indicateur qui affiche les swing highs et lows avec confirmation 
de closing price. Comme une version simplifiée du ZigZag mais qui attend la clôture."

Output: PRODUCT_SPEC:
- Nom: Swing High/Low with Close Confirmation
- Type: Custom (Trend + Signal)
- Paramètres: swingPeriod (5-50, déf: 14), confirmationBars (1-5, déf: 1)
- Questions: Comment gérer les faux signaux en range?
```