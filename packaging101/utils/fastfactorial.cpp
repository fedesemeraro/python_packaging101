#include <Python.h>

int cpp_fastfactorial(int n) {
    if (n <= 1)
        return 1;
    else
        return n * cpp_fastfactorial(n - 1);
}

static PyObject* py_fastfactorial(PyObject* self, PyObject* args) {
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    int result = cpp_fastfactorial(n);

    return Py_BuildValue("i", result);
}

static PyMethodDef methods[] = {
    {"fastfactorial", py_fastfactorial, METH_VARARGS, "Calculate the factorial of n"},
    {NULL, NULL, 0, NULL}  // Sentinel
};

static PyModuleDef fastfactorialmodule = {
    PyModuleDef_HEAD_INIT,
    "fastfactorial",  // Module name should match the name used in setup.py
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_fastfactorial(void) {
    return PyModule_Create(&fastfactorialmodule);
}
