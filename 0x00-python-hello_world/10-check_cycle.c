#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 *
 * @list: pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *tmp;
	int count, i;

	count = 0;
	current = list;
	while (current != (void *) 0)
	{
		current = current->next;
		count++;
		tmp = list;
		for (i = 0; i < count; i++, tmp = tmp->next)
		{
			if (tmp == current)
				return (1);
		}
	}

	return (0);
}
