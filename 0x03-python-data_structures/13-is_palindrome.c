#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to first node in the list
 * Return: pointer to first node in new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prv = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = prv;
		prv = curr;
		curr = next;
	}

	*head = prv;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to linked list
 *
 * Return: 0 if it is not, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *y = *head, *z = *head, *tmp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		z = z->next->next;
		if (!z)
		{
			dup = y->next;
			break;
		}
		if (!z->next)
		{
			dup = y->next->next;
			break;
		}
		y = y->next;
	}

	reverse_listint(&dup);

	while (dup && tmp)
	{
		if (tmp->n == dup->n)
		{
			dup = dup->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
