
from distutils.core import setup, Extension
setup(name='book',
version='1.0',
classifiers = [ 'book','book.bookDataBase'],
packages=['book','book.bookDataBase'],
package_dir={'bookDataBase': 'book'},
)

