#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint - prints a doubly linked list
 * @h: the head of the linked list
 * Return: the number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t nofnodes = 0;
	dlistint_t *temp = (dlistint_t) h;

	while (temp != NULL)
	{
		printf("%d", temp->n);
		temp = temp->next;
		nofnodes++;
	}
	return (nofnodes)
}
