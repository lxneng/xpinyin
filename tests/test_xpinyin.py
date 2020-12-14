import pytest

from xpinyin import Pinyin
from xpinyin.combs import _get_comb_indexes, get_combs


@pytest.fixture(scope='module')
def pinyin():
    return Pinyin()


def test_get_pinyin_with_default_splitter(pinyin):
    assert pinyin.get_pinyin('上海') == 'shang-hai'


def test_get_pinyin_with_splitter(pinyin):
    assert pinyin.get_pinyin('上海', splitter='') == 'shanghai'


def test_get_pinyin_mixed_words(pinyin):
    assert pinyin.get_pinyin('Apple发布iOS7', splitter='-') == 'Apple-fa-bu-iOS7'


def test_get_pinyin_with_tone_marks(pinyin):
    assert pinyin.get_pinyin('上海', tone_marks='marks') == 'sh\xe0ng-h\u01cei'
    assert pinyin.get_pinyin('秋', tone_marks='marks') == 'qiū'


def test_get_initial(pinyin):
    assert pinyin.get_initial('你') == 'N'


def test_get_initials(pinyin):
    assert pinyin.get_initials('你好') == 'N-H'


def test_get_initials_with_splitter(pinyin):
    assert pinyin.get_initials('你好', ' ') == 'N H'
    assert pinyin.get_initials('你好', '') == 'NH'


def test_get_initials_with_retroflex(pinyin):
    assert pinyin.get_initials('上海', '-', True) == 'SH-H'
    assert pinyin.get_initials('知识', '-', True) == 'ZH-SH'
    assert pinyin.get_initials('文字', '-', True) == 'W-Z'


# --- testing combinations auxiliary functions ---

def test_get_comb_indexes(pinyin):
    assert [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0]] == _get_comb_indexes([2, 2, 1])


def test_get_comb_indexes_max_num(pinyin):
    assert [[0, 0, 0], [0, 1, 0], [1, 0, 0]], _get_comb_indexes([2, 2, 1], 3)


def test_get_combs(pinyin):
    assert ['a1@', 'a1#', 'a2@', 'a2#', 'b1@', 'b1#', 'b2@', 'b2#'] == get_combs([['a', 'b'], ['1', '2'], ['@', '#']])


def test_get_combs_splitter_max_num(pinyin):
    assert ['a 1 @', 'a 1 #', 'a 2 @', 'a 2 #', 'b 1 @'] == get_combs([['a', 'b'], ['1', '2'], ['@', '#']],
                                                                      splitter=' ', n=5)


def test_get_combs_max_num_too_big(pinyin):
    assert ['a||1||@', 'a||1||#', 'a||2||@', 'a||2||#', 'b||1||@', 'b||1||#', 'b||2||@', 'b||2||#'] == get_combs(
        [['a', 'b'], ['1', '2'], ['@', '#']], splitter='||', n=100)


# --- testing pinyin combinations ---

def test_get_pinyins_with_default_splitter(pinyin):
    assert pinyin.get_pinyins('上海') == ['shang-hai']


def test_get_pinyins_single_char(pinyin):
    # 4E50	LE4 YUE4 YAO4 LUO4 LIAO2
    assert ['lè', 'yuè', 'yào', 'luò', 'liáo'] == pinyin.get_pinyins('乐', splitter='', tone_marks='marks')


def test_get_pinyins_two_chars(pinyin):
    combs1 = pinyin.get_pinyins('音', splitter='', tone_marks='marks')
    combs2 = pinyin.get_pinyins('乐', splitter='', tone_marks='marks')
    combs12 = pinyin.get_pinyins('音乐', splitter='', tone_marks='marks')
    assert len(combs12) == len(combs1) * len(combs2)
    assert 'yīnyuè' in combs12


def test_get_pinyins_no_tones_uniq(pinyin):
    assert ['ma'] == pinyin.get_pinyins('吗', splitter='', tone_marks=None)


def test_get_pinyins_max_num(pinyin):
    assert 5 == len(pinyin.get_pinyins('音乐', splitter='', n=5))


def test_get_pinyins_mixed_words(pinyin):
    assert pinyin.get_pinyins('ABC串123', splitter=' ', tone_marks='marks') == ['ABC chuàn 123', 'ABC guàn 123']


def test_get_pinyins_long_seq(pinyin):
    text = """汉语拼音（Hànyǔ Pīnyīn），
        簡稱拼音，是一種以拉丁字母作普通话（現代標準漢語）標音的方案，為中文羅馬拼音的國際標準規範。
        汉语拼音在中国大陆作为基础教育内容全面使用，是义务教育的重要内容。在海外，特别是常用現代標準漢語的地区如新加坡、
        马来西亚、菲律宾和美国唐人街等，目前也在汉语教育中进行汉语拼音教学。臺灣自2008年開始，
        中文譯音使用原則也採用漢語拼音[1]，但舊護照姓名和部分地名、道路名稱仍採用威妥瑪拼音、
        郵政式拼音、國語羅馬字、國音二式抑或通用拼音[2]。"""
    assert 20 == len(pinyin.get_pinyins(text, n=20))
    assert 10 == len(pinyin.get_pinyins(text))  # limited to 10 by default
