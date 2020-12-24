# -*- coding: utf-8 -*-
from distutils.core import setup
LONGDOC = """
lawrouge
===========================

"法摘"中英文摘要评价：做最好的 Python 中英文摘要评价组件

"lawrouge" (Law-rouge) Chinese and English text summary evaluation metric: built to
be the best Python Multilingual Text Summary Evaluation module.

完整文档见 ``README.md``

GitHub: https://github.com/ShenDezhou/lawrouge

特点
=========================

-  支持中英文摘要测评模式
    
    -  中文模式
    -  英文模式
    -  THU 授权协议

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
=========================

* 支持英文文本摘要测评, lawrouge.Rouge(isChinese=False) 方法接受语言参数: isChinese是否为中文


代码示例：

```python
rouge = lawrouge.Rouge()
scores = rouge.get_scores(["他是清华大学计算机科学与技术系"], ["计算机科学与技术专业"], avg=2)
print(scores)
```


内核类构造方法
===========================


* 下面对核心Rouge类的构造参数exclusive说明：该值影响最长公共子串匹配的计算方式。


-  exclusive=True表明将文本表示为字的集合，

-  exclusive=False（默认值）表明将文本表示为列表，在计算最长公共子串时，合并不同句子的最长串时，会将每个预测句子中与标准摘要句重合部分计入最长公共子串中。因此，以下面示例为例，则最长公共子串为  LCS=他是清华大学计算机科学与技术系计算机科学与技术  ，而在字集合表示下，则重复字会消去。因为会出现LCS大于标准句的情况，进而可能会出现R值大于1的情形。


代码示例：


```python
rouge = lawrouge.Rouge(exclusive=True)
scores = rouge.get_scores(["他是清华大学计算机科学与技术系。计算机科学与技术专业。"], ["他是清华大学计算机科学与技术系。"],  avg=1)
print(scores)
```


内核方法说明
===========================


* 下面对核心方法get_score中avg参数进行说明：该值影响数据处理以及返回值。


-  avg=0表明用户传入的两个子串计算Rouge值，返回句子对Rouge评分列表。

-  avg=1对用户传入两个子串进行按照句子分割符拆分后，计算Rouge值，并取平均返回。

-  avg=2除上述处理外，还将3种Rouge得分加权求和后返回。


版本说明
============================


* 1.2.0: 修复英文摘要测评计算方法中的缺陷。

* 1.3.1: 修复英文摘要测评使用方法中的缺陷。

* 2.0.0: 增加对最长公共子串匹配的说明。


"""

setup(name='lawrouge',
      version='2.0.0',
      description='Chinese Text Summary Evaluation Utilities',
      long_description=LONGDOC,
      author='Shen Dezhou',
      author_email='tsinghua9boy@sina.com',
      url='https://github.com/ShenDezhou/lawrouge',
      license="MIT",
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='NLP,summary,Chinese text summarization metric',
      packages=['lawrouge'],
      package_dir={'lawrouge':'lawrouge'},
      package_data={'lawrouge':['*.*']}
)
