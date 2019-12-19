#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints basic info about a python list
 * @p: pointer to a python list
 */
void print_python_list_info(PyObject *p)
{
	int len, i;
	PyListObject *list = (PyListObject *)p;

	len = (int)PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", (int)list->allocated);
	for (i = 0; i < len; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
