#include <stdio.h>
#include <conio.h>

struct nod
{
    int value;
    struct node *head;
};

typedef struct nod node;

void insertNode(struct node **head, int value, int position)
{
    int k = 1;
    struct node *p, *q, *newnode;
    newnode = (node *)malloc(sizeof(node));
    if (!newnode)
    {
        printf("memory error");
        return;
    }
    newnode->value = value;
    p = *head;

    //insert at beginning
    if (position == 1)
    {
        newnode->next = p;
        *head = newnode;
    }
    else
    {
        //traverse the list
        while ((p != NULL) && (k < position))
        {
            k++;
            q = p;
            p = p->next;
        }
        q->next = newnode;
        newnode->next = p;
    }
}
