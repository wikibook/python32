#include <Python.h>
#include "structmember.h"  // PyMethodDef 구조체를 사용하기 위해서 임포트 합니다.   
#define PI  3.14
typedef struct {
    PyObject_HEAD
    PyObject *color;   // 인스턴스 멤버: circle color 
    int radius;        // 인스턴스 멤버: circle radius    
} circle_CircleObject;
static PyObject *
Circle_new(PyTypeObject *type, PyObject *args, PyObject *keywords)
{
    circle_CircleObject *self;
    self = (circle_CircleObject *)type->tp_alloc(type, 0);  // type allocation  
    if (self != NULL) {
        self->color = PyUnicode_FromString("");
            if (self->color == NULL)
            {
                Py_DECREF(self);
                return NULL;
            }
 
        self->radius = 0;
    }
    return (PyObject *)self;
}
static void
Circle_dealloc(circle_CircleObject* self)
{
    Py_XDECREF(self->color);
    Py_TYPE(self)->tp_free((PyObject*)self);
}
static int
Circle_init(circle_CircleObject *self, PyObject *args, PyObject *keywords)
{
    PyObject *color=NULL, *tmp=NULL;
    static char *keywordList[] = {"color", "radius", NULL};
    if (! PyArg_ParseTupleAndKeywords(args, keywords, "|Si", keywordList,
                                    &color, &self->radius))
        return -1;
    if (color) {    // 인수 초기화
        tmp = self->color;
        Py_INCREF(color);
        self->color = color;   // 이전 인스턴스에 대해서 레퍼런스 카운트를 감소 시킵니다.  
        Py_XDECREF(tmp);
    }
    return 0;
}
// 외부객체에 공개될 인스턴스 멤버를 등록합니다.
static PyMemberDef Circle_members[] = {
    {"color", T_OBJECT_EX, offsetof(circle_CircleObject, color), 0,
    "color of circle"},
    {"radius", T_INT, offsetof(circle_CircleObject, radius), 0,
    "radius of circle"},
    {NULL}  /* 스트럭쳐의 끝 */
};

// 사용자 정의 함수 구현부  
static PyObject *
Circle_color(circle_CircleObject* self)
{
    static PyObject *fmt = NULL;
    PyObject *tmp, *result;
    if (fmt == NULL) {
        fmt = PyUnicode_FromString("The circle color is %s");
        if (fmt == NULL)
            return NULL;
    }
    if (self->color == NULL) {
        PyErr_SetString(PyExc_AttributeError, "color");
        return NULL;
    }
 
    tmp = Py_BuildValue("S", self->color);
    if (tmp == NULL)
        return NULL;
    result = PyUnicode_Format(fmt, tmp);
    Py_DECREF(tmp);     // 레퍼런스 카운트를 감소 시켜 줍니다.
  
    return result;
}
static PyObject *
Circle_area(circle_CircleObject* self)
{
    int area_circle = 0;

    if (self->radius < 0){
    PyErr_SetString(PyExc_AttributeError, "radius");
        return NULL;
    }
    area_circle = (int)(2 * (PI*(self->radius) ));
  
    return Py_BuildValue("i", area_circle);
}
// 사용자 정의 함수.  
static PyMethodDef Circle_methods[] = {
    {"color", (PyCFunction)Circle_color, METH_NOARGS,
    "Return the color of circle"
    },
    {"area", (PyCFunction)Circle_area, METH_NOARGS,
    "the area of a circle."
    },
    {NULL}
};
static PyObject* Circle_add(circle_CircleObject* self, circle_CircleObject* target)
{
    self->radius += target->radius;
    return Py_BuildValue("i", self->radius);
}
static PyObject* Circle_multiply(circle_CircleObject* self, circle_CircleObject* target)
{
    PyErr_SetString(PyExc_NotImplementedError, "The multiply has been not Implemented");
    return NULL;
}
static PyNumberMethods circle_number = {
     (binaryfunc) Circle_add, /*nb_add*/
     (binaryfunc) 0, /*nb_subtract*/
     (binaryfunc) Circle_multiply, /*nb_multiply*/
     (binaryfunc) 0 /*nb_remainder*/
};
static PyTypeObject circle_CircleType = {
    PyObject_HEAD_INIT(NULL)
    "circle.Circle",             /* tp_name */
    sizeof(circle_CircleObject),   /* tp_basicsize*/
    0,                         /* tp_itemsize */
     (destructor)Circle_dealloc, /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_reserved */
    0,                         /* tp_repr */
    &circle_number,       /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "The color & radius of circle has been saved",  /* tp_doc */
    0,       /* tp_traverse */
    0,       /* tp_clear */
    0,       /* tp_richcompare */
    0,       /* tp_weaklistoffset */
    0,       /* tp_iter */
    0,       /* tp_iternext */
    Circle_methods,    /* tp_methods */
    Circle_members, /* tp_members */
    0,       /* tp_getset */
    0,       /* tp_base */
    0,       /* tp_dict */
    0,       /* tp_descr_get */
    0,       /* tp_descr_set */
    0,       /* tp_dictoffset */
     (initproc)Circle_init, /* tp_init */
    0,                         /* tp_alloc */
    Circle_new,   /* tp_new */
};
static PyModuleDef circlemodule = {
    PyModuleDef_HEAD_INIT,
    "circle",
    "Example module that creates an extension type.",
    -1,
    NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC
PyInit_circle(void)
{
    PyObject* m;
    if (PyType_Ready(&circle_CircleType) < 0)
         return NULL;
    m = PyModule_Create(&circlemodule);
    if (m == NULL)
        return NULL;
    Py_INCREF(&circle_CircleType);
    PyModule_AddObject(m, "Circle", (PyObject *)&circle_CircleType);
    return m;
}
