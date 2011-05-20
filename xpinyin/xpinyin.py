#!/usr/bin/env python
# coding=utf-8

"""Translate chinese hanzi to pinyin by python
Created by Eric Lo on 2010-05-20.
Copyright (c) 2010 __lxneng@gmail.com__. http://lxneng.com All rights reserved.
"""

import os.path

VERSION = '0.2'


class Pinyin():
    """translate chinese hanzi to pinyin by python, inspired by flyerhzm’s
    `chinese\_pinyin`_ gem

    usage
    -----
    ::
        In [1]: from xpinyin import xpinyin
        In [2]: p = xpinyin.Pinyin()
        In [3]: p.get_pinyin(u"上海")
        Out[3]: 'shanghai'
        In [4]: p.get_initials(u"上")
        Out[4]: 'S'
    请输入utf8编码汉字
    .. _chinese\_pinyin: https://github.com/flyerhzm/chinese_pinyin
    """

    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), \
            'Mandarin.dat')

    def __init__(self):
        self.dict = {}
        for line in open(self.data_path):
            k, v = line.split('\t')
            self.dict[k] = v
        self.splitter = ''

    def get_pinyin(self, chars=u'你好'):
        result = []
        for char in chars:
            key = "%X" % ord(char)
            try:
                result.append(self.dict[key].split(" ")[0].strip()[:-1]\
                        .lower())
            except:
                result.append(char)
        return self.splitter.join(result)

    def get_initials(self, char=u'你'):
        try:
            return self.dict["%X" % ord(char)].split(" ")[0][0]
        except:
            return char
