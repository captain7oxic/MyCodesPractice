#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;

class complex
{
    double real_;
    double imaginary_;

public:
    complex(double real, double imaginary) : real_(real),
                                             imaginary_(imaginary) {}

    double norm() { return sqrt(real_ * real_ + imaginary_ * imaginary_); }

    void print()
    {
        cout << "!" << real_ << "+j" << imaginary_ << "!=";
        cout << norm() << endl;
    }
};

int main()
{
    complex c(2.3, 6.4), d = {3.5, 6.8};

    c.print();
    d.print();

    return 0;
}