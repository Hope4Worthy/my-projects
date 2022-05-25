// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment05: testcase01b.c
// ===========================
// FUNCTION TESTED: get_char_count()
// OUTPUT FILE: sample_output/output01b.txt


#include <stdio.h>
#include <stdlib.h>

int get_char_count(char *str, char ch);

int main(void)
{
	int result = get_char_count("Hello there!\n", '$');
	printf("%d\n", result);

	return 0;
}
