#!/usr/bin/env python
# encoding: utf-8
"""
Created by Eric Lo on 2010-05-20.
Copyright (c) 2010 __lxneng@gmail.com__. http://lxneng.com All rights reserved.
"""
class Pinyin():
    def __init__(self, data_path='./Mandarin.dat'):
        self.dict = {}
        for line in open(data_path):
            k, v = line.split('\t')
            self.dict[k] = v
        self.splitter = ''	
    def get_pinyin(self, chars="你好吗"):
        chars = chars.decode("utf8")
        result = []
        for char in chars:
            key = "%X" % ord(char)
            try:
                result.append(self.dict[key].split(" ")[0].strip()[:-1].lower())
            except:
                result.append(char)
        return self.splitter.join(result)
    def get_initials(self, char='你'):
        char = char.decode("utf8")
        try:
            return self.dict["%X" % ord(char)].split(" ")[0][0]
        except:
            return char
