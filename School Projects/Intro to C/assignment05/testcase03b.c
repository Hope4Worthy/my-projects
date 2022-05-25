// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment05: testcase03b.c
// ===========================
// FUNCTION TESTED: print_char_counts()
// OUTPUT FILE: sample_output/output03b.txt


#include <stdio.h>
#include <stdlib.h>

void print_char_counts(char **array, int num_strings, char ch);

int main(void)
{
	int num_strings = 4;

	// Create array to hold string pointers.
	char **array = malloc(sizeof(char *) * num_strings);

	// These are read-only strings. Attempting to modify them will crash your
	// program.
	array[0] = "Bobo";
	array[1] = "Harry";
	array[2] = "Potter";
	array[3] = "broom";

	print_char_counts(array, num_strings, '$');

	// Clean up the dynamically allocated array.
	free(array);

	return 0;
}
