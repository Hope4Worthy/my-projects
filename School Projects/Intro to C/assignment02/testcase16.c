// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment02: testcase16.c
// ==========================
// This test case helps ensure that your difficulty_rating() function returns a value
// within the expected range (as defined in the assignment PDF).


#include <stdio.h>

double difficulty_rating(void);

int main(void)
{
	if (difficulty_rating() < 1.0 || difficulty_rating() > 5.0)
	{
		printf("failwhale :(\n");
	}
	else
	{
		printf("Success!\n");
	}

	return 0;
}
