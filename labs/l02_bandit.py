"""第 2 课实验：10 台老虎机，探索还是利用。

每种玩法玩 200 局（每局一组新的老虎机，种子 0–199），每局拉 1000 次，看平均赢几次。

运行（在仓库根目录）：
    python -m labs.l02_bandit            两个参照（随便拉 / 开天眼）；你写好 update、choose 以后，再跑几种 ε
    python -m labs.l02_bandit --one 0    只玩第 0 局、ε = 0，看前 20 次拉了哪台、最后每台拉了几次
    python -m labs.l02_bandit --one 0.1  同上，ε = 0.1
"""

from __future__ import annotations

import sys

import numpy as np

from rl.bandit import choose, play, play_baseline, update

GAMES = 200
STEPS = 1000
EPSILONS = [0.0, 0.01, 0.1, 0.2, 0.5, 1.0]


def written() -> bool:
    """update 和 choose 写了没有：随便试一下，没写会抛 NotImplementedError。"""
    try:
        Q = np.zeros(3)
        N = np.zeros(3, dtype=int)
        update(Q, N, 0, 1)
        choose(Q, 0.0, np.random.default_rng(0))
        return True
    except NotImplementedError:
        return False


def baselines() -> None:
    random_wins = []
    oracle_wins = []
    for seed in range(GAMES):
        random_wins.append(play_baseline("random", seed, STEPS))
        oracle_wins.append(play_baseline("oracle", seed, STEPS))
    print(f"每局拉 {STEPS} 次，玩 {GAMES} 局，平均赢几次：")
    print(f"  随便拉（每次随便挑一台）      {np.mean(random_wins):6.1f}")
    print(f"  开天眼（每次都拉真正最好那台）{np.mean(oracle_wins):6.1f}")


def epsilon_table() -> None:
    print()
    print("ε（探索的比例）  平均赢几次  拉到最好那台的比例")
    for eps in EPSILONS:
        wins = []
        shares = []
        for seed in range(GAMES):
            res = play(eps, seed, STEPS)
            wins.append(res["wins"])
            shares.append(res["best_share"])
        print(f"  {eps:<5}           {np.mean(wins):7.1f}      {np.mean(shares) * 100:5.1f}%")


def one_game(eps: float) -> None:
    res = play(eps, seed=0, steps=STEPS, trace=True)
    print(f"第 0 局，ε = {eps}：前 20 次")
    print("  第几次  拉哪台  中没中  这台现在的平均")
    for t, a, r, q in res["log"][:20]:
        print(f"  {t:>4}    {a:>4}     {'中' if r else '没中'}     {q:.3f}")
    print()
    print("拉完 1000 次以后：")
    print("  第几台  真实中奖率（玩家看不到）  拉了几次  玩家估计的平均")
    for i in range(len(res["p"])):
        mark = "  ← 真正最好" if i == res["best_arm"] else ""
        print(f"  {i:>4}        {res['p'][i]:.3f}               {res['N'][i]:>5}      {res['Q'][i]:.3f}{mark}")
    print(f"一共赢了 {res['wins']} 次")


def main():
    if "--one" in sys.argv:
        if not written():
            print("先写好 rl/bandit.py 里的 update 和 choose（见 docs/L02_bandit.md）。")
            return
        eps = float(sys.argv[sys.argv.index("--one") + 1])
        one_game(eps)
        return
    baselines()
    if written():
        epsilon_table()
    else:
        print("\n你的 update、choose 还没写：打开 rl/bandit.py，见 docs/L02_bandit.md 第 3、4 步。")


if __name__ == "__main__":
    main()
