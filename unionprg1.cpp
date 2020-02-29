#include <iostream>

using namespace std;

union myType {
    char c;
    unsigned int i;

} u;

int main()
{
    u.c = 'g';
    u.i = 66;

    cout << u.c << " " << u.i;
    return 0;
}