#include "Python.h"

static PyObject *
page_print(PyObject *self, PyObject *args)
{
    const char* str="module name is page";
    
    return Py_BuildValue("s", str);
}

static PyMethodDef PageMethods[] = {
	 {"print", page_print, METH_VARARGS,
     "print page module information."},
     {NULL, NULL, 0, NULL}    //배열의 끝을 나타냅니다.
};

static struct PyModuleDef pagemodule = {
   PyModuleDef_HEAD_INIT,
   "page",               // 모듈 이름
   "It is test module.", 
   -1,PageMethods
};

PyMODINIT_FUNC
PyInit_page(void)
{
    return PyModule_Create(&pagemodule);
}
