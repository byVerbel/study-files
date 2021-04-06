#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
} node;

int main(void)
{
    node *list = NULL;

    // Number 1
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }

    n->number = 1;
    n->next = NULL;

    list = n;

    // Number 2
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list);
        return 1;
    }

    n->number = 2;
    n->next = NULL;

    list->next = n;

    // Number 3
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list);
        free(list->next);
        return 1;
    }

    n->number = 3;
    n->next = NULL;

    list->next->next = n;

    // Loop trough the values in the linked list
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->number);
    }

    // Loop to free all the memory allocated to the nodes
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list); // This will free the first node
        list = tmp; // Update list to contain the next node
    }
}