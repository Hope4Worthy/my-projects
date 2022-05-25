// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment03: testcase01c.c
// ===========================
// This test case calls your sort_ascending() function. If that function works correctly, then the
// output produced by this program will match the output specified in sample_output/output01c.txt.


#include <stdio.h>

void sort_ascending(int *a, int *b, int *c);

int main(void)
{
	int x, y, z;

	x = 2;
	y = 43;
	z = 9;

	printf("Before sorting:\n");
	printf("x = %d, y = %d, z = %d\n", x, y, z);

	sort_ascending(&x, &y, &z);

	printf("\n");
	printf("After sorting:\n");
	printf("x = %d, y = %d, z = %d\n", x, y, z);

	printf("\n");
	if (x == 2 && y == 9 && z == 43)
	{
		printf("Hooray!\n");
	}
	else
	{
		printf("oh no :(\n");
	}

	return 0;
}
