// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment02: testcase17.c
// ==========================
// This test case helps ensure that your hours_invested() function returns a value
// within the expected range (as defined in the assignment PDF).


#include <stdio.h>

double hours_invested(void);

int main(void)
{
	if (hours_invested() <= 0.0 || hours_invested() >= 100.0)
	{
		printf("failwhale :(\n");
	}
	else
	{
		printf("Success!\n");
	}

	return 0;
}
