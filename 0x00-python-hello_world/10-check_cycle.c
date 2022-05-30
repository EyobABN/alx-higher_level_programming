#include "lists.h"

/**
 * check_cycle - checks if a cycle exists in a linked list
 * @list: the head of the linked list
 *
 * Return: 1 if there is a cycle, 0 if there isn't
 */
int check_cycle(listint_t *list)
{
	listint_t *f = list, *s = list;

	if (list == NULL)
		return (-1);
	while (1)
	{
		f = f->next->next;
		s = s->next;
		if (f == NULL || s == NULL)
			return (0);
		if (f == s)
			break;
	}
	return (1);
}
