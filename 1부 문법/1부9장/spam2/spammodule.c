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

static PyObject *
spam_division(PyObject *self, PyObject *args)
{
    int quotient=0;
    int dividend,divisor=0; 
           
    if (!PyArg_ParseTuple(args, "ii", &dividend,&divisor)) //피제수와 제수 할당
          return NULL;
   
    if (divisor){
         quotient = dividend/divisor;
    } else {  // 제수가 0일 때 예외 처리를 합니다.
         // 예외 처리를 할 때는 반드시 NULL을 리턴 해줍니다. PyErr_SetString함수는 항상 NULL을 리턴합니다.
         //PyExc_ZeroDivisionError는 0으로 나누려고 할 때 쓰는 예외입니다.
         PyErr_SetString(PyExc_ZeroDivisionError, "divisor must not be zero");
         return  NULL;
    }
    
    return Py_BuildValue("i",quotient);
}


static PyMethodDef SpamMethods[] = {
    {"strlen", spam_strlen, METH_VARARGS,
    "count a string length."},
    {"division", spam_division, METH_VARARGS,
    "division function \n return quotient, quotient is dividend / divisor"},
    {NULL, NULL, 0, NULL}    //배열의 끝을 나타낸다.
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
