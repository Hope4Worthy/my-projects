// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase09.c
// ==========================
// Various tests of your get_pancake_data() function.


#include <stdio.h>

double get_pancake_data(double pancake_count, double pancakes_per_minute, double minutes);

int main(void)
{
	if (get_pancake_data(0, 9.2, 23.0) != 211.6)
	{
		printf("Failed first call to get_pancake_data(). Womp womp. :(\n");
		return 0;
	}

	if (get_pancake_data(211.6, 0, 23.0) != 9.2)
	{
		printf("Failed second call to get_pancake_data(). Womp womp. :(\n");
		return 0;
	}

	if (get_pancake_data(211.6, 9.2, 0) != 23.0)
	{
		printf("Failed third call to get_pancake_data(). Womp womp. :(\n");
		return 0;
	}

	printf("Hooray!\n");

	return 0;
}
