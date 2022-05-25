// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment05: testcase03c.c
// ===========================
// FUNCTION TESTED: print_char_counts()
// OUTPUT FILE: sample_output/output03c.txt


#include <stdio.h>
#include <stdlib.h>

void print_char_counts(char **array, int num_strings, char ch);

int main(void)
{
	int num_strings = 3;

	// Create array to hold string pointers.
	char **array = malloc(sizeof(char *) * num_strings);

	// These are read-only strings. Attempting to modify them will crash your
	// program.
	array[0] = "The next string is empty.";
	array[1] = "";
	array[2] = "This is the last string in the array.";

	print_char_counts(array, num_strings, ' ');

	// Clean up the dynamically allocated array.
	free(array);

	return 0;
}
