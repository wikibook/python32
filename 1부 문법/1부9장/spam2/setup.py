# -*- coding: cp949 -*-
# 파이썬
# 사용방법 : 'setup.py install' 빌드와 설치가 동시에 진행됩니다. 
# 'setup.py --help'처럼 실행하시면 자세한 사용방법을 볼 수 있습니다.
from distutils.core import setup, Extension
spam_mod = Extension('spam', sources = ['spammodule.c'])
setup(name = "spam",
    version = "1.0",
    description = "A sample extension module",
    ext_modules = [spam_mod],
)
