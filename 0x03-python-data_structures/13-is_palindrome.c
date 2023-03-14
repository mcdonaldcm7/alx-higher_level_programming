#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * get_2half - Returns a pointer to the halfpoint of the singly linked list
 *
 * @head: Pointer to the head of the singly linked list
 *
 * Return: Pointer to the midpoint of the list
 */
listint_t *get_2half(listint_t *head)
{
	listint_t *fast, *slow;

	fast = slow = head;
	while (fast != (void *) 0 && fast->next != (void *) 0)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return (slow);
}

/**
 * get_2bhalf - Returns a pointer to the halfpoint - 1 of the singly linked list
 *
 * @head: Pointer to the head of the singly linked list
 *
 * Return: Pointer to the node before the midpoint of the list
 */
listint_t *get_2bhalf(listint_t *head)
{
        listint_t *fast, *slow, *bslow;

        fast = slow = head;
	bslow = (void *) 0;
        while (fast != (void *) 0 && fast->next != (void *) 0)
        {
		bslow = slow;
                slow = slow->next;
                fast = fast->next->next;
        }

        return (bslow);
}


/**
 * push_node - Uses a stack technique to reverse the midpoint of the list
 *
 * @head: Pointer to the head of the list
 * @prev: Pointer to the previous node of the list
 *
 * Return: Pointer to the new head of the list
 */
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

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 *
 * @head: Pointer to the head of the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr, *nxt, *slow, *fast, *prev, *bslow;

	slow = fast = *head;
	curr = get_2half(*head);
	bslow = get_2bhalf(*head);
	if (bslow == (void *) 0)
		return (1);
	nxt = prev = (void *) 0;
	while (curr != (void *) 0)
	{
		nxt = curr->next;
		curr->next = prev;
		prev = curr;
		curr = nxt;
	}
	bslow->next = prev;
	while (fast != (void *) 0 && fast->next != (void *) 0)
	{
		if (slow->n != prev->n)
		{
			return 0;
		}
		slow = slow->next;
		fast = fast->next->next;
		prev = prev->next;
	}
	return (1);
}
