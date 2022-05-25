// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment03: testcase13.c
// ==========================
// This test case helps ensure that your prior_experience() function returns a value
// within the expected range (as defined in the assignment PDF).


#include <stdio.h>

double prior_experience(void);

int main(void)
{
	if (prior_experience() < 1.0 || prior_experience() > 5.0)
	{
		printf("failwhale :(\n");
	}
	else
	{
		printf("Success!\n");
	}

	return 0;
}
