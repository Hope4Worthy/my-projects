// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2018

// ==========================
// assignment04: testcase08.c
// ==========================
// FUNCTION TESTED: prior_experience()
// OUTPUT FILE: sample_output/output08.txt


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
