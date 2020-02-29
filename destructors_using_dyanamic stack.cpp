#include <iostream>
#include <stdlib.h>

using namespace std;

class stack
{
private:
    char *data;
    int top_;

public:
    stack();
    ~stack();
    int empty()
    {
        return (top_ == -1);
    }
    void push(char x)
    {
        data[++top_] = x;
    }
    void pop()
    {
        --top_;
    }
    char top()
    {
        return data[top_];
    }
};

stack::stack() : data(new char[10]), top_(-1) //memory being assigned in heap of 10 chars and its pointer is returned to the data member 'data' .
{
    cout << "call using stack::stack()" << endl;
}

stack::~stack()
{
    //memory being deallocated at the end of main parenthesis by an implicit call to destructor.
    cout << "\ncall using stack::~stack:() function" << endl;
    delete data;
}

int main()
{
    char str[10] = "VATSAL";
    stack s;

    for (int i = 0; i < 6; ++i)
    {
        s.push(str[i]);
    }

    while (!s.empty())
    {
        cout << s.top();
        s.pop();
    }
    return 0;
}