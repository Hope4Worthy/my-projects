// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase03.c
// ==========================
// Various tests of your get_pancake_count() function.


#include <stdio.h>

double get_pancake_count(double minutes, double pancakes_per_minute);

int main(void)
{
	if (get_pancake_count(2.0, 300.0) != 600.0)
	{
		printf("Failed first call to get_pancake_count(). Womp womp. :(\n");
		return 0;
	}

	if (get_pancake_count(40.0, 0.3) != 12.0)
	{
		printf("Failed second call to get_pancake_count(). Womp womp. :(\n");
		return 0;
	}

	if (get_pancake_count(23.0, 9.2) != 211.6)
	{
		printf("Failed third call to get_pancake_count(). Womp womp. :(\n");
		return 0;
	}

	printf("Hooray!\n");

	return 0;
}
