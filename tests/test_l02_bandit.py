"""第 2 课测试：老虎机、平均值更新、ε-贪心。

数字是云端实跑核对过的（种子 0）：第 0 局真正最好的是第 9 台（中奖率 0.935）；随便拉 1000 次赢 551 次，开天眼赢 942 次。
ε = 0（只利用）时第 0 局一直拉第 8 台（0.544），1000 次赢 560 次，第 9 台一次都没试过；ε = 0.1 时找到第 9 台，拉了 880 次，赢 897 次。
"""

import numpy as np
import pytest

from rl.bandit import SlotMachines, argmax_random_tie, choose, play, play_baseline, update


def test_machines_and_baselines():
    m = SlotMachines(0)
    assert m.best_arm == 9 and m.p[9] == pytest.approx(0.935, abs=1e-3)
    assert play_baseline("random", 0) == 551
    assert play_baseline("oracle", 0) == 942


def test_argmax_random_tie_spreads_over_ties():
    """开局全是 0 时，不能永远只挑第 0 台。"""
    rng = np.random.default_rng(0)
    picks = {argmax_random_tie(np.zeros(10), rng) for _ in range(200)}
    assert picks == set(range(10))
    assert argmax_random_tie(np.array([0.1, 0.9, 0.3]), rng) == 1


def _written():
    try:
        update(np.zeros(2), np.zeros(2, dtype=int), 0, 1)
        choose(np.zeros(2), 0.0, np.random.default_rng(0))
    except NotImplementedError:
        pytest.skip("update / choose 还没写")


def test_update_is_running_mean():
    """拉第 0 台 4 次，中、没中、中、中：平均就是 3 / 4 = 0.75，次数 4；别的台不动。"""
    _written()
    Q = np.zeros(3)
    N = np.zeros(3, dtype=int)
    for r in (1, 0, 1, 1):
        update(Q, N, 0, r)
    assert Q[0] == pytest.approx(0.75) and N[0] == 4
    assert Q[1] == 0 and N[1] == 0


def test_choose_explore_and_exploit():
    """ε = 0：永远挑平均最高的；ε = 1：每台都会被挑到。"""
    _written()
    rng = np.random.default_rng(0)
    Q = np.array([0.2, 0.8, 0.5])
    assert {choose(Q, 0.0, rng) for _ in range(50)} == {1}
    assert {choose(Q, 1.0, rng) for _ in range(200)} == {0, 1, 2}


def test_greedy_gets_stuck_epsilon_finds_the_best():
    """第 0 局：只利用的一直拉第 8 台、赢 560 次；ε = 0.1 找到第 9 台，赢 897 次。"""
    _written()
    greedy = play(0.0, seed=0)
    assert greedy["wins"] == 560 and greedy["N"][8] == 1000 and greedy["N"][9] == 0
    explore = play(0.1, seed=0)
    assert explore["wins"] == 897 and explore["N"][9] == 880
