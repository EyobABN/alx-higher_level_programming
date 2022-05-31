#include "lists.h"

/**
 * insert_node - inserts a number into a sorted
 * singly linked list
 * @head: the head of the list
 * @number: the number to be inserted
 *
 * Return: the address of the new node upon success,
 * NULL upon failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p = *head, *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || number < p->n)
	{
		new->next = p;
		*head = new;
	}
	else
	{
		while (p->next != NULL && p->next->n < number)
			p = p->next;
		new->next = p->next;
		p->next = new;
	}
	return (new);
}
