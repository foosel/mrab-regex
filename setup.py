#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, Extension
from os.path import join

setup(
    ext_modules=[Extension('regex._regex', [join('regex_3', '_regex.c'),
      join('regex_3', '_regex_unicode.c')])],
)
