#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted linked list.
 * @head: the head of the node
 * @number: the new number to insert
 * Return: a pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (head == NULL || new == NULL)
	{
		free(new);
		return (NULL);
	}
	new->n = number;
	while (tmp != NULL)
	{
		if (number < tmp->next->n)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	tmp->next = new;
	new->next = NULL;
	return (new);
}
