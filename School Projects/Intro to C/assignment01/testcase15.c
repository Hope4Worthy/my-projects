// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase15.c
// ==========================
// Various tests of your print_ordinal_day() function.


#include <stdio.h>

int print_ordinal_day(int month, int day);

int main(void)
{
	// expected result: 1
	print_ordinal_day(1, 1);

	// expected result: 31
	print_ordinal_day(1, 31);

	// expected result: 32
	print_ordinal_day(2, 1);

	// expected result: 59
	print_ordinal_day(2, 28);

	// expected result: 60
	print_ordinal_day(3, 1);

	// expected result: 74
	print_ordinal_day(3, 15);

	// expected result: 365
	print_ordinal_day(12, 31);

	printf("\nHooray! (This will print even if you're not getting the correct results.)\n");

	return 0;
}
