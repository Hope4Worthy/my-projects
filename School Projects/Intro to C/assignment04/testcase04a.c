// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2018

// ===========================
// assignment04: testcase04a.c
// ===========================
// FUNCTION TESTED: cipher()
// INPUT FILE: sweater-plaintext.txt
// OUTPUT FILE: sample_output/output04a.txt


#include <stdio.h>

int cipher(char *filename, int key);

int main(void)
{
	int retval = cipher("sweater-plaintext.txt", 1);

	if (retval != 0)
	{
		printf("\nOh no. :( That didn't go as expected.\n");
	}

	return 0;
}
