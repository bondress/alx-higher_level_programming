#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - prints some basic info about Python lists
* @p: python object
**/

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int n;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (n = 0; n < size; n++)
		printf("Element %i: %s\n", n, Py_TYPE(obj->ob_item[n])->tp_name);
}
