# rl-lab: reinforcement learning from zero

English | [中文](README.zh-CN.md)

At university I learned neural networks (CNN, RNN, Transformer, NLP), all of it supervised learning, where every example comes with the right answer. This repository is where I learn the other kind of problem from scratch: nobody tells you what to do at each step, you only find out later whether it went well.

How I work here: in every lesson I run something and look at the result first, then learn the theory. I write the core algorithms myself (Q-learning, DQN, policy gradient, PPO) and compare them with an off-the-shelf library at the end. Everything runs on a laptop CPU with small [Gymnasium](https://gymnasium.farama.org/) environments.

## Lessons

| # | Environment | Topic | Status |
| --- | --- | --- | --- |
| 1 | CartPole | environment, state, action, reward, policy, return; a hand-written rule as the policy | in progress |
| 2 | 10-armed bandit | exploration vs exploitation (epsilon-greedy) | |
| 3 | FrozenLake / CliffWalking | tabular Q-learning, discounting, the Bellman update | |
| 4 | CliffWalking | SARSA vs Q-learning | |
| 5 | CartPole | DQN: a network instead of a table, replay buffer, target network | |
| 6 | CartPole | policy gradient (REINFORCE) | |
| 7 | LunarLander | actor-critic, then PPO | |
| 8 | my own reward | how a model exploits a badly written reward | |
| 9 | mine vs stable-baselines3 | multi-seed comparison | |
| 10 | RL for language models | what RLHF and GRPO do (tentative) | |

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
