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
	listint_t *temp = list, *two, *two_t;
	int count = 0, l = 0;

	two = list;
	while (temp != NULL)
	{
		temp = temp->next;
		two_t = two;
		count++;
		l = 0;
		while (l < count)
		{
			if (temp == two_t)
			{
				return (1);
			}
			two_t = two_t->next;
			l++;
		}
	}
	return (0);
}
