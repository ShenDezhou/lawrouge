# lawrouge
“法摘”中文文本摘要测评：做最好的 Python 文本中英文摘要测评组件

特点
====

-  支持两种种摘要评价模式：
   -  中文模式，支持中文文本摘要评价（默认）；
   -  英文模式，支持英文文本摘要评价,
-  支持繁体文本
-  THU 授权协议

在线演示： 

安装说明
========

代码对 Python 2/3 均兼容

-  全自动安装： ``easy_install lawrouge`` 或者 ``pip install lawrouge`` / ``pip3 install lawrouge``
-  半自动安装：先下载 https://pypi.python.org/pypi/lawrouge/ ，解压后运行
   python setup.py install
-  手动安装：将 lawrouge 目录放置于当前目录或者 site-packages 目录
-  通过 ``import lawrouge`` 来引用


算法
========

* Rouge-1、Rouge-2、Rouge-L作为摘要评价算法，以及三个评价的加权平均作为最终评价。

主要功能
=======

1. 中文摘要
--------

* `files_rouge.get_scores` 方法接受三个输入参数: 模型输出摘要文件列表、参考（标准）摘要文件列表、是否取平均

代码示例

```python
files_rouge = lawrouge.FoldersRouge()
scores = files_rouge.get_scores(pred_list, gold_list, avg=True)
print(scores)
weighted_f1 = 0.2*scores['rouge-1']['f'] + 0.4*scores['rouge-2']['f']+ 0.4*scores['rouge-l']['f']
print('weighted F1-score:', weighted_f1)
```

输出:

```
{'rouge-1': {'f': 0.9999999949999997, 'p': 1.0, 'r': 1.0}, 'rouge-2': {'f': 0.9999999949999997, 'p': 1.0, 'r': 1.0}, 'rouge-l': {'f': 0.9999999949999997, 'p': 1.0, 'r': 1.0}}
weighted F1-score: 0.9999999949999998
```

2. 英文摘要
----------------

* 支持英文文本摘要测评, lawrouge.FoldersRouge(isChinese=False) 方法接受语言参数; isChinese是否为中文.


代码示例：

```
files_rouge = lawrouge.FoldersRouge(isChinese=False)
scores = files_rouge.get_scores(pred_list, gold_list, avg=True)
print(scores)
weighted_f1 = 0.2*scores['rouge-1']['f'] + 0.4*scores['rouge-2']['f']+ 0.4*scores['rouge-l']['f']
print('weighted F1-score:', weighted_f1)
```

输出:

```
{'rouge-1': {'f': 0.9999999949999997, 'p': 1.0, 'r': 1.0}, 'rouge-2': {'f': 0.9999999949999997, 'p': 1.0, 'r': 1.0}, 'rouge-l': {'f': 0.9999999949999997, 'p': 1.0, 'r': 1.0}}
weighted F1-score: 0.9999999949999998
```

版本说明
=======

* 1.2.0: 修复英文计算方法中的缺陷。