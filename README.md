# Python

---

## 写在开始

&emsp;&emsp;本文档使用[Markdown](https://zh.wikipedia.org/wiki/Markdow)编写，笔者已有 Python 基础，这次学习不过是回顾一遍，查漏补缺,主要学习别人的实例，大体语法很简单，基本看一下实例就会了。写这篇文档也不期望会有谁看，大概率是记录自己的学习过程吧。不过不得不吐槽一下，Markdown 对中文的不友好，首行缩进一定要打&emsp，听说全角空格也行，但是我在 VScode 里好像不行，又懒得下 typora，所幸放弃。

## 关于 Python

&emsp;&emsp;Python 是一种比较简单的编程语言，可以说是目前唯一的超级语言。
其优缺点很明显：

- **可读性优秀**，可以说是最简单的编程语言，理解起来毫不费力，把符号去掉，你甚至有读自然语言的感觉。
- 兼具面向对象和函数式编程，**实用性广**。
- **可移植性**极强，各种主流系统都能运行。
- **编写效率高**，同样行数的代码，Python 能干的事比其他语言多得多，但是代码**执行效率低**。
- 最重要的是**开源**，社区群体庞大，生态优良，但因可选方法过多，往往容易出错。

## Python 之禅

&emsp;&emsp;老规矩，开始放上 Tim Peters 的 Python 之禅，这其中的道理，适用于任何语言。

**_Tim Peters:_**

*<p align="center">Beautiful is better than ugly.</p>*
*<p align="center">优美优于丑陋</p>*
*<p align="center">Explicit is better than implicit.</p>*
*<p align="center">明了优于隐晦</p>*
*<p align="center">Simple is better than complex.</p>*
*<p align="center">简单优于复杂</p>*
*<p align="center">Complex is better than complicated.</p>*
*<p align="center">复杂优于凌乱</p>*
*<p align="center">Flat is better than nested.</p>*
*<p align="center">扁平优于嵌套</p>*
*<p align="center">Sparse is better than dense.</p>*
*<p align="center">稀疏优于稠密</p>*
*<p align="center">Readability counts.</p>*
*<p align="center">可读性很重要</p>*
*<p align="center">Special cases aren't special enough to break the rules.</p>*
*<p align="center">特例不可违背这些原则</p>*
*<p align="center">Although practicality beats purity.</p>*
*<p align="center">尽管代码的实用性比规范性更重要</p>*
*<p align="center">Errors should never pass silently.</p>*
*<p align="center">错误绝不能被无故忽略</p>*
*<p align="center">Unless explicitly silenced.</p>*
*<p align="center">除非明确需要</p>*
*<p align="center">In the face of ambiguity, refuse the temptation to guess.</p>*
*<p align="center">如果面对模棱两可的逻辑，请不要瞎猜</p>*
*<p align="center">There should be one-- and preferably only one --obvious way to do it.</p>*
*<p align="center">应该找出一种，且最好只有一种，最显而易见的方法</p>*
*<p align="center">Although that way may not be obvious at first unless you're Dutch.</p>*
*<p align="center">尽管这种方法是无法一蹴而就的，除非你是荷兰人（意指Python创始人Guido van Rossum）</p>*
*<p align="center">Now is better than never.</p>*
*<p align="center">立刻就做好过永远不做</p>*
*<p align="center">Although never is often better than _right_ now.</p>*
*<p align="center">然而永远不做也好过闷头蛮干</p>*
*<p align="center">If the implementation is hard to explain, it's a bad idea.</p>*
*<p align="center">如果你的方法难以解释，它一定不是个好主意</p>*
*<p align="center">If the implementation is easy to explain, it may be a good idea.</p>*
*<p align="center">如果你的方法一目了然，那它可能是个好主意</p>*
*<p align="center">Namespaces are one honking great idea -- let's do more of those!</p>*
*<p align="center">命名空间是个很好的主意，让我们好好利用它吧！</p>*
