// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment06: testcase02b.c
// ===========================
// FUNCTION TESTED: get_missing_pancake_info()
// OUTPUT FILE: sample_output/output02b.txt


#include <stdio.h>
#include <stdlib.h>
#include "pancake_stuff.h"

int main(void)
{
	pancake_info p;

	p.name = "Jo Mama";
	p.pancake_count = 3.52212;
	p.pancakes_per_minute = 0.0;
	p.minutes_spent_munching = 28.00000;

	printf("Return Value: %.3f\n", get_missing_pancake_info(p));

	return 0;
}
