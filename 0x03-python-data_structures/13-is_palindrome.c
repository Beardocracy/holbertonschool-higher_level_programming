#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks a list to see if it is a palindrome
 * @head: pointer to the head of the list.
 * Return: 1 if is palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp1, *temp2;
	int start, len, i, end;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	if (loop_exists(head))
		return (0);
	len = list_length(head);
	temp1 = *head;
	len -= 1;
	for (start = 0, end = len; start <= end; start++, len -= 2, end--)
	{
		temp2 = temp1;
		for (i = 0; i < len; i++)
			temp2 = temp2->next;
		if (temp1->n != temp2->n)
			return (0);
		temp1 = temp1->next;
	}
	return (1);
}

/**
 * list_length - returns the length of a listint_t list.
 * @head: pointer to the head of the list.
 * Return: the number of nodes in the list.
 */
int list_length(listint_t **head)
{
	listint_t *temp = *head;
	int count = 0;

	while (temp != NULL)
	{
		count++;
		temp = temp->next;
	}
	return (count);
}

/**
 * loop_exists - checks a listint_t list for a loop
 * @head: pointer to the first node.
 * Return: 1 if loop exists, 0 if not.
 */
int loop_exists(listint_t **head)
{
	listint_t *hare = *head;
	listint_t *tort = *head;
	
	while (hare != NULL)
	{
		tort = tort->next;
		hare = hare->next;
		if (hare == NULL)
			return (0);
		hare = hare->next;
		if (hare == tort)
			return (1);
	}
	return (0);
}
