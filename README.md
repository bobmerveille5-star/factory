# Trading Indicator Factory

**CLI pour générer des indicateurs de trading multi-plateformes en 30 secondes.**

```
Idee: "RSI avec alertes sur surachat/survente"
↓
python3 src/gsd/cli.py new my-rsi "RSI avec alertes"
python3 src/gsd/cli.py generate my-rsi
↓
→ my-rsi.mq5 (MT5)
→ my-rsi.mq4 (MT4)
→ my-rsi.pine (TradingView)
→ my-rsi.cs (NinjaTrader)
```

## 🎯 Qu'est-ce que c'est ?

Traduis une idée d'indicateur en code prêt-à-compiler pour **4 plateformes** :
- MetaTrader 5 (MQL5)
- MetaTrader 4 (MQL4)
- Pine Script (TradingView)
- NinjaTrader (NinjaScript)

## ⚡ Quickstart

```bash
# 1. Cloner
git clone https://github.com/bobmerveille5-star/factory.git
cd factory

# 2. Créer un indicateur
python3 src/gsd/cli.py new my-rsi "RSI avec alertes sur surachat"

# 3. Générer le code
python3 src/gsd/cli.py generate my-rsi

# 4. Vérifier
ls src/projects/my-rsi/*/src/
```

## 📁 Résultat

Après `generate`, vous obtient :

| Fichier | Description |
|---------|-------------|
| `mt5/src/my-rsi.mq5` | Code MQL5 prêt pour MT5 |
| `mt4/src/my-rsi.mq4` | Code MQL4 prêt pour MT4 |
| `pine/src/my-rsi.pine` | Script Pine v5 pour TradingView |
| `ninjatrader/src/my-rsi.cs` | C# pour NinjaTrader |

## 🔧 Commandes CLI

```bash
python3 src/gsd/cli.py list-skills              # Voir tous les skills
python3 src/gsd/cli.py detect "RSI + MACD"      # Détecter patterns
python3 src/gsd/cli.py new <nom> <desc>         # Créer projet
python3 src/gsd/cli.py generate <nom>           # Générer code
python3 src/gsd/cli.py validate <nom>           # Valider structure
python3 src/gsd/cli.py build <nom>              # Compiler projet
```

## 🧪 Tests

```bash
python3 -c "
import sys; sys.path.insert(0, 'src')
from lib.core import detect_patterns
assert 'rsi' in detect_patterns('RSI avec alertes')
print('✓ Tests passent')
"
```

## 📦 Structure

```
factory/
├── src/gsd/cli.py          # CLI principale
├── src/lib/core.py          # Moteur de patterns
├── tests/                   # Tests unitaires
├── skills/                  # 42 skills (specs)
├── projects/               # Projets générés
└── .github/workflows/       # CI/CD
```

## 🆚 Pourquoi pas un prompt ChatGPT ?

| ChatGPT | Trading Indicator Factory |
|---------|---------------------------|
| Code à copier-coller | Fichiers prêts |
| Erreurs de syntaxe possibles | Validation intégrée |
| 1 plateforme à la fois | 4 plateformes simultané |
| Pas de tests | Tests unitaires |
| Pas de structure | Projet structuré |

## 📝 License

MIT