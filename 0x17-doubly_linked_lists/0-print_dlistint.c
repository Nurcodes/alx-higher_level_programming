#include "lists.h"

/**
 * print_dlistint - print all the number of nodes
 *
 * @h: head pointer
 *
 * Return: size of list
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t nums = 0;

	while (h != NULL)
	{
		nums++;
		printf("%d\n", h->n);
		h = h->next;
	}
	return (nums);
}
