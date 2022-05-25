// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment06: testcase01b.c
// ===========================
// FUNCTION TESTED: print_pancake_report()
// OUTPUT FILE: sample_output/output01b.txt


#include <stdio.h>
#include <stdlib.h>
#include "pancake_stuff.h"

int main(void)
{
	pancake_info p;

	p.name = "Jo Mama";
	p.pancake_count = 3.50184;
	p.pancakes_per_minute = 0.07002;
	p.minutes_spent_munching = 50.01201;

	print_pancake_report(p);

	return 0;
}
