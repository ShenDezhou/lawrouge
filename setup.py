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
===============

* 支持英文文本摘要测评, lawrouge.FoldersRouge(isChinese=False) 方法接受语言参数: isChinese是否为中文


代码示例：

```python
files_rouge = lawrouge.FoldersRouge(isChinese=False)
scores = files_rouge.get_scores(pred_list, gold_list, avg=True)
print(scores)
weighted_f1 = 0.2*scores['rouge-1']['f'] + 0.4*scores['rouge-2']['f']+ 0.4*scores['rouge-l']['f']
print('weighted F1-score:', weighted_f1)
```


版本说明
======================

* 1.2.0: 修复英文摘要测评计算方法中的缺陷。


"""

setup(name='lawrouge',
      version='1.2.0',
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
