# Swing High/Low with Close Confirmation

## Résumé
Indicateur affichant les points swing highs et lows avec confirmation par clôture des barres suivantes.

## Cas d'usage
- Identification des sommets et vallées importants
- Signaux de retournement potentiels
- Confirmation de趋势

## Comportement
L'indicateur identifie les maxima et minima locaux sur une période configurable. Un point n'est confirmé comme swing high/low que lorsque les N barres suivantes clôture en dessous/dessus.

## Données d'entrée
- Prix: High, Low, Close
- Timeframe: Tous timeframes

## Paramètres
| Nom | Type | Défaut | Plage | Description |
|-----|------|--------|-------|-------------|
| SwingPeriod | int | 14 | 5-50 | Période de recherche du swing |
| ConfirmationBars | int | 1 | 1-5 | Nombre de barres de confirmation |

## Questions ouvertes
- Comment gérer les faux signaux en marché latéral?
- Quelle couleur pour les highs vs lows?