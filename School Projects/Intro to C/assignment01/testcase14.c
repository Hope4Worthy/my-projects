// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase14.c
// ==========================
// Various tests of your get_ordinal_day() function.


#include <stdio.h>

int get_ordinal_day(int month, int day);

int main(void)
{
	printf("01/01: Day %d\n", get_ordinal_day(1, 1));    // expected result: 1
	printf("01/31: Day %d\n", get_ordinal_day(1, 31));   // expected result: 31
	printf("02/01: Day %d\n", get_ordinal_day(2, 1));    // expected result: 32
	printf("02/28: Day %d\n", get_ordinal_day(2, 28));   // expected result: 59
	printf("03/01: Day %d\n", get_ordinal_day(3, 1));    // expected result: 60
	printf("03/15: Day %d\n", get_ordinal_day(3, 15));   // expected result: 74
	printf("12/31: Day %d\n", get_ordinal_day(12, 31));  // expected result: 365

	printf("\nHooray! (This will print even if you're not getting the correct results.)\n");

	return 0;
}
