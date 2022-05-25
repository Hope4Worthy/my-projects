// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2018

// ===========================
// assignment04: testcase05f.c
// ===========================
// FUNCTION TESTED: print_first_word_beginning_with_character()
// OUTPUT FILE: sample_output/output05f.txt


#include <stdio.h>

int print_first_word_beginning_with_character(char *filename, char ch);

int main(void)
{
	int retval = print_first_word_beginning_with_character("this-file-should-not-exist.txt", 'q');

	if (retval != -1)
	{
		printf("\nOh no. :( That didn't go as expected.\n");
	}

	return 0;
}
