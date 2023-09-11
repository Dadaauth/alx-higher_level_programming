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
	listint_t *tmp = *head, *prev = *head;
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
		if (number <= tmp->n)
		{
			new->next = tmp;
			if (prev == *head)
				*head = new;
			else
				prev->next = new;
			return (new);
		}
		prev = tmp;
		tmp = tmp->next;
	}
	tmp = prev;
	new->next = NULL;
	if (tmp == *head)
	{
		*head = malloc(sizeof(listint_t));
		if (*head == NULL)
		{
			free(new);
			return (NULL);
		}
		*head = new;
	}
	else
	{
		tmp->next = new;
	}
	return (new);
}
