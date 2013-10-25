from distutils.core import setup, Extension

classifierList = [ 'animal', 'animal::etc', 'animal::bird::penguin','animal::bird::sparrow',
'animal::mammal::human','animal::mammal::monkey']

setup(name='animal',
version='1.0',
classifiers = classifierList,
packages=['animal', 'animal.bird', 'animal.mammal'],

)