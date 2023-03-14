#include <stdio.h>
#include <stddef.h>
#include "Python.h"

/**
 * print_python_list_info - Prints some basic info about Python lists
 *
 * @p: Pointer to python list
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *) p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GET_ITEM(p, i))->tp_name);
	}
}
