#include <stdio.h>
#include <stdlib.h>

struct nod
{
    int value;
    struct node *next;
};
typedef struct nod node;

void printlist(node *head)
{
    node *temp = head;
    while (temp != NULL)
    {
        printf("%d -", temp->value);
        temp = temp->next;
    }
    printf("\n");
}

node *insert_to_head(node **head, node *node_to_insert)
{
    node_to_insert->next = *head;
    *head = node_to_insert;
    return node_to_insert;
}

void main()
{
    //declaration of structure variables .
    node n1, n2, n3;
    node *head;
    // values of nodes

    n1.value = 21;
    n2.value = 31;
    n3.value = 41;

    //link them up.
    head = &n1;
    n1.next = &n3;
    n3.next = &n2;
    n2.next = NULL;
    printlist(head);

    //adding new node
    node n4;
    n4.value = 100;
    n4.next = &n3;
    n1.next = &n4;

    printlist(head);

    return 0;
}