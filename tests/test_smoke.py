from polymarket_copytrade_replay_firewall.main import RiskConfig, run


def test_smoke_run_allows_valid_config():
    result = run(wallet="0xabc", mode="replay", risk=RiskConfig())
    assert result.allowed
    assert result.reason == "ok"
