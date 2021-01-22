概率图模型
================
wenxin Gao
2020/6/30

# 概率图模型

> 概率图模型提供了一种描述框架：将学习任务归结于计算变量分概率分布换句话说就是利用已知变量推测未知变量的条件分布。
> 假定关心变量集合Y，可观测变量集合为O.其他变量集合为R，生成式模型考虑联合分布概率P(Y,R,O),判别式模型考虑条件概率分布：P(Y,R|O),从P(Y,R,O)，P(Y,R|O)得到P(Y|O)。\[@西瓜书\]

生成式对联合分布建模，判别式对条件概率分布建模\~

**概率图**是一类用来表达向量相关关系的概率模型。用一个结点表示一个或者一组随机变量，结点之间的边表示变量之间的相关关系。

有两类：

  - 有向图模型/贝叶斯网络：有向无环图
  - 无向图模型/马尔可夫：无向图

## 隐马尔可夫模型HMM

是一种有向图模型的结构，主要用于时序建模和语音识别，自然语言处理。

### 变量

隐变量（状态变量）：

观测变量：

在任一一个时刻的取值，观测变量的取值仅仅依赖于状态变量==系统下一个时刻的状态仅仅由当前状态决定，不依赖与以往的任何状态

### 马尔可夫随机场MRF

马尔可夫网：无向图模型，图中每个结点表示表示一个或者一组向量，结点之间表示依赖关系。

马尔可夫随机场有一组势函数，也叫factor，这是定义在变量子集上的非负实函数，主要用于定义概率分布函数。

团：

### 条件随机场CRF

条件随机场处理的是条件概率也是使用团上的势函数来定义的

## 序列标注算法