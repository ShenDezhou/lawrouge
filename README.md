lawrouge
===========================

"法摘"中英文摘要评价器：做最好的 Python 中英文摘要评价组件

"lawrouge" (Law-rouge) Chinese and English text summary evaluation metric: built to
be the best Python Multilingual Text Summary Evaluation module.

完整文档见 ``README.md``

GitHub: https://github.com/ShenDezhou/lawrouge

特点
======================

-  支持两种种摘要评价模式：
   -  中文模式，支持中文文本摘要评价（默认）；
   -  英文模式（西、葡、法），支持英文以及西、葡、法等语言文本摘要评价;
-  支持繁体文本

在线演示： ShenDezhou

安装说明
======================

代码对 Python 2/3 均兼容

-  全自动安装： ``easy_install lawrouge`` 或者 ``pip install lawrouge`` / ``pip3 install lawrouge``
-  半自动安装：先下载 https://pypi.python.org/pypi/lawrouge/ ，解压后运行
   python setup.py install
-  手动安装：将 lawrouge 目录放置于当前目录或者 site-packages 目录
-  通过 ``import lawrouge`` 来引用

使用说明
======================

* 支持英文文本摘要测评, 
    -  lawrouge.Rouge(isChinese=False) 方法接受语言参数: 
    -  isChinese: True中文, False为英文（西班牙、意大利等西方语系） 




中文摘要
====================================

* 比较两组字符串：

```
rouge = lawrouge.Rouge()
scores = rouge.get_scores(["他是清华大学计算机科学与技术系"], ["计算机科学与技术专业"], avg=2)
print(scores)
```


* 比较两组文件名（比较文件名给定文件内容）：


```
files_rouge = lawrouge.FoldersRouge()  
scores = files_rouge.get_scores(pred_list, gold_list, avg=2)  
print('weighted score: ', scores)
```

* 结果输出:


```
weighted F1-score: 0.9999999949999998
```


English Summary
======================

Support English text summary evaluation, string version: lawrouge.Rouge(isChinese=False) and file name version: lawrouge.FoldersRouge(isChinese=False).

Compare two lists of strings：

```
rouge = lawrouge.Rouge(isChinese=False)
scores = rouge.get_scores(["He gets the Master Degree of Computer Science and Technology"], ["in the Department of Computer Science and Technology"], avg=2)
print(scores)
```


Compare two lists of files(pred_list, gold_list are file path of two corpus.)：

```
rouge = lawrouge.FoldersRouge(isChinese=False)
scores = rouge.get_scores(pred_list, gold_list, avg=2) 
print('weighted score: ', scores)
```

Result Output:

```
weighted F1-score: 0.9999999949999998
```

内核类构造方法
===========================

* 下面对核心Rouge类的构造参数exclusive说明：该值影响最长公共子串匹配的计算方式。

-  exclusive=True表明将文本表示为字的集合，
-  exclusive=False（默认值）表明将文本表示为列表，在计算最长公共子串时，合并不同句子的最长串时，会将每个预测句子中与标准摘要句重合部分计入最长公共子串中。
因此，以下面示例为例，则最长公共子串为  LCS=他是清华大学计算机科学与技术系计算机科学与技术  ，而在字集合表示下，则重复字会消去。因为会出现LCS大于标准句的情况，进而可能会出现R值大于1的情形。

代码示例：

```
rouge = lawrouge.Rouge(exclusive=True)
scores = rouge.get_scores(["他是清华大学计算机科学与技术系。计算机科学与技术专业。"], ["他是清华大学计算机科学与技术系。"],  avg=1)
print(scores)
```

内核方法说明
===========================

* 下面对核心方法get_score中avg参数进行说明：该值影响数据处理以及返回值。

-  avg=0表明用户传入的两个子串计算Rouge值直接返回列表。
-  avg=1对用户传入两个子串进行按照句子分割符拆分后，计算Rouge值，并取平均返回。
-  avg=2除上述处理外，还将3种Rouge得分加权求和后返回。


版本说明
======================================

* 1.2.2: 修复英文摘要测评计算方法中的缺陷。

* 1.3.1: 修复英文摘要测评使用方法中的缺陷。

* 2.0.0: 增加对最长公共子串匹配的说明。


常见问题
==========================

* 1.对于两个句子，应如何调用？
  
* 答：参见内核类构造方法和内核方法说明


