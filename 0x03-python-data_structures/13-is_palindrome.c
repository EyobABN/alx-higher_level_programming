#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list is
 * a palindrome
 * @head: the head of the list
 *
 * Return: 1 if a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int *nums, i, j;
	listint_t *p = *head;
	int len = 1;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	while ((p = p->next) != NULL)
		len++;
	nums = malloc(sizeof(int) * len);
	if (nums == NULL)
		return (0);
	for (i = 0, p = *head; i < len; i++, p = p->next)
		nums[i] = p->n;
	for (i = 0, j = len - 1; i < j; i++, j--)
		if (nums[i] != nums[j])
		{
			free(nums);
			return (0);
		}
	free(nums);
	return (1);
}
