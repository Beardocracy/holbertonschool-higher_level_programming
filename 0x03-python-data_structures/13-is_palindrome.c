#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks a list to see if it is a palindrome
 * @head: pointer to the head of the list.
 * Return: 1 if is palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp1, *temp2;
	int start, end, len, i;

	if (*head == NULL)
		return (1);
	len = list_length(*head);
	if (len == 1)
		return (1);
	for (start = 0, end = len - 1; start <= end; start++, end--)
	{
		temp1 = *head;
		temp2 = *head;
		for (i = 0; i < start; i++)
			temp1 = temp1->next;
		for (i = 0; i < end; i++)
			temp2 = temp2->next;
		if (temp1->n != temp2->n)
			return (0);
	}
	return (1);
}

/**
 * list_length - returns the length of a listint_t list.
 * @head: pointer to the head of the list.
 * Return: the number of nodes in the list.
 */
int list_length(listint_t *head)
{
	listint_t *temp = head;
	int count = 0;

	while (temp != NULL)
	{
		count++;
		temp = temp->next;
	}
	return (count);
}
