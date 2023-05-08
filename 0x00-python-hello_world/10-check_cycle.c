#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * list_size - checks the size of a linked list
 *
 * @list: the list
 * Return: the number of nodes in the list
 */
int list_size(listint_t *list)
{
	listint_t *temp = list;
	int len = 0;

	while (temp != NULL)
	{
		len++;
		temp = temp->next;
	}
	return (len);
}
/**
 * check_cycle - checks if a linked list has a cycle
 * @list: the linked list
 *
 * Return: 1 if there is a cycle and 0 for otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list, **check;
	int l = 1, i;

	check = malloc(120 * sizeof(listint_t*));
	check[0] = list;
	check[120] = NULL;
	while (temp != NULL)
	{
		temp = temp->next;
		check[l] = temp;
		i = 0;
		while (i < l)
		{
			if (check[i] == temp)
				return (1);
			i++;
		}
		l++;
	}
	return (0);
}
