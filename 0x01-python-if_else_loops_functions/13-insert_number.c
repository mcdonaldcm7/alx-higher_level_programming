#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 *
 * @head: Pointer to the head of the list
 * @n: value of the number to be inserted
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, const int n)
{
	listint_t *curr, *tmp, *prev;

	tmp = malloc(sizeof(*tmp));
	if (tmp == (void *) 0)
		return (tmp);
	tmp->n = n;
	if (head == (void *) 0 || *head == (void *) 0)
	{
		tmp->next = (void *) 0;
		*head = tmp;
		return (tmp);
	}
	if ((*head)->n > n)
	{
		tmp->next = *head;
		*head = tmp;
		return (tmp);
	}
	for (curr = *head, prev = (void *) 0; curr->next != ((void *) 0);
			prev = curr, curr = curr->next)
	{
		if (curr->n > n)
		{
			tmp->next = curr;
			prev->next = tmp;
			return (tmp);
		}
	}

	tmp->next = (void *) 0;
	curr->next = tmp;
	return (tmp);
}
