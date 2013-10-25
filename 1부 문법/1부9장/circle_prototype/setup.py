from distutils.core import setup, Extension
setup(name="circle",
      version="1.0",
      ext_modules=[Extension("circle", ["circle_prototype.c"])]) 
