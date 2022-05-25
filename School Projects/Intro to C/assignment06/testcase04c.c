// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment06: testcase04c.c
// ===========================
// FUNCTION TESTED: make_pancake_info()
// OUTPUT FILE: sample_output/output04c.txt


#include <stdio.h>
#include <stdlib.h>
#include "pancake_stuff.h"

int main(void)
{
	pancake_info *p;

	p = make_pancake_info("Low Key Covfefe", 3.52212, 0.12579, 28.00000);

	// Note: This also relies on your print_pancake_report() function working
	// correctly. Note also that this will crash if your make_pancake_info
	// function returns and invalid pointer or a corrupted struct.
	print_pancake_report(*p);

	// Both of these should have been dynamically allocated within the
	// make_pancake_info() function, so it should be safe to free them.
	free(p->name);
	free(p);

	return 0;
}
