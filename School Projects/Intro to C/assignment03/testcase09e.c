// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment03: testcase09e.c
// ===========================
// This test case calls your feed_glowworm() function. If that function works correctly, then the
// output produced by this program will match the output specified in sample_output/output09e.txt.


#include <stdio.h>

int feed_glowworm(int *tail, int *head, int *is_alive, char *snack);

int main(void)
{
	int tail = 4, head = 10, is_alive = 1, retval;
	char snack = 'q';

	// The glowworm shouldn't eat this snack.
	retval = feed_glowworm(&tail, &head, &is_alive, &snack);

	if (tail != 4)
	{
		printf("\nOh no! The tail should be 4, but it's actually %d. :(\n", tail);
	}
	if (head != 10)
	{
		printf("\nOh no! The head should be 10, but it's actually %d. :(\n", head);
	}
	if (is_alive != 1)
	{
		printf("\nOh no! The is_alive variable should be 1, but it's actually %d. :(\n", is_alive);
	}
	if (snack != 'q')
	{
		printf("\nOh no! The snack should be 'q', but it's actually '%c'. :(\n", snack);
	}
	if (retval != 0)
	{
		printf("\nOh no! feed_glowworm() should have returned 0, but it returned %d. :(\n", retval);
	}

	return 0;
}
