#include "lists.h"
/**
 * is_palindrome - checks to see if provided is palindrome
 *
 * @head: pointer to pointer of first node
 *
 * Return: 0 if not or 1 if true
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast;
	listint_t *slow;

	fast = *head;
	slow = *head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	slow = rev(slow);
	fast = *head;

	while (slow != NULL)
	{
		if (slow->n != fast->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}
	return (1);

}

/**
 * rev - gets reverse of linked list
 *
 * @slow: sub list to reverse
 *
 * Return: reversed list
 */

listint_t *rev(listint_t *slow)
{
	listint_t *prev;
	listint_t *next_n;

	prev = NULL;
	while (slow != NULL)
	{
		next_n = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next_n;
	}
	return (prev);
}
