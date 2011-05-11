#!/usr/bin/env python
from setuptools import setup, find_packages

version = '0.2'
setup(name="xpinyin",
      version=version,
      description="translate chinese hanzi to pinyin by python",
      author="Eric Lo",
      author_email="lxneng@gmail.com",
      url="https://github.com/lxneng/xpinyin",
      packages = find_packages(),
      include_package_data=True,
      license = "MIT License",
      zip_safe = True)
