#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * dlistint_len - a function that returns the number of elements in a linked dlistint_t list
 * @h: a pointer to the head of the list
 *
 * Return: the number of elements in a linked list
 */

size_t dlistint_len(const dlistint_t *h)
{
	int x = 0;

	if (h == NULL)
		return (x);
	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		x++;
		h = h->next;
	}

	return (x);
}
