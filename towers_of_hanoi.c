void towers(int n, char frompeg, char auxpeg, char topeg)
{
    //if only one peg move and return
    if (n == 1)
    {
        printf("Move Disk 1 from peg %c to peg %c ", frompeg, topeg);
        return;
    }

    //move n-1 topdisks from a to b through c as  auxillary
    towers(n - 1, frompeg, auxpeg, topeg);
    //move remaining disk from a to c
    printf("\nMove disk %d from peg to %c to peg %c", n, frompeg, topeg);

    //move n-1 disk from b to c using a as auxillary
    towers(n - 1, auxpeg, topeg, frompeg);
}

int main()
{
    char A, B, C;
    towers(10, A, B, C);
    return 0;
}