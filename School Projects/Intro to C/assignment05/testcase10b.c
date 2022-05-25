// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment05: testcase10b.c
// ===========================
// FUNCTION TESTED: hours_invested()
// OUTPUT FILE: sample_output/output10b.txt


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
