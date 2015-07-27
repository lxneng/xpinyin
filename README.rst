xpinyin
==========

.. image:: https://img.shields.io/travis/lxneng/xpinyin.svg
    :target: https://travis-ci.org/lxneng/xpinyin

.. image:: https://img.shields.io/pypi/v/xpinyin.svg
    :target: https://pypi.python.org/pypi/xpinyin/

.. image:: https://img.shields.io/pypi/dm/xpinyin.svg
    :target: https://pypi.python.org/pypi/xpinyin/

translate chinese hanzi to pinyin by python, inspired by flyerhzm’s
`chinese\_pinyin`_ gem

Install
----------

::

    pip install xpinyin


Usage
-----

::

    >>> from xpinyin import Pinyin
    >>> p = Pinyin()
    >>> # default splitter is `-`
    >>> p.get_pinyin(u"上海")
    'shang-hai'
    >>> # show tone marks
    >>> p.get_pinyin(u"上海", show_tone_marks=True)
    'shàng-hǎi'
    >>> # remove splitter
    >>> p.get_pinyin(u"上海", '')
    'shanghai'
    >>> # set splitter as whitespace
    >>> p.get_pinyin(u"上海", ' ')
    'shang hai'
    >>> p.get_initial(u"上")
    'S'
    >>> p.get_initials(u"上海")
    'S-H'
    >>> p.get_initials(u"上海", u'')
    'SH'
    >>> p.get_initials(u"上海", u' ')
    'S H'

请输入utf8编码汉字

.. _chinese\_pinyin: https://github.com/flyerhzm/chinese_pinyin
