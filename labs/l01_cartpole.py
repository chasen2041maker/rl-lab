"""第 1 课实验：倒立摆，随机乱推 vs 你写的规则，各玩 20 回合（种子 0–19）。

运行（在仓库根目录）：
    python -m labs.l01_cartpole           随机乱推；你写好规则以后，规则也一起跑
    python -m labs.l01_cartpole --show    开窗口看 3 回合（写好规则就看规则，没写就看随机）
"""

from __future__ import annotations

import sys

from rl.policies import random_policy, rule_policy
from rl.runner import evaluate

STEP_S = 0.02        # 倒立摆每一步 0.02 秒，500 步 = 10 秒


def rule_is_written() -> bool:
    """你的规则写了没有：随便喂一个状态试试，没写会抛 NotImplementedError。"""
    try:
        rule_policy([0.0, 0.0, 0.0, 0.0])
        return True
    except NotImplementedError:
        return False


def summarize(name: str, rows: list[dict]) -> None:
    """一个策略 20 回合的成绩：平均撑几步、最少最多、每回合怎么结束的。"""
    steps = []
    whys = {}
    for r in rows:
        steps.append(r["steps"])
        whys[r["why"]] = whys.get(r["why"], 0) + 1
    mean = sum(steps) / len(steps)
    parts = []
    for why, n in whys.items():
        parts.append(f"{why} {n} 回合")
    why_text = "、".join(parts)
    print(f"{name}：平均撑 {mean:.2f} 步（{mean * STEP_S:.2f} 秒），最少 {min(steps)}、最多 {max(steps)}；{why_text}")
    print(f"    每回合撑的步数：{steps}")


def main():
    written = rule_is_written()
    if "--show" in sys.argv:
        policy = rule_policy if written else random_policy
        print(f"开窗口看 3 回合：{'你的规则' if written else '随机乱推'}")
        summarize("看到的这 3 回合", evaluate(policy, n_episodes=3, render=True))
        return
    print("倒立摆 CartPole：每撑住一步奖励 +1；杆倒过 12° 或小车出轨就结束；最多 500 步（10 秒）。\n")
    summarize("随机乱推", evaluate(random_policy))
    if written:
        summarize("你的规则", evaluate(rule_policy))
    else:
        print("\n你的规则还没写：打开 rl/policies.py，把 rule_policy 里那行 raise 换成你的规则（见 docs/L01_cartpole.md 第 3 步）。")


if __name__ == "__main__":
    main()
