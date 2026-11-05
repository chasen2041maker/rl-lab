"""策略（policy）：看到状态，决定动作的函数。第 1 课只有两个：随机乱推、你写的规则。

倒立摆 CartPole 的状态是 4 个数（obs）：
  obs[0] 小车位置（米，0 = 轨道正中；超过 ±2.4 就出轨）
  obs[1] 小车速度（米 / 秒，正 = 往右）
  obs[2] 杆的角度（弧度，正 = 往右倒；超过 ±12°，也就是 ±0.21，就算倒了）
  obs[3] 杆的角速度（弧度 / 秒，正 = 正在往右倒）
动作只有两个：0 = 往左推一下，1 = 往右推一下（每次 10 牛，推 0.02 秒）。
"""

from __future__ import annotations


def random_policy(obs, rng) -> int:
    """随机乱推：不看状态，一半概率往左、一半概率往右。"""
    return int(rng.integers(2))


# ---------- 第 1 课：你来写 ----------

def rule_policy(obs, rng=None) -> int:
    """你写的规则：看 obs 决定往左推（返回 0）还是往右推（返回 1）。rng 用不到，留着是为了和随机策略长得一样。

    见 docs/L01_cartpole.md 第 3 步。
    """
    raise NotImplementedError("第 1 课：你来写，见 docs/L01_cartpole.md 第 3 步")
