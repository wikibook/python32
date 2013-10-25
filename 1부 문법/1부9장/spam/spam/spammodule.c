#include "python.h" 

static PyObject * 

spam_strlen(PyObject *self, PyObject *args)
{
    const char* str=NULL;
    int len; 

    if (!PyArg_ParseTuple(args, "s", &str)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
         return NULL; 

    len = strlen(str); 

    return Py_BuildValue("i", len);
}

static PyMethodDef SpamMethods[] = {
{"strlen", spam_strlen, METH_VARARGS,
 "count a string length."},
 {NULL, NULL, 0, NULL} // 배열의 끝을 나타냅니다.
}; 

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",            // 모듈 이름
    "It is test module.", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
    -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
