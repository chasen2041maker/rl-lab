"""第 2 课：10 台老虎机（多臂老虎机）。

每台中奖概率不一样，开局随机定好，玩家看不到。拉一次：中奖得 1，不中得 0。
玩家只能一台一台去试，边试边记每台的平均中奖率，决定下一次拉哪台。
难处：一直拉目前看着最好的那台（利用），可能错过真正最好的；一直换着试（探索），又浪费机会。
"""

from __future__ import annotations

import numpy as np

N_ARMS = 10


class SlotMachines:
    """一组 10 台老虎机。种子定了，每台的中奖概率和每次开奖都定了，结果能复现。"""

    def __init__(self, seed: int, n_arms: int = N_ARMS):
        rng = np.random.default_rng(seed)
        self.p = rng.uniform(0.0, 1.0, n_arms)          # 每台真实的中奖概率（玩家看不到）
        self.n_arms = n_arms
        self.best_arm = int(np.argmax(self.p))          # 真正最好的那台（只有出题人知道）
        self.rng = np.random.default_rng(seed + 10_000)  # 开奖用的骰子

    def pull(self, a: int) -> int:
        """拉第 a 台：按它的中奖概率开奖，中了返回 1，没中返回 0。"""
        return int(self.rng.random() < self.p[a])


def argmax_random_tie(Q, rng) -> int:
    """挑 Q 最大的那台；几台一样大时随便挑一台（不然开局全是 0，就永远只挑第 0 台）。"""
    best = Q.max()
    candidates = np.flatnonzero(Q == best)
    return int(rng.choice(candidates))


# ---------- 第 2 课：你来写 ----------

def update(Q, N, a: int, r: int) -> None:
    """拉了第 a 台、得到 r（1 或 0）：这台拉过的次数 N[a] 加 1，平均中奖率 Q[a] 往 r 挪一点。

    挪多少：Q[a] += (r - Q[a]) / N[a]。见 docs/L02_bandit.md 第 3 步。不用 return，直接改 Q 和 N。
    """
    raise NotImplementedError("第 2 课：你来写，见 docs/L02_bandit.md 第 3 步")


def choose(Q, epsilon: float, rng) -> int:
    """ε-贪心：选下一次拉哪台。

    掷一次骰子 rng.random()（0 到 1 之间的随机数）：
      小于 epsilon → 探索：随便挑一台，rng.integers(len(Q))
      否则         → 利用：挑目前平均中奖率最高的那台，argmax_random_tie(Q, rng)
    见 docs/L02_bandit.md 第 4 步。
    """
    raise NotImplementedError("第 2 课：你来写，见 docs/L02_bandit.md 第 4 步")


# ---------- 玩一局（助手写好的） ----------

def play(epsilon: float, seed: int, steps: int = 1000, trace: bool = False) -> dict:
    """玩一局：一组新的老虎机（seed 定），拉 steps 次。返回赢了几次、拉最好那台的比例；trace = True 时把每一次都记下来。"""
    machines = SlotMachines(seed)
    rng = np.random.default_rng(seed + 20_000)          # 玩家自己的骰子（探索时用）
    Q = np.zeros(machines.n_arms)                       # 每台目前的平均中奖率（玩家心里的估计，开局都当 0）
    N = np.zeros(machines.n_arms, dtype=int)            # 每台拉过几次
    wins = 0
    best_pulls = 0
    log = []
    for t in range(steps):
        a = choose(Q, epsilon, rng)                     # ① 选一台
        r = machines.pull(a)                            # ② 拉，开奖
        update(Q, N, a, r)                              # ③ 记下来，更新这台的平均
        wins += r
        if a == machines.best_arm:
            best_pulls += 1
        if trace:
            log.append((t + 1, a, r, round(float(Q[a]), 3)))
    return {"wins": wins, "best_share": best_pulls / steps, "Q": Q, "N": N, "p": machines.p,
            "best_arm": machines.best_arm, "log": log}


def play_baseline(kind: str, seed: int, steps: int = 1000) -> int:
    """两个参照：random = 每次随便拉一台；oracle = 开了天眼，每次都拉真正最好的那台。返回赢了几次。"""
    machines = SlotMachines(seed)
    rng = np.random.default_rng(seed + 20_000)
    wins = 0
    for _ in range(steps):
        if kind == "random":
            a = int(rng.integers(machines.n_arms))
        else:
            a = machines.best_arm
        wins += machines.pull(a)
    return wins
