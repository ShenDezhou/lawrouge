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
=======================================

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

版本说明
======================================

* 1.2.2: 修复英文摘要测评计算方法中的缺陷。

* 1.3.0: 修复英文摘要测评使用方法中的缺陷。




