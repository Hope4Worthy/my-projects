// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment05: testcase01a.c
// ===========================
// FUNCTION TESTED: get_char_count()
// OUTPUT FILE: sample_output/output01a.txt


#include <stdio.h>
#include <stdlib.h>

int get_char_count(char *str, char ch);

int main(void)
{
	int result = get_char_count("Hello there!\n", 'e');
	printf("%d\n", result);

	return 0;
}
