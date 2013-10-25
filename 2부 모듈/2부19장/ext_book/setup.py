from distutils.core import setup, Extension
setup(name='book',
version='1.0',
ext_package='pkg',
ext_modules=[ Extension('book', ['book.c']),
Extension('book.page', ['page.c'])],
)
