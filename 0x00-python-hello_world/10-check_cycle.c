#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *start = list, *search = list;

	while (search && search->next)
	{
		while (start != search && start != search->next)
			start = start->next;
		if (start == search->next)
			return (1);
		search = search->next;
		start = list;
	}
	return (0);
}
