translate chinese hanzi to pinyin by python, inspired by flyerhzm's chinese_pinyin gem

## usage

    In [1]: from xpinyin import Pinyin
    
    In [2]: p = Pinyin()
    
    In [3]: p.get_pinyin(u"上海")
    Out[3]: 'shanghai'
    
    In [4]: p.get_initials(u"上")
    Out[4]: 'S'

请输入utf8编码汉字
