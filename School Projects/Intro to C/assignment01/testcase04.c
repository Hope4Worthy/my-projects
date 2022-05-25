// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase04.c
// ==========================
// Various tests of your get_pancakes_per_minute() function.


#include <stdio.h>

double get_pancakes_per_minute(double minutes, double pancake_count);

int main(void)
{
	if (get_pancakes_per_minute(2.0, 600.0) != 300.0)
	{
		printf("Failed first call to get_pancakes_per_minute(). Womp womp. :(\n");
		return 0;
	}

	if (get_pancakes_per_minute(40.0, 12.0) != 0.3)
	{
		printf("Failed second call to get_pancakes_per_minute(). Womp womp. :(\n");
		return 0;
	}

	if (get_pancakes_per_minute(23.0, 211.6) != 9.2)
	{
		printf("Failed third call to get_pancakes_per_minute(). Womp womp. :(\n");
		return 0;
	}

	printf("Hooray!\n");

	return 0;
}
