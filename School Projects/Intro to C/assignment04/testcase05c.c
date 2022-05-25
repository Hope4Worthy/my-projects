// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2018

// ===========================
// assignment04: testcase05c.c
// ===========================
// FUNCTION TESTED: print_first_word_beginning_with_character()
// INPUT FILE: sweater-plaintext.txt
// OUTPUT FILE: sample_output/output05c.txt


#include <stdio.h>

int print_first_word_beginning_with_character(char *filename, char ch);

int main(void)
{
	int retval = print_first_word_beginning_with_character("sweater-plaintext.txt", 'm');

	if (retval != 0)
	{
		printf("\nOh no. :( That didn't go as expected.\n");
	}

	return 0;
}
