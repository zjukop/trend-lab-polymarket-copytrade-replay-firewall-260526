# Polymarket Replay + Risk Firewall

Minimal Python starter for a **copy-trade safely** toolkit:
- replay/backtest scaffold
- shadow mode scaffold
- risk firewall scaffold

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m polymarket_copytrade_replay_firewall.main --help
pytest -q
```

## Example

```bash
python -m polymarket_copytrade_replay_firewall.main \
  --wallet 0xWhale \
  --mode replay \
  --max-position 100 \
  --max-drawdown 0.2
```
