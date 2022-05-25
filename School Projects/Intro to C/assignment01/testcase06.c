// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase06.c
// ==========================
// Various tests of your print_pancake_count() function.


#include <stdio.h>

void print_pancake_count(double minutes, double pancakes_per_minute);

int main(void)
{
	print_pancake_count(2.0, 300.0);  // 600.000
	print_pancake_count(40.0, 0.3);   // 12.000
	print_pancake_count(23.0, 9.2);   // 211.600

	printf("\nHooray!\n");

	return 0;
}
