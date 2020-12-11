import os.path
import re
from typing import List, Optional

from xpinyin.combs import get_combs

PinyinToneMark = {
    0: "aoeiuv\u00fc",
    1: "\u0101\u014d\u0113\u012b\u016b\u01d6\u01d6",
    2: "\u00e1\u00f3\u00e9\u00ed\u00fa\u01d8\u01d8",
    3: "\u01ce\u01d2\u011b\u01d0\u01d4\u01da\u01da",
    4: "\u00e0\u00f2\u00e8\u00ec\u00f9\u01dc\u01dc",
}


class Pinyin:
    """translate chinese hanzi to pinyin by python, inspired by flyerhzm’s
    `chinese_pinyin`_ gem

    usage
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

    请输入utf8编码汉字
    .. _chinese_pinyin: https://github.com/flyerhzm/chinese_pinyin
    """

    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'Mandarin.dat')

    def __init__(self, data_path=data_path):
        self.dict = {}
        with open(data_path) as f:
            for line in f:
                k, v = line.split('\t')
                self.dict[k] = v.rstrip()

    @staticmethod
    def decode_pinyin(s):
        s = s.lower()
        r = ""
        t = ""
        for c in s:
            if "a" <= c <= 'z':
                t += c
            elif c == ':':
                assert t[-1] == 'u'
                t = t[:-1] + "\u00fc"
            else:
                if '0' <= c <= '5':
                    tone = int(c) % 5
                    if tone != 0:
                        m = re.search("[aoeiuv\u00fc]+", t)
                        if m is None:
                            # pass when no vowels find yet
                            t += c
                        elif len(m.group(0)) == 1:
                            # if just find one vowels, put the mark on it
                            t = t[:m.start(0)] \
                                + PinyinToneMark[tone][PinyinToneMark[0].index(m.group(0))] \
                                + t[m.end(0):]
                        else:
                            # mark on vowels which search with "a, o, e" one by one
                            # when "i" and "u" stand together, make the vowels behind
                            for num, vowels in enumerate(("a", "o", "e", "ui", "iu")):
                                if vowels in t:
                                    t = t.replace(vowels[-1], PinyinToneMark[tone][num])
                                    break
                r += t
                t = ""
        r += t
        return r

    @staticmethod
    def convert_pinyin(word, convert):
        if convert == 'capitalize':
            return word.capitalize()
        if convert == 'lower':
            return word.lower()
        if convert == 'upper':
            return word.upper()

    def get_pinyins(self, chars: str, splitter: str = '-',
                    tone_marks: Optional[str] = None, convert: str = 'lower', n: int = 10) -> List[str]:
        """
        Get All pinyin combinations given all possible readings of each character.
        The number of combinations is limited par default to 10 to avoid exponential explosion on long texts.
        """
        all_pinyin_options = []  # a list of lists that we'll fill with all pinyin options for each character
        flag = 1  # in the list (otherwise, probably not a Chinese character)
        for char in chars:
            key = "%X" % ord(char)
            if key not in self.dict:
                if flag == 1:
                    all_pinyin_options.append([char])  # add as is
                else:
                    all_pinyin_options[-1][-1] += char  # add to previous sequence of non Chinese chars
                flag = 0  # within a sequence of non Chinese characters
            else:
                if tone_marks is None:  # in this case we may have duplicates if the variations differ just by the tones
                    char_py_options = []
                    for v in self.dict[key].split():
                        if v[0:-1] not in char_py_options:  # we remove the tone mark while we're at it
                            char_py_options.append(v[0:-1])
                else:
                    char_py_options = self.dict[key].split()
                last = 1 if n == 1 else len(char_py_options)
                if tone_marks == 'marks':
                    char_options = [Pinyin.decode_pinyin(o) for o in char_py_options[0:last]]
                else:  # 'numbers' or None
                    char_options = [o for o in char_py_options[0:last]]

                all_pinyin_options.append([Pinyin.convert_pinyin(c, convert) for c in char_options])
                flag = 1

        return get_combs(options=all_pinyin_options, splitter=splitter, n=n)

    def get_pinyin(self, chars: str, splitter: str = '-',
                   tone_marks=None, convert: str = 'lower') -> str:

        return self.get_pinyins(chars, splitter=splitter, tone_marks=tone_marks, convert=convert, n=1)[0]

    def get_initial(self, char='你'):
        try:
            return self.dict["%X" % ord(char)].split(" ")[0][0]
        except KeyError:
            return char

    def get_initials(self, chars='你好', splitter='-'):
        result = []
        flag = 1
        for char in chars:
            try:
                result.append(self.dict["%X" % ord(char)].split(" ")[0][0])
                flag = 1
            except KeyError:
                if flag:
                    result.append(char)
                else:
                    result[-1] += char

        return splitter.join(result)
