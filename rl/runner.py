"""跑回合：让一个策略在环境里从头玩到结束，数它拿了多少奖励。

这是所有强化学习代码最外面的那一圈：重置 → 看状态 → 选动作 → 环境走一步、给奖励 → 结束了没有。
以后学的 Q-learning、DQN、PPO，都是在这一圈里面加“从奖励里学”。
"""

from __future__ import annotations

import gymnasium as gym
import numpy as np

X_LIMIT_M = 2.4      # 小车离轨道中间超过 2.4 米就算出轨


def run_episode(env, policy, seed: int) -> dict:
    """玩一回合：同一个种子，开局一模一样，随机策略的骰子也一模一样，所以结果能复现。"""
    obs, info = env.reset(seed=seed)
    rng = np.random.default_rng(seed)
    total_reward = 0.0
    steps = 0
    while True:
        action = policy(obs, rng)                                    # ① 看状态，选动作
        obs, reward, terminated, truncated, info = env.step(action)  # ② 环境走一步：给新状态和这一步的奖励
        total_reward += reward                                       # ③ 记奖励（倒立摆：每撑住一步 +1）
        steps += 1
        if terminated or truncated:                                  # ④ 结束：terminated = 失败了，truncated = 时间到（满 500 步）
            break
    if terminated and abs(obs[0]) > X_LIMIT_M:
        why = "小车出轨"
    elif terminated:
        why = "杆倒了"
    else:
        why = "撑满 500 步"
    return {"seed": seed, "steps": steps, "return": total_reward, "why": why}


def evaluate(policy, n_episodes: int = 20, render: bool = False) -> list[dict]:
    """同一个策略玩 n 回合（种子 0、1、2……），每回合一行结果。render = True 时开窗口看。"""
    env = gym.make("CartPole-v1", render_mode="human" if render else None)
    rows = []
    try:
        for seed in range(n_episodes):
            rows.append(run_episode(env, policy, seed))
    finally:
        env.close()
    return rows
