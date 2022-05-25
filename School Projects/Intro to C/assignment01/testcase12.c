// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase12.c
// ==========================
// Various tests of your get_median_of_three() function.


#include <stdio.h>

int get_median_of_three(int a, int b, int c);

int main(void)
{
	printf("Median of {1, 5, 9}: %d\n", get_median_of_three(1, 5, 9));  // expected result: 5
	printf("Median of {9, 5, 1}: %d\n", get_median_of_three(9, 5, 1));  // expected result: 5
	printf("Median of {1, 9, 5}: %d\n", get_median_of_three(1, 9, 5));  // expected result: 5
	printf("Median of {9, 1, 5}: %d\n", get_median_of_three(9, 1, 5));  // expected result: 5
	printf("Median of {5, 1, 9}: %d\n", get_median_of_three(5, 1, 9));  // expected result: 5
	printf("Median of {5, 9, 1}: %d\n", get_median_of_three(5, 9, 1));  // expected result: 5
	printf("Median of {1, 1, 5}: %d\n", get_median_of_three(1, 1, 5));  // expected result: 1
	printf("Median of {1, 5, 1}: %d\n", get_median_of_three(1, 5, 1));  // expected result: 1
	printf("Median of {5, 1, 1}: %d\n", get_median_of_three(5, 1, 1));  // expected result: 1
	printf("Median of {1, 1, 1}: %d\n", get_median_of_three(1, 1, 1));  // expected result: 1

	printf("\nHooray! (This will print even if you're not getting the correct results.)\n");

	return 0;
}
