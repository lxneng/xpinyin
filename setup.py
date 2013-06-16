# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

setup(name="xpinyin",
      version='0.4.8',
      description="translate chinese hanzi to pinyin by python",
      long_description=README + '\n\n' + CHANGES,
      author="Eric Lo",
      author_email="lxneng@gmail.com",
      url="https://github.com/lxneng/xpinyin",
      packages=find_packages('src'),
      test_suite='xpinyin.tests',
      package_dir={'': 'src'},
      include_package_data=True,
      license="MIT License")
