#include <stdio.h>
/*void func(int a)
{
    printf("value of a is %d\n", a);
}*/
int main()
{
    int num[] = {1, 2, 3, 4, 5, 6};
    int *p1 = num;
    int *p2 = p1 + 5;
    int a = (char *)p2 - (char *)p1;
    printf("%d", a);
    return 0;
}