// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase11.c
// ==========================
// Various tests of your round_up_or_down() function.


#include <stdio.h>

int round_up_or_down(double dub);

int main(void)
{
	printf("%d\n", round_up_or_down(12.00));  // expected result: 12
	printf("%d\n", round_up_or_down(12.10));  // expected result: 12
	printf("%d\n", round_up_or_down(12.49));  // expected result: 12
	printf("%d\n", round_up_or_down(12.50));  // expected result: 13
	printf("%d\n", round_up_or_down(12.51));  // expected result: 13
	printf("%d\n", round_up_or_down(12.89));  // expected result: 13
	printf("%d\n", round_up_or_down(12.90));  // expected result: 13
	printf("%d\n", round_up_or_down(0.000));  // expected result: 0

	printf("\nHooray! (This will print even if you're not getting the correct results.)\n");

	return 0;
}
