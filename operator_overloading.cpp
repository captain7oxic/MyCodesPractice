#include <iostream>
using namespace std;

class complex
{
    float x; //real
    float y;

public:
    complex(){}; //default
    complex(float real, float imag)
    {
        x = real;
        y = imag;
    }
    void display();
    complex operator+(complex);
};

complex complex ::operator+(complex c)
{
    complex temp;
    temp.x = x + c.x;
    temp.y = y + c.y;
    return (temp);
}

void complex::display()
{
    cout << x << "+j" << y << endl;
}

int main()
{
    complex c1, c2, c3;
    c1 = complex(2.5, 3.5);
    c2 = complex(3.7, 6.9);
    c3 = c1 + c2;
    c3.display();
}