#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * list: pointer to first node of a linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *leader;

	leader = list;

	while (leader != NULL)
	{
		list = list->next;
		if (list == NULL)
			return (0);
		leader = leader->next->next;
		if (list == leader)
			return (1);
	}

	return (0);
}
