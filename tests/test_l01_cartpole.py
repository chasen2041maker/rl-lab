"""第 1 课测试：倒立摆的回合循环、随机策略的基准成绩、你写的规则。

数字是云端实跑核对过的（gymnasium 1.3.0，种子 0–19）：随机乱推平均 22.15 步，20 回合全是“杆倒了”。
"""

import pytest

from rl.policies import random_policy, rule_policy
from rl.runner import evaluate


def test_random_policy_baseline():
    """随机乱推：平均撑 22.15 步（0.44 秒），全部因为杆倒了结束。种子固定，每次跑都一样。"""
    rows = evaluate(random_policy, n_episodes=20)
    mean = sum(r["steps"] for r in rows) / len(rows)
    assert mean == pytest.approx(22.15)
    assert {r["why"] for r in rows} == {"杆倒了"}
    assert evaluate(random_policy, n_episodes=3) == rows[:3]      # 同样的种子，同样的结果


def test_return_equals_steps():
    """倒立摆每撑住一步奖励 +1，所以一回合的总奖励（回报）就等于撑的步数。"""
    for r in evaluate(random_policy, n_episodes=5):
        assert r["return"] == r["steps"]


def test_rule_policy_beats_random():
    """你的规则要比随机乱推撑得久（还没写就先跳过）。"""
    try:
        rule_policy([0.0, 0.0, 0.0, 0.0])
    except NotImplementedError:
        pytest.skip("rule_policy 还没写")
    rows = evaluate(rule_policy, n_episodes=20)
    mean = sum(r["steps"] for r in rows) / len(rows)
    assert mean > 30
    for obs in ([0, 0, 0.05, 0], [0, 0, -0.05, 0]):
        assert rule_policy(obs) in (0, 1)
