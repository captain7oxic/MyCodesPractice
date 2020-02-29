#include <stdio.h>
#include <conio.h>

struct stacks
{
    int top;
    int capacity;
    char *string;
};
typedef struct stacks stack;

stack *createstack(int capacity)
{
    stack *s = malloc(sizeof(stack));
    s->top = -1;
    s->capacity = capacity;
    s->string = (char *)malloc(s->capacity * sizeof(char));
    return s;
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
        s->string[++s->top] = data;
    }
}

int pop(stack *s)
{
    int data;
    if (is_empty(s))
    {
        printf("Stack Underflow");
        return -1;
    }
    else
    {
        return s->string[s->top--];
    }
}

void reverse(char *str)
{
    int n = strlen(str);
    stack *s = createstack(n);
    for (int i = 0; i < n; i++)
    {
        push(s, str[i]);
    }
    for (int j = 0; j < n; j++)
    {
        str[j] = pop(s);
    }
}
int main()
{
    char str[] = "hidhchujejc";
    reverse(str);
    printf("%s", str);
    return 0;
}