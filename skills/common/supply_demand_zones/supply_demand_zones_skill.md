# Supply Demand Zones Skill

## Purpose
Identifier automatiquement les zones d'offre (supply) et de demande (demand) sur le graphique, qui représentent des niveaux où le prix a historiquement rebondi ou été rejeté.

## Trigger
Ce skill est invoqué quand l'utilisateur veut identifier les zones de support/résistance dynamiques basées sur le comportement du prix.

## Inputs
- Données de prix (OHLC)
- Configuration (lookback, swing size, overlap)
- Mode (Supply only, Demand only, Both)

## Outputs
- `SUPPLY_DEMAND_REPORT.md`: Rapport contenant:
  - Zones de demande identifiées
  - Zones d'offre identifiées
  - Force de chaque zone
  - Signaux associés

## Process

### 1. Identification des zones
**Zone de demande (Demand):**
- Prix a rebondi depuis un niveau
- Plusieurs toucher bas
- Base horizontale claire

**Zone d'offre (Supply):**
- Prix a été rejeté depuis un niveau
- Plusieurs toucher haut
- Base horizontale claire

### 2. Paramètres
- **Swing Size**: Taille minimum du swing (10-50 pips)
- **Lookback**: Nombre de barres à analyser
- **Overlap**:，允许 les zones qui se chevauchent

### 3. Scoring des zones
- **Force**: Basé sur le nombre de touchers
- **Freshness**: Recent vs ancien
- **Proximity**: Distance du prix actuel

## Output Example
```markdown
# Supply & Demand Zones

## Zones de Demande

### DZ-001
- Range: 1.2000 - 1.2050
- Touchers: 4
- Force: 90%
- Freshness: FRESH
- Distance: 50 pips
- Action: BUY ZONE

### DZ-002
- Range: 1.1800 - 1.1850
- Touchers: 2
- Force: 50%
- Freshness: AGED

## Zones d'Offre

### SZ-001
- Range: 1.2500 - 1.2550
- Touchers: 3
- Force: 75%
- Freshness: FRESH

## Signaux
- Enter when price returns to DZ-001
- Stop below zone
- Target: next supply zone
```

## Validation
- Chaque zone doit avoir un score de force
- Zones doivent être actionnables
- Code performant

## Example
```
Input: Prix EURUSD, swing=20, lookback=500
Output: 3 zones demande, 2 zones offre, avec scores
```