// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2018

// ==========================
// assignment04: testcase06.c
// ==========================
// FUNCTION TESTED: difficulty_rating()
// OUTPUT FILE: sample_output/output06.txt


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
