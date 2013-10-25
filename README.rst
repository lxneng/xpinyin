xpinyin
==========

.. image:: https://travis-ci.org/lxneng/xpinyin.png?branch=master
   :target: https://travis-ci.org/tangsty/xpinyin

.. image:: https://pypip.in/d/xpinyin/badge.png
        :target: https://crate.io/packages/xpinyin/

translate chinese hanzi to pinyin by python, inspired by flyerhzm’s
`chinese\_pinyin`_ gem

Install
----------

::

    pip install xpinyin
    not supported yet!

Usage
-----

::

    In [1]: from xpinyin import Pinyin

    In [2]: p = Pinyin()

    In [3]: p.get_pinyin(u"上海")
    Out[3]: 'shanghai'

    In [4]: p.get_pinyin(u"上海", '-')
    Out[4]: 'shang-hai'

    In [5]: p.get_pinyin(u"上海", ' ')
    Out[5]: 'shang hai'

    In [6]: p.get_initials(u"上")
    Out[6]: 'S'

请输入utf8编码汉字

.. _chinese\_pinyin: https://github.com/flyerhzm/chinese_pinyin
