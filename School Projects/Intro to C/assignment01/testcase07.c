// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase07.c
// ==========================
// Various tests of your print_pancakes_per_minute() function.


#include <stdio.h>

void print_pancakes_per_minute(double minutes, double pancake_count);

int main(void)
{
	print_pancakes_per_minute(2.0, 600.0);   // 300.000
	print_pancakes_per_minute(40.0, 12.0);   // 0.300
	print_pancakes_per_minute(23.0, 211.6);  // 9.200

	printf("\nHooray!\n");

	return 0;
}
