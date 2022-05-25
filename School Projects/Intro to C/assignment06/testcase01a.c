// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment06: testcase01a.c
// ===========================
// FUNCTION TESTED: print_pancake_report()
// OUTPUT FILE: sample_output/output01a.txt


#include <stdio.h>
#include <stdlib.h>
#include "pancake_stuff.h"

int main(void)
{
	pancake_info p;

	p.name = "Bo Bobbity Frank";
	p.pancake_count = 23.39413;
	p.pancakes_per_minute = 2.10001;
	p.minutes_spent_munching = 11.14001;

	print_pancake_report(p);

	return 0;
}
