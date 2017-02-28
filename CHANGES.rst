Changelog
=========


0.5.5 - Feb. 28, 2016
----------------------
- add a new staticmethod which can convert pinyin to upper, lower or capitalize.
  https://github.com/lxneng/xpinyin/pull/28

- Removed extraneous "!" being appended to non 'a' vowel replacements when show_tone_marks=True; also added simple unitest.main() for non-nose users
  https://github.com/lxneng/xpinyin/pull/30


0.5.4 - Dec. 14, 2015
----------------------

- replace open() calls with io.open() for Python 3 compatibility,
  fix `UnicodeDecodeError`
- change \u730E 猎 to LIE4
- improve readme


0.5.3 - Dec. 25, 2014
----------------------

- adjust default pinyin for character '什' and '么', 什么 => 'shén-me'


0.5.2 - Jul. 6, 2014
----------------------

- 修复一些常用字的拼音标注

0.4.9 - Oct. 25, 2013
----------------------

- change README and get_initials; add get_initial
  [tangsty]


0.4.8 - Jun. 16, 2013
----------------------

- change README and get_initials; add get_initial
  [tangsty]

- add download status image to README.rst
  [lxneng]

- add travis status image to README.rst
  [lxneng]

- add .travis.yml
  [lxneng]

- 添加测试
  [lxneng]

- 解决翻译中英文混合句子问题
  [lxneng]
