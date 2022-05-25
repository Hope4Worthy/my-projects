// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment03: testcase05a.c
// ===========================
// This test case calls your get_pointer_to_median() function. If that function works
// correctly, then the output produced by this program will match the output specified in
// sample_output/output05a.txt.


#include <stdio.h>

int *get_pointer_to_median(int *a, int *b, int *c);

int main(void)
{
	int x, y, z, *ptr;

	x = 34;
	y = 11;
	z = 25;

	ptr = get_pointer_to_median(&x, &y, &z);

	// z holds the median of those three values, so the function must return a pointer to z.
	if (ptr == &z)
	{
		printf("Hooray!\n");
	}
	else
	{
		printf("oh no :(\n");
	}

	if (x != 34 || y != 11 || z != 25)
	{
		printf("Oh no! Your function shouldn't change the values pointed to by a, b, and c!\n");
	}

	return 0;
}
