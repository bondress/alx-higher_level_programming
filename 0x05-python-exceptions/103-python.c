#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t siz, alloc, i;
	const char *typ;
	PyListObject *li = (PyListObject *)p;
	PyVarObject *v = (PyVarObject *)p;

	siz = v->ob_size;
	alloc = li->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", siz);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < siz; i++)
	{
		typ = li->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, typ);
		if (strcmp(typ, "bytes") == 0)
			print_python_bytes(li->ob_item[i]);
		else if (strcmp(typ, "float") == 0)
			print_python_float(li->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t siz, i;
	PyBytesObject *b = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", b->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		siz = 10;
	else
		siz = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", siz);
	for (i = 0; i < siz; i++)
	{
		printf("%02hhx", b->ob_sval[i]);
		if (i == (siz - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *buff = NULL;

	PyFloatObject *fl_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buff = PyOS_double_to_string(fl_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buff);
	PyMem_Free(buff);
}
