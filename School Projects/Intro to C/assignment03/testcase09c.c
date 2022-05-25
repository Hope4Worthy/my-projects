// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment03: testcase09c.c
// ===========================
// This test case calls your feed_glowworm() function. If that function works correctly, then the
// output produced by this program will match the output specified in sample_output/output09c.txt.


#include <stdio.h>

int feed_glowworm(int *tail, int *head, int *is_alive, char *snack);

int main(void)
{
	int tail = 4, head = 10, is_alive = 1, retval;
	char snack = '=';

	// This should cause the glowworm to inch forward.
	retval = feed_glowworm(&tail, &head, &is_alive, &snack);

	if (tail != 5)
	{
		printf("\nOh no! The tail should be 5, but it's actually %d. :(\n", tail);
	}
	if (head != 11)
	{
		printf("\nOh no! The head should be 11, but it's actually %d. :(\n", head);
	}
	if (is_alive != 1)
	{
		printf("\nOh no! The is_alive variable should be 1, but it's actually %d. :(\n", is_alive);
	}
	if (snack != ' ')
	{
		printf("\nOh no! The snack should be ' ', but it's actually '%c'. :(\n", snack);
	}
	if (retval != 1)
	{
		printf("\nOh no! feed_glowworm() should have returned 1, but it returned %d. :(\n", retval);
	}

	return 0;
}
