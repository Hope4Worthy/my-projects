// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2018

// ===========================
// assignment04: testcase04e.c
// ===========================
// FUNCTION TESTED: cipher()
// OUTPUT FILE: sample_output/output04e.txt


#include <stdio.h>

int cipher(char *filename, int key);

int main(void)
{
	int retval = cipher("this-file-should-not-exist.txt", 5);

	if (retval != -1)
	{
		printf("\nOh no. :( That didn't go as expected.\n");
	}

	return 0;
}
