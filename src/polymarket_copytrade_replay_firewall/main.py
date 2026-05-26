from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass
class RiskConfig:
    max_slippage_bps: int = 100
    max_position: float = 100.0
    cooldown_seconds: int = 30
    max_drawdown: float = 0.2


@dataclass
class RunResult:
    wallet: str
    mode: str
    allowed: bool
    reason: str


def run(wallet: str, mode: str, risk: RiskConfig) -> RunResult:
    if risk.max_drawdown <= 0 or risk.max_drawdown > 1:
        return RunResult(wallet=wallet, mode=mode, allowed=False, reason="invalid max_drawdown")
    if risk.max_position <= 0:
        return RunResult(wallet=wallet, mode=mode, allowed=False, reason="invalid max_position")
    return RunResult(wallet=wallet, mode=mode, allowed=True, reason="ok")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Polymarket Replay + Risk Firewall")
    p.add_argument("--wallet", required=True, help="Wallet to follow/backtest")
    p.add_argument("--mode", choices=["replay", "shadow", "live"], default="shadow")
    p.add_argument("--max-slippage-bps", type=int, default=100)
    p.add_argument("--max-position", type=float, default=100.0)
    p.add_argument("--cooldown-seconds", type=int, default=30)
    p.add_argument("--max-drawdown", type=float, default=0.2)
    return p


def cli() -> int:
    args = build_parser().parse_args()
    risk = RiskConfig(
        max_slippage_bps=args.max_slippage_bps,
        max_position=args.max_position,
        cooldown_seconds=args.cooldown_seconds,
        max_drawdown=args.max_drawdown,
    )
    result = run(wallet=args.wallet, mode=args.mode, risk=risk)
    status = "ALLOW" if result.allowed else "BLOCK"
    print(f"[{status}] wallet={result.wallet} mode={result.mode} reason={result.reason}")
    return 0 if result.allowed else 2


if __name__ == "__main__":
    raise SystemExit(cli())
