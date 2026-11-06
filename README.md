# rl-lab: reinforcement learning from zero

English | [中文](README.zh-CN.md)

At university I learned neural networks (CNN, RNN, Transformer, NLP), all of it supervised learning, where every example comes with the right answer. This repository is where I learn the other kind of problem from scratch: nobody tells you what to do at each step, you only find out later whether it went well.

How I work here: in every lesson I run something and look at the result first, then learn the theory. I write the core algorithms myself (Q-learning, DQN, policy gradient, PPO) and compare them with an off-the-shelf library at the end. Everything runs on a laptop CPU with small [Gymnasium](https://gymnasium.farama.org/) environments.

## Lessons

13 lessons, one or two sittings each, at most two a week: about 3-4 months. Each lesson covers two kinds of "why": the intuition (what problem a design choice fixes; remove it and watch what breaks) and the derivation (the core formula in a few lines, every step checked against numbers from a real run). Convergence proofs are stated with their conditions, not proved.

| # | Environment | Topic | Status |
| --- | --- | --- | --- |
| 1 | CartPole | environment, state, action, reward, policy, return; a hand-written rule as the policy | done: 22 → 41 → 199 → 500 steps |
| 2 | 10-armed bandit | exploration vs exploitation (epsilon-greedy) | |
| 3 | FrozenLake with a known model | value iteration: the Bellman equation at its plainest | |
| 4 | FrozenLake / CliffWalking | tabular Q-learning, discounting, learning rate | |
| 5 | CliffWalking | SARSA vs Q-learning: hug the cliff or take the long way | |
| 6 | grid world | Dyna: learn a small world model and rehearse in it | |
| 7 | CartPole | DQN: a network instead of a table, replay buffer, target network | |
| 8 | CartPole | policy gradient (REINFORCE) | |
| 9 | LunarLander | actor-critic, then PPO | |
| 10 | Pendulum | continuous actions: SAC | |
| 11 | my own reward | how a model exploits a badly written reward | |
| 12 | mine vs stable-baselines3 | multi-seed comparison: telling a real improvement from noise | |
| 13 | RL for language models | what RLHF and GRPO do, on a small example | |

**After lesson 13: a project phase (about six months).** Reproduce the key results of five foundational papers (DQN, PPO, SAC, InstructGPT, DeepSeek-R1) and build one real project, for example training a driver from scratch with RL in MetaDrive and racing it against one trained by imitation.

Lesson notes are in `docs/` (Chinese); progress and the numbers from each lesson are in [PROGRESS.md](PROGRESS.md).

## Quick start

```text
conda create -n rl python=3.11 -y
conda activate rl
python -m pip install -r requirements.txt
python -m labs.l01_cartpole            # lesson 1: random pushes vs my rule
python -m labs.l01_cartpole --show     # watch it in a window
python -m pytest -q
```

## Layout

```text
rl/        core code: policies, the episode loop; later Q-learning, DQN, PPO (core parts written by hand)
labs/      one experiment script per lesson
tests/     tests (numbers checked against real runs)
docs/      lesson notes
```
