// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase08.c
// ==========================
// Various tests of your print_minutes_spent_munching() function.


#include <stdio.h>

void print_minutes_spent_munching(double pancake_count, double pancakes_per_minute);

int main(void)
{
	print_minutes_spent_munching(600.0, 300.0);  // 2.000
	print_minutes_spent_munching(12.0, 0.3);     // 40.000
	print_minutes_spent_munching(211.6, 9.2);    // 23.000

	printf("\nHooray!\n");

	return 0;
}
