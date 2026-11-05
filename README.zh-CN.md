# rl-lab：从零学强化学习

[English](README.md) | 中文

我在学校学过神经网络（CNN、RNN、Transformer、NLP），学的都是**有标准答案**的监督学习。这个仓库从零学另一类问题：**没人告诉你每一步该怎么做，只在后面告诉你结果好不好**。

做法：每一课先跑、看结果，再讲原理；核心算法（Q-learning、DQN、策略梯度、PPO）自己从零手写，最后再和现成库比。全部在笔记本 CPU 上跑，用 [Gymnasium](https://gymnasium.farama.org/) 的小环境。

## 课表

| 课 | 环境 | 学什么 | 状态 |
| --- | --- | --- | --- |
| 1 | 倒立摆 CartPole | 环境、状态、动作、奖励、策略、回报；自己写规则当策略 | 进行中 |
| 2 | 10 台老虎机 | 探索还是利用（ε-贪心） | |
| 3 | 冰湖 / 悬崖格子世界 | 表格 Q-learning、折扣、贝尔曼更新 | |
| 4 | 悬崖 | SARSA vs Q-learning | |
| 5 | 倒立摆 | DQN：神经网络代替表格、经验回放、目标网络 | |
| 6 | 倒立摆 | 策略梯度 REINFORCE | |
| 7 | 登月 LunarLander | Actor-Critic → PPO | |
| 8 | 自己设计奖励 | 奖励写错了，模型怎么钻空子 | |
| 9 | 自己写的 vs stable-baselines3 | 多种子对比 | |
| 10 | 大模型里的强化学习 | RLHF、GRPO 在干什么（待定） | |

每课的讲义在 `docs/`，进度和每课的数字在 [PROGRESS.md](PROGRESS.md)。

## 快速开始

```text
conda create -n rl python=3.11 -y
conda activate rl
python -m pip install -r requirements.txt
python -m labs.l01_cartpole            第 1 课：随机乱推 vs 你写的规则
python -m labs.l01_cartpole --show     开窗口看
python -m pytest -q                    跑测试
```

## 目录

```text
rl/        核心代码：策略、跑回合，以后的 Q-learning、DQN、PPO 都在这里（核心部分自己写）
labs/      每课的实验脚本
tests/     测试（数字都是实跑核对过的）
docs/      每课讲义
```
