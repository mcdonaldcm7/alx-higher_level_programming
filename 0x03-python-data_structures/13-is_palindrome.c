#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

listint_t *get_2half(listint_t *head)
{
	listint_t *fast, *slow;

	fast = slow = head;
	while (fast != (void *) 0)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	return (slow);
}

listint_t *push_node(listint_t *head, listint_t *prev)
{
	listint_t *new;

	new = malloc(sizeof(*new));
	if (new == (void *) 0)
		return (new);
	new->n = head->n;
	new->next = prev;
	return (new);
}

int is_palindrome(listint_t **head)
{
	listint_t *half, *revhead, *slow, *fast, *prev, *iter;

	slow = fast = *head;
	half = get_2half(*head);
	revhead = prev = (void *) 0;

	if (head == (void *) 0 || *head == (void *) 0)
		return (1);
	while (half != (void *) 0)
	{
		revhead = push_node(half, prev);
		if (revhead == (void *) 0)
		{
			free_listint(prev);
			return (0);
		}
		half = half->next;
		prev = revhead;
	}

	iter = revhead;
	while(fast != (void *) 0 && fast->next != (void *) 0)
	{
		if (slow->n != iter->n)
		{
			free_listint(revhead);
			return (0);
		}
		slow = slow->next;
		fast = fast->next->next;
		iter = iter->next;
	}
	free_listint(revhead);
	return (1);
}
