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
	listint_t *temp_right, *temp_head, *temp_right_saved;
	int i;

	temp_right = *head;
	temp_head = *head;
	for (i = 0; i < list_length(temp_head) / 2; i++)
	{
		temp_right = temp_right->next;
	}
	temp_right = reverse_list(temp_right);
	temp_right_saved = temp_right;
	while (temp_head != NULL && temp_right != NULL)
	{
		if (temp_head->n != temp_right->n)
		{
			revert_append(*head, temp_right);
			return (0);
		}
		temp_head = temp_head->next;
		temp_right = temp_right->next;
	}
	revert_append(*head, temp_right_saved);
	return (1);
}

/**
 * list_length - returns the length of a listint_t list.
 * @head: pointer to the head of the list.
 * Return: the number of nodes in the list.
 */
int list_length(listint_t *head)
{
	int count = 0;

	while (head != NULL)
	{
		count++;
		head = head->next;
	}
	return (count);
}

/** 
 * revert_append - reverse a list and appends or attaches it to another
 * @head: pointer to the left piece
 * @tail: pointer to the right piece, which will be reversed.
 */
void revert_append(listint_t *head, listint_t *tail)
{
	int i;

	for (i = 0; i < list_length(head); i++)
		head = head->next;
	tail = reverse_list(tail);
	head->next = tail;
}

/**
 * reverse_list - reverses a linked list
 * @head: the head of the list
 * Return: the new head
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *temp = NULL, *tail;

	while (head != NULL)
	{
		tail = head->next;
		head->next = temp;
		temp = head;
		head = tail;
	}
	return (temp);
}
