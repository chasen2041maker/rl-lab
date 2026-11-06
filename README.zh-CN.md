# rl-lab：从零学强化学习

[English](README.md) | 中文

我在学校学过神经网络（CNN、RNN、Transformer、NLP），学的都是**有标准答案**的监督学习。这个仓库从零学另一类问题：**没人告诉你每一步该怎么做，只在后面告诉你结果好不好**。

做法：每一课先跑、看结果，再讲原理；核心算法（Q-learning、DQN、策略梯度、PPO）自己从零手写，最后再和现成库比。全部在笔记本 CPU 上跑，用 [Gymnasium](https://gymnasium.farama.org/) 的小环境。

## 课表

13 课，每课一两次坐下，一周最多两次，大约 3–4 个月。每课讲到两层“为什么”：**直觉**（这个设计解决什么毛病，去掉它跑一遍看会坏成什么样）和**推导**（核心公式几行推出来，每一步配实跑的数）；严格的收敛证明只讲结论和条件。

| 课 | 环境 | 学什么 | 状态 |
| --- | --- | --- | --- |
| 1 | 倒立摆 CartPole | 环境、状态、动作、奖励、策略、回报；自己写规则当策略 | ✅ 22 → 41 → 199 → 500 步 |
| 2 | 10 台老虎机 | 探索还是利用（ε-贪心） | 下一课 |
| 3 | 冰湖格子世界（规则全知道） | 价值迭代：贝尔曼方程最直接的样子 | |
| 4 | 冰湖 / 悬崖 | 表格 Q-learning、折扣、学习率 | |
| 5 | 悬崖 | SARSA vs Q-learning：贴着悬崖走还是绕远 | |
| 6 | 格子世界 | Dyna：学一个小“世界模型”，在脑子里演练 | |
| 7 | 倒立摆 | DQN：神经网络代替表格、经验回放、目标网络 | |
| 8 | 倒立摆 | 策略梯度 REINFORCE | |
| 9 | 登月 LunarLander | Actor-Critic → PPO | |
| 10 | 单摆 Pendulum | 连续动作：SAC | |
| 11 | 自己设计奖励 | 奖励写错了，模型怎么钻空子 | |
| 12 | 自己写的 vs stable-baselines3 | 多种子对比，怎么判断谁真的更好 | |
| 13 | 大模型里的强化学习 | RLHF、GRPO 在干什么，小例子跑一遍 | |

**13 课之后：项目期（约半年）**：读并复现 5 篇奠基论文的关键结果（DQN、PPO、SAC、InstructGPT、DeepSeek-R1），做一个真项目（比如在 MetaDrive 里用强化学习从零练一个司机，和模仿学习练出来的比一场）。

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
