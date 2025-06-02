from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).resolve().parent
README = (here / "README.rst").read_text()
CHANGES = (here / "CHANGES.rst").read_text()

setup(
    name="xpinyin",
    version="0.7.7",
    description="Translate Chinese hanzi to pinyin (拼音) by Python, 汉字转拼音",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="pinyin",
    author="Eric Lo",
    author_email="lxneng@gmail.com",
    url="https://github.com/lxneng/xpinyin",
    packages=find_packages("src"),
    test_suite="xpinyin.tests",
    package_dir={"": "src"},
    include_package_data=True,
    extras_require={
        "test": ["pytest>=6.2.0"],
    },
    license="MIT",
)
