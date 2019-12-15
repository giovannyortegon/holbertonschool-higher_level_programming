#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t * prev = NULL;
	listint_t *curr = (*head);
	listint_t *np = add_nodeint_end( &curr, number);
	
	while (curr != NULL && number > curr->n)
	{
		prev = curr;
		curr = curr->next;
	}
	
	np->next = curr;
	prev-> next = np;
	return (*head);
}
