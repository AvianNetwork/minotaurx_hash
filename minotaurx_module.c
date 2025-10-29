#define PY_SSIZE_T_CLEAN

#include <Python.h>

#include "minotaurx.h"

static PyObject *minotaurx_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
    PyBytesObject *input;

    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;

    Py_INCREF(input);
    output = PyMem_Malloc(32);

    if (output == NULL)
    {
        Py_DECREF(input);
        return PyErr_NoMemory();
    }

    minotaurx_hash((char *)PyBytes_AsString((PyObject *)input), output);
    Py_DECREF(input);

    value = Py_BuildValue("y#", output, 32);
    PyMem_Free(output);
    return value;
}

static PyMethodDef MinotaurXMethods[] = {
    {"getPoWHash", minotaurx_getpowhash, METH_VARARGS, "Returns the proof of work hash using MinotaurX hash"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef MinotaurXModule = {
    PyModuleDef_HEAD_INIT,
    "minotaurx_hash",
    "MinotaurX proof of work hash module",
    -1,
    MinotaurXMethods};

PyMODINIT_FUNC PyInit_minotaurx_hash(void)
{
    return PyModule_Create(&MinotaurXModule);
}
