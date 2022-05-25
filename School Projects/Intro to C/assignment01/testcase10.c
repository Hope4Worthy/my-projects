// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase10.c
// ==========================
// Various tests of your print_pancake_data() function.


#include <stdio.h>

void print_pancake_data(double pancake_count, double pancakes_per_minute, double minutes);

int main(void)
{
	print_pancake_data(0, 9.2, 23.0);
	printf("\n");

	print_pancake_data(211.6, 0, 23.0);
	printf("\n");

	print_pancake_data(211.6, 9.2, 0);
	printf("\n");

	printf("Hooray! (This will print even if you're not getting the correct results.)\n");

	return 0;
}
