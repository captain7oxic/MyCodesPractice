#include <stdio.h>
int InsertionSort(int a[], int n)
{
    for (int i = 1; i < n; i++)
    {
        int temp = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > temp)
        {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = temp;
    }
    return;
}

void main()
{
    int a[] = {4, 3, 5, 7, 1, 3};
    int n = 5;
    InsertionSort(a[], n);
    for (i = 0; i < n; i++)
    {
        printf(" %d ", a[i]);
    }
}