// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment06: testcase03b.c
// ===========================
// FUNCTION TESTED: update_missing_pancake_info()
// OUTPUT FILE: sample_output/output03b.txt


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

	// Note: This also relies on your print_pancake_report() function working correctly.
	update_missing_pancake_info(&p);
	print_pancake_report(p);

	return 0;
}
