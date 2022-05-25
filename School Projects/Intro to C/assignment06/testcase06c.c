// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment06: testcase06c.c
// ===========================
// FUNCTION TESTED: prior_experience()
// OUTPUT FILE: sample_output/output06c.txt


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
