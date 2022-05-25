// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase17.c
// ==========================
// Various tests of your get_ordinal_day_with_error_checking() function.


#include <stdio.h>

int get_ordinal_day_with_error_checking(int month, int day, int leapyear);

int main(void)
{
	printf("01/01 (NOT in a leap year): Day %d\n", get_ordinal_day_with_error_checking(1, 1, 0));    // expected result: 1
	printf("01/31 (NOT in a leap year): Day %d\n", get_ordinal_day_with_error_checking(1, 31, 0));   // expected result: 31
	printf("02/01 (NOT in a leap year): Day %d\n", get_ordinal_day_with_error_checking(2, 1, 0));    // expected result: 32
	printf("02/28 (NOT in a leap year): Day %d\n", get_ordinal_day_with_error_checking(2, 28, 0));   // expected result: 59
	printf("03/01 (NOT in a leap year): Day %d\n", get_ordinal_day_with_error_checking(3, 1, 0));    // expected result: 60
	printf("03/15 (NOT in a leap year): Day %d\n", get_ordinal_day_with_error_checking(3, 15, 0));   // expected result: 74
	printf("12/31 (NOT in a leap year): Day %d\n", get_ordinal_day_with_error_checking(12, 31, 0));  // expected result: 365

	printf("\n");

	printf("12/32 (NOT in a leap year): Day %d\n", get_ordinal_day_with_error_checking(12, 32, 0));  // expected result: -1
	printf("13/15 (NOT in a leap year): Day %d\n", get_ordinal_day_with_error_checking(13, 15, 0));  // expected result: -1
	printf("00/15 (NOT in a leap year): Day %d\n", get_ordinal_day_with_error_checking(0, 15, 0));   // expected result: -1
	printf("02/29 (NOT in a leap year): Day %d\n", get_ordinal_day_with_error_checking(2, 29, 0));   // expected result: -1

	printf("\n");

	printf("01/01 (in a leap year): Day %d\n", get_ordinal_day_with_error_checking(1, 1, 1));    // expected result: 1
	printf("01/31 (in a leap year): Day %d\n", get_ordinal_day_with_error_checking(1, 31, 1));   // expected result: 31
	printf("02/01 (in a leap year): Day %d\n", get_ordinal_day_with_error_checking(2, 1, 1));    // expected result: 32
	printf("02/28 (in a leap year): Day %d\n", get_ordinal_day_with_error_checking(2, 28, 1));   // expected result: 59
	printf("03/01 (in a leap year): Day %d\n", get_ordinal_day_with_error_checking(3, 1, 1));    // expected result: 61
	printf("03/15 (in a leap year): Day %d\n", get_ordinal_day_with_error_checking(3, 15, 1));   // expected result: 75
	printf("12/31 (in a leap year): Day %d\n", get_ordinal_day_with_error_checking(12, 31, 1));  // expected result: 366

	printf("\n");

	printf("12/32 (in a leap year): Day %d\n", get_ordinal_day_with_error_checking(12, 32, 1));  // expected result: -1
	printf("13/15 (in a leap year): Day %d\n", get_ordinal_day_with_error_checking(13, 15, 1));  // expected result: -1
	printf("00/15 (in a leap year): Day %d\n", get_ordinal_day_with_error_checking(0, 15, 1));   // expected result: -1
	printf("02/29 (in a leap year): Day %d\n", get_ordinal_day_with_error_checking(2, 29, 1));   // expected result: 60

	printf("\n");

	printf("Hooray! (This will print even if you're not getting the correct results.)\n");

	return 0;
}
