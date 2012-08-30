#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(name="xpinyin",
      version='0.4.5',
      description="translate chinese hanzi to pinyin by python",
      author="Eric Lo",
      author_email="lxneng@gmail.com",
      url="https://github.com/lxneng/xpinyin",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      license="MIT License")
