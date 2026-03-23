# Indicator Composer Skill

## Purpose
Composer plusieurs indicateurs existants pour créer des indicateurs composites avancés avec des signaux combinés, des croisements, et des confirmations multi-indicateurs.

## Trigger
Ce skill est invoqué quand l'utilisateur veut créer un indicateur basé sur plusieurs indicateurs existants (ex: "RSI + MACD + MA").

## Inputs
- `base_indicators`: Liste des indicateurs de base à combiner
- `composition_rules`: Règles de combinaison (signal, confirmation, filtre)
- `RULES_SPEC.md`: Spécifications existantes (optionnel)

## Outputs
- `COMPOSED_INDICATOR_SPEC.md`: Spécification de l'indicateur composite contenant:
  - Liste des indicateurs composants avec poids
  - Logique de combinaison
  - Signaux générés (primaire, confirmation, alerte)
  - Code source pour chaque plateforme

## Process

### 1. Analyse des indicateurs composants
Pour chaque indicateur:
- Extraire les paramètres configurables
- Identifier les sorties (valeurs, signaux)
- Déterminer les dépendances

### 2. Définition du mode de composition
Types de combinaison supportés:
- **Signal + Confirmation**: Indicateur A confirme Indicateur B
- **Filtre**: Indicateur A filtre les signaux de B
- **Crossover**: Croisement de deux indicateurs
- **Fusion Pondérée**: Moyenne pondérée de plusieurs indicateurs
- **Divergence**: Détection de divergence entre indicateurs

### 3. Conception des signaux
Pour chaque signal composé:
- Condition déclencheuse
- Indicateurs impliqués
- Priorité (primaire, secondaire, confirmation)

### 4. Implémentation par plateforme
Générer le code en respectant:
- Les limites de chaque plateforme
- Les performances de calcul
- La lisibilité du code

### 5. Génération COMPOSED_INDICATOR_SPEC
```markdown
# Indicateur Composé: [NOM]

## Composants
| Indicateur | Rôle | Poids | Paramètres |
|------------|------|-------|-------------|
| RSI | Signal principal | 1.0 | period=14 |
| MACD | Confirmation | 0.5 | fast=12,slow=26 |

## Logique de combinaison
### Signal principal
- RSI crossing overbought (70) ET MACD bullish crossover

### Confirmation
- Price above 200 MA

### Filtre trend
- ADX > 25

## Signaux
| Signal | Type | Condition | Priorité |
|--------|------|-----------|----------|
| Buy | Signal | RSI<30 AND MACD cross up | 1 |
| Buy Confirmed | Confirmation | ADX>25 AND Price>MA200 | 2 |
```

## Validation
- Chaque composant doit être implémentable
- Les conflits de signaux doivent être résolus
- Les performances doivent être acceptables (< 10ms par barre)

## Example
```
Input: ["RSI", "MACD"] avec règles "buy when RSI oversold AND MACD cross up"
Output:
- Composants: RSI (period=14), MACD (12,26,9)
- Signal buy: RSI < 30 AND MACD.Hist > 0 AND MACD.Hist[1] <= 0
- Signal sell: RSI > 70 AND MACD.Hist < 0 AND MACD.Hist[1] >= 0
- Code MT5, MT4, Pine, NinjaTrader
```