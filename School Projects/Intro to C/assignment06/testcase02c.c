// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment06: testcase02c.c
// ===========================
// FUNCTION TESTED: get_missing_pancake_info()
// OUTPUT FILE: sample_output/output02c.txt


#include <stdio.h>
#include <stdlib.h>
#include "pancake_stuff.h"

int main(void)
{
	pancake_info p;

	p.name = "Low Key Covfefe";
	p.pancake_count = 3.52212;
	p.pancakes_per_minute = 0.12579;
	p.minutes_spent_munching = 0.0;

	printf("Return Value: %.3f\n", get_missing_pancake_info(p));

	return 0;
}
