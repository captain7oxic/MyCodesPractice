#include <iostream>
#include <stdlib.h>

using namespace std;

//using automatic  array
class stack
{
private:
    //DATAMEMBERS
    char data[10]; // automatic
    int top_;

public:
    stack(); //constructor
    //member functions
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

stack::stack() : top_(-1)
{ //init list
    cout << "stack::stack() called" << endl;
}
int main()
{

    char str[10] = "ABCDE";
    stack s; //init by stack::stack():top(-1) call

    for (int i = 0; i < 5; ++i)
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