#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

class PinyinTests(unittest.TestCase):
    def Pinyin(self, *a, **kw):
        from xpinyin import Pinyin

        return Pinyin(*a, **kw)

    def setUp(self):
        self.p = self.Pinyin()

    def test_get_pinyin_with_default_splitter(self):
        self.assertEqual(self.p.get_pinyin(u'上海'), u'shang-hai')

    def test_get_pinyin_with_splitter(self):
        self.assertEqual(self.p.get_pinyin(u'上海', splitter=u''), u'shanghai')

    def test_get_pinyin_mixed_words(self):
        self.assertEqual(self.p.get_pinyin(u'Apple发布iOS7', splitter=u'-'),
                         u'Apple-fa-bu-iOS7')

    def test_get_pinyin_with_tone_marks(self):
        self.assertEqual(self.p.get_pinyin(u'上海', tone_marks='marks'), u'sh\xe0ng-h\u01cei')

    def test_get_pinyin_with_tone_marks(self):
        self.assertEqual(self.p.get_pinyin(u'秋', tone_marks='marks'), u'qiū')

    def test_get_initial(self):
        self.assertEqual(self.p.get_initial(u'你'), u'N')

    def test_get_initials(self):
        self.assertEqual(self.p.get_initials(u'你好'), u'N-H')

    def test_get_initials_with_splitter(self):
        self.assertEqual(self.p.get_initials(u'你好', u' '), u'N H')
        self.assertEqual(self.p.get_initials(u'你好', u''), u'NH')

if __name__ == '__main__':
    unittest.main()
