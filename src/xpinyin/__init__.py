#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

class Pinyin(object):
    '''
    xPinyin
    =======
    Translate chinese hanzi to pinyin by python, inspired by flyerhzm’s
    `chinese\_pinyin`_ gem.

    Usage
    -----
    ::
        In [1]: from xpinyin import Pinyin
        In [2]: p = Pinyin()
        In [3]: p.get_pinyin(u"上海")
        Out[3]: 'shanghai'
        In [4]: p.get_initials(u"上")
        Out[4]: 'S'
    Aforementioned methods take Unicode arguments.
    
    Credits
    -------
    .. _chinese\_pinyin: https://github.com/flyerhzm/chinese_pinyin
    
    Enhanced by Tslmy: https://github.com/tslmy/xpinyin
    
    新特征 by Tslmy
    ------
    * 对于“我的[1]还在吗？”这样的字符串，输出结果为“wo de [1] hai zai ma ？”而非“wo de [ 1 ] hai zai ma ？ ”，这在字符串匹配时十分有用。
    
    * 对于多音字，只读取第一个读音，减小了内存占用。
    
    * 加入了“with_tone”参数来控制get_pinyin方法是否返回包含读音（“一、二、三、四声”，以数字表示）的拼音。
    
    * 可通过“to_lower”参数来控制get_pinyin方法返回小写的拼音（关掉即为大写）。
        
    '''
    default_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'Mandarin.dat')
    def __init__(self, data_path = default_data_path):
        '''Initialization: Opens the database, reads in all the relationship.
        Takes one argument: "data_path" -- the absolute path of the data file.'''
        self.dict = {}#这里存放汉字的Unicode四位数字字符串与拼音的对应关系
        for line in open(data_path):
            k, v = line.split('\t')
            self.dict[k] = unicode(v.split(' ')[0].strip())
            #“[0]”是为了只选择第一项拼音（多音字的处理）

    def get_pinyin(self, chars=u'你好', splitter=u'', with_tone=True, to_lower=True):
        #result = []
        result=''
        no_splitter_before = False
        for char in chars:
            key = "%X" % ord(char)#把Unicode字符转换成数字，再把数字转换成数字字符串。
            try:
                if with_tone:
                    this_pinyin = self.dict[key]
                else:#不需“读音位”
                    this_pinyin = self.dict[key][:-1]#-1：去掉数字读音位
            except KeyError:
                result += char
                no_splitter_before = True
            else:
                if no_splitter_before:
                    no_splitter_before = False
                    result += splitter
                result += this_pinyin+splitter
        if to_lower:
            result = result.lower()
        return unicode(result)

    def get_initials(self, char=u'你'):
        try:
            return self.dict["%X" % ord(char)][0]
        except:
            return char
