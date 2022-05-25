// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase05.c
// ==========================
// Various tests of your get_minutes_spent_munching() function.


#include <stdio.h>

double get_minutes_spent_munching(double pancake_count, double pancakes_per_minute);

int main(void)
{
	if (get_minutes_spent_munching(600.0, 300.0) != 2.0)
	{
		printf("Failed first call to get_minutes_spent_munching(). Womp womp. :(\n");
		return 0;
	}

	if (get_minutes_spent_munching(12.0, 0.3) != 40.0)
	{
		printf("Failed second call to get_minutes_spent_munching(). Womp womp. :(\n");
		return 0;
	}

	if (get_minutes_spent_munching(211.6, 9.2) != 23.0)
	{
		printf("Failed third call to get_minutes_spent_munching(). Womp womp. :(\n");
		return 0;
	}

	printf("Hooray!\n");

	return 0;
}
