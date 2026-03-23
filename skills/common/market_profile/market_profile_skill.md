# Market Profile Skill

## Purpose
Créer un Market Profile (TPO Profile) qui divise chaque session en périodes de temps égales et identifie le Point de Contrôle (POC), les Value Areas, et les zones de contrôle.

## Trigger
Ce skill est invoqué quand l'utilisateur veut analyser la distribution des prix sur une session pour identifier les zones d'équilibre et de déséquilibre.

## Inputs
- Données de prix (OHLC)
- Configuration (sessions, bins, timezone)
- Mode (Classic, TPO, Volume Profile)

## Outputs
- `MARKET_PROFILE_REPORT.md`: Rapport contenant:
  - POC (Point of Control)
  - Value Area High/Low
  - Zones d'équilibre/déséquilibre
  - Visualisation textuelle

## Process

### 1. Construction du profil
- Diviser session en bins de temps égaux
- Compter temps passé à chaque niveau de prix
- Identifier où le prix a passé le plus de temps

### 2. Métriques clés
- **POC**: Prix avec plus de temps
- **VA High/Low**: Zone où 70% du temps
- **IB (Initial Balance)**: Première heure de trading
- **Opening Range**: Range d'ouverture

### 3. Signaux
- **POC Test**: Retour sur POC
- **VA Break**: Cassure de Value Area
- **Balance/Range**: Mode range vs trend

## Output Example
```markdown
# Market Profile - D1

## Session: 2024-03-15

### Métriques
| Métrique | Valeur |
|----------|--------|
| POC | 1.2450 |
| VA High | 1.2500 |
| VA Low | 1.2400 |
| IB | 1.2420 - 1.2480 |
| Closing | 1.2470 |

## Analyse
- Mode: TREND (cassure VA)
- POC Test: EN ATTENTE
- Opening Range: 60 pips

## Zones
[Visualisation ASCII du profil]
     1.2500    VA High
     |
     |   ####  (30% du temps)
     |
     1.2450    POC (40% du temps)
     |
     |   ####  (30% du temps)
     |
     1.2400    VA Low
```

## Validation
- POC doit correspondre au prix le plus traded
- VA doit couvrix ~70% des trades
- doit être timezone-aware

## Example
```
Input: EURUSD H1, session London
Output: POC, VA High/Low, IB, analyse trend/range
```