#include <stdio.h>
#include <conio.h>
#define MAXSIZE 10

struct stacks
{
    int capacity;
    int top;
    int *array;
};

typedef struct stacks stack;

stack *createstack()
{
    stack *s = malloc(sizeof(stack));
    s->top = -1;
    s->capacity = MAXSIZE;
    s->array = malloc(s->capacity * sizeof(int));
    if (!s)
    {
        return;
    }
    else
    {
        return s;
    }
}

int is_empty(stack *s)
{
    return (s->top == -1);
}
int is_full(stack *s)
{
    return (s->top == s->capacity - 1);
}

void push(stack *s, int data)
{
    if (is_full(s))
    {
        printf("Stack Overflow");
    }
    else
    {
        s->array[++s->top] = data;
    }
}

int pop(stack *s)
{
    int data;
    if (is_empty(s))
    {
        printf("Stack Underflow");
    }
    else
    {
        return (s->array[s->top--]);
    }
}

int main()
{
    stack *mystack = createstack();
    //printf(" stack state =%d as its empty", is_empty(mystack));
    //pushing elements to stack
    push(mystack, 10);
    push(mystack, 20);
    push(mystack, 30);
    printf("popping top from stack %d", pop(mystack));
    printf("popping top from stack %d", pop(mystack));
    printf("popping top from stack %d", pop(mystack));
    return 0;
}