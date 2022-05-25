// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase13.c
// ==========================
// Various tests of your print_median_of_three() function.


#include <stdio.h>

void print_median_of_three(int a, int b, int c);

int main(void)
{
	// expected result: 5
	printf("Median of {1, 5, 9}:\n");
	print_median_of_three(1, 5, 9);
	printf("\n");

	// expected result: 5
	printf("Median of {9, 5, 1}:\n");
	print_median_of_three(9, 5, 1);
	printf("\n");

	// expected result: 5
	printf("Median of {1, 9, 5}:\n");
	print_median_of_three(1, 9, 5);
	printf("\n");

	// expected result: 5
	printf("Median of {9, 1, 5}:\n");
	print_median_of_three(9, 1, 5);
	printf("\n");

	// expected result: 5
	printf("Median of {5, 1, 9}:\n");
	print_median_of_three(5, 1, 9);
	printf("\n");

	// expected result: 5
	printf("Median of {5, 9, 1}:\n");
	print_median_of_three(5, 9, 1);
	printf("\n");

	// expected result: 1
	printf("Median of {1, 1, 5}:\n");
	print_median_of_three(1, 1, 5);
	printf("\n");

	// expected result: 1
	printf("Median of {1, 5, 1}:\n");
	print_median_of_three(1, 5, 1);
	printf("\n");

	// expected result: 1
	printf("Median of {5, 1, 1}:\n");
	print_median_of_three(5, 1, 1);
	printf("\n");

	// expected result: 1
	printf("Median of {1, 1, 1}:\n");
	print_median_of_three(1, 1, 1);
	printf("\n");

	printf("Hooray! (This will print even if you're not getting the correct results.)\n");

	return 0;
}
