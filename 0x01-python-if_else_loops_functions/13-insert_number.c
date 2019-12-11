#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a number in it's correct spot in a linked list.
 * @head: a double pointer, the address of the pointer to the first node
 * @number: the number to be inserted
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
		return (new);
	new->next = *head;
	if (number < (*head)->n)
	{
		*head = new;
		return (new);
	}
	if ((*head)->n == number)
	{
		new->next = (*head)->next;
		(*head)->next = new;
		return (new);
	}
	temp = *head;
	new->next = temp->next;
	while (temp->next != NULL)
	{
		if (temp->n <= number && new->next->n >= number)
		{
			temp->next = new;
			return (new);
		}
		temp = temp->next;
		new->next = temp->next;
	}
	temp->next = new;
	return (new);
}
