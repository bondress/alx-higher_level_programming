#include <Python.h>

/**
 * print_python_list - prints basic info about Python lists
 * @p: a PyObject list object
 */
void print_python_list(PyObject *p)
{
	int sz, alloc, i;
	const char *typ;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	sz = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < sz; i++)
	{
		typ = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, typ);
		if (strcmp(typ, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, sz;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		sz = 10;
	else
		sz = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", sz);
	for (i = 0; i < sz; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (sz - 1))
			printf("\n");
		else
			printf(" ");
	}
}
