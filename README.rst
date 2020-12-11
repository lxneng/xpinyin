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
    >>> p.get_pinyin(u"上海", tone_marks='marks')
    'shàng-hǎi'
    >>> p.get_pinyin(u"上海", tone_marks='numbers')
    >>> 'shang4-hai3'
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
    >>> # get combinations of the multiple readings of the characters
    >>> p.get_pinyins(u'模型', splitter=u' ', tone_marks='marks')
    ['mó xíng', 'mú xíng']
    >>> p.get_pinyins(u'模样', splitter=u' ', tone_marks='marks')
    ['mó yáng', 'mó yàng', 'mó xiàng', 'mú yáng', 'mú yàng', 'mú xiàng']



请输入utf8编码汉字



.. _chinese\_pinyin: https://github.com/flyerhzm/chinese_pinyin
