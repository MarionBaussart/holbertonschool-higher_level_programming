#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *hare = list->next, *turtle = list;

	if (list == NULL)
		return (0);
	while (hare && hare->next && turtle)
	{
		if (hare == turtle)
			return (1);
		hare = hare->next->next;
		turtle = turtle->next;
	}
	return (0);
}
