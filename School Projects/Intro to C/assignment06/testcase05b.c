// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment06: testcase05b.c
// ===========================
// FUNCTION TESTED: clone_pancake_info()
// OUTPUT FILE: sample_output/output05b.txt


#include <stdio.h>
#include <stdlib.h>
#include "pancake_stuff.h"

int main(void)
{
	pancake_info source;
	pancake_info *p;

	source.name = "Jo Mama";
	source.pancake_count = 3.50184;
	source.pancakes_per_minute = 0.07002;
	source.minutes_spent_munching = 50.01201;

	p = clone_pancake_info(source);

	// Note: This also relies on your print_pancake_report() function working
	// correctly. Note also that this will crash if your make_pancake_info
	// function returns and invalid pointer or a corrupted struct.

	printf("Source Struct:\n");
	printf("==============\n");
	print_pancake_report(source);

	printf("\n");
	printf("Newly Allocated (Destination) Struct:\n");
	printf("=====================================\n");
	print_pancake_report(*p);

	if (source.name == p->name)
	{
		printf("\nOh no! The new struct doesn't point to a new copy of the name!\n");
	}

	// Both of these should have been dynamically allocated within the
	// make_pancake_info() function, so it should be safe to free them.
	free(p->name);
	free(p);

	return 0;
}
