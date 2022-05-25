// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment06: testcase04b.c
// ===========================
// FUNCTION TESTED: make_pancake_info()
// OUTPUT FILE: sample_output/output04b.txt


#include <stdio.h>
#include <stdlib.h>
#include "pancake_stuff.h"

int main(void)
{
	pancake_info *p;

	p = make_pancake_info("Jo Mama", 3.50184, 0.07002, 50.01201);

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
