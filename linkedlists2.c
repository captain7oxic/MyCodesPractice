#include <stdio.h>
#include <stdlib.h>

struct nod
{
    int value;
    struct nod *next;
};
typedef struct nod node;
//function to allocate memory dyanamically through malloc on a heap.

node *Create_node(int value)
{
    node *result = malloc(sizeof(node));
    result->value = value;
    result->next = NULL;
    return result;
}
//function to print list

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

node *find(node *head, int value)
{
    node *tmp = head;
    while (tmp != NULL)
    {
        if (tmp->value == value)
        {
            return tmp;
        }
        else
            return NULL;
    }
}

node *insert_to_head(node **head, node *node_to_insert)
{
    node_to_insert->next = *head;
    *head = node_to_insert;
    return node_to_insert;
}
void main()
{
    node *head = NULL;
    node *tmp;

    /*tmp = Create_node(100);
    head = tmp;
    tmp = Create_node(200);
    //taking previous head and assigning  it to next ptr of tmp
    //so tmp comes first, and then replacing head with new tmp
    tmp->next = head;
    head = tmp;
    tmp = Create_node(400);
    tmp->next = head;
    head = tmp;*/
    //adding nodes via loop
    for (int i = 0; i < 25; i++)
    {
        tmp = Create_node(i);
        insert_to_head(&head, tmp);
        /*tmp->next = head;
        head = tmp;*/
    }

    printlist(head);

    tmp = find(head, 19);
    printf("you have found %d", tmp->value);

    return 0;
}