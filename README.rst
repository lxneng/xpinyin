xpinyin
==========

.. image:: https://github.com/lxneng/xpinyin/workflows/CI/badge.svg
   :target: https://github.com/lxneng/xpinyin/actions?query=workflow%3ACI

.. image:: https://img.shields.io/travis/lxneng/xpinyin.svg
    :target: https://travis-ci.org/lxneng/xpinyin

.. image:: https://img.shields.io/pypi/v/xpinyin.svg
    :target: https://pypi.python.org/pypi/xpinyin/

.. image:: https://img.shields.io/pypi/dm/xpinyin.svg
    :target: https://pypi.python.org/pypi/xpinyin/


Translate Chinese hanzi to pinyin (拼音) by Python, 汉字转拼音


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
    >>> p.get_pinyin("上海")
    'shang-hai'
    >>> # show tone marks
    >>> p.get_pinyin("上海", tone_marks='marks')
    'shàng-hǎi'
    >>> p.get_pinyin("上海", tone_marks='numbers')
    >>> 'shang4-hai3'
    >>> # remove splitter
    >>> p.get_pinyin("上海", '')
    'shanghai'
    >>> # set splitter as whitespace
    >>> p.get_pinyin("上海", ' ')
    'shang hai'
    >>> p.get_initial("上")
    'S'
    >>> p.get_initials("上海")
    'S-H'
    >>> p.get_initials("上海", '')
    'SH'
    >>> p.get_initials("上海", ' ')
    'S H'
    >>> # get_initials with retroflex, #39
    >>> p.get_initials("上海", splitter='-', with_retroflex=True)
    'SH-H'
    >>> # get combinations of the multiple readings of the characters
    >>> p.get_pinyins('模型', splitter=' ', tone_marks='marks')
    ['mó xíng', 'mú xíng']
    >>> p.get_pinyins('模样', splitter=' ', tone_marks='marks')
    ['mó yáng', 'mó yàng', 'mó xiàng', 'mú yáng', 'mú yàng', 'mú xiàng']
