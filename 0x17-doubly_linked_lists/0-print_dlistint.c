#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint - a function that prints the elements of a list
 * @h: a pointer to the head of the list
 *
 * Return: the number fo nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	int i = 0;

	if (h == NULL)
		return (i);
	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		i++;
		h = h->next;
	}
	return (i);
}
