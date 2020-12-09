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
        self.assertEqual(self.p.get_pinyin(u'秋', tone_marks='marks'), u'qiū')

    def test_get_initial(self):
        self.assertEqual(self.p.get_initial(u'你'), u'N')

    def test_get_initials(self):
        self.assertEqual(self.p.get_initials(u'你好'), u'N-H')

    def test_get_initials_with_splitter(self):
        self.assertEqual(self.p.get_initials(u'你好', u' '), u'N H')
        self.assertEqual(self.p.get_initials(u'你好', u''), u'NH')

    # --- testing combinations ---

    def test_get_pinyins_with_default_splitter(self):
        self.assertEqual(self.p.get_pinyins(u'上海'), [u'shang-hai'])

    def test_get_pinyins_single_char(self):
        self.assertEqual(self.p.get_pinyins(u'乐', splitter='', tone_marks='marks'),
                         ['lè', 'yuè', 'yào', 'luò', 'liáo'])  # 4E50	LE4 YUE4 YAO4 LUO4 LIAO2

    def test_get_pinyins_two_chars(self):
        combs1 = self.p.get_pinyins(u'音', splitter='', tone_marks='marks')
        combs2 = self.p.get_pinyins(u'乐', splitter='', tone_marks='marks')
        combs12 = self.p.get_pinyins(u'音乐', splitter='', tone_marks='marks')
        self.assertEqual(len(combs12), len(combs1) * len(combs2))
        self.assertIn('yīnyuè', combs12)

    def test_get_pinyins_no_tones_uniq(self):
        self.assertEqual(['ma'], self.p.get_pinyins(u'吗', splitter='', tone_marks=None))

    def test_get_pinyins_max_number(self):
        self.assertEqual(5, len(self.p.get_pinyins(u'音乐', splitter='', n=5)))


if __name__ == '__main__':
    unittest.main()
