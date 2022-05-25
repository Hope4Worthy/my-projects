// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2018

// ===========================
// assignment04: testcase01c.c
// ===========================
// FUNCTION TESTED: is_consonant()
// OUTPUT FILE: sample_output/output01c.txt


#include <stdio.h>

int is_consonant(char ch);

int main(void)
{
	char ch;

	for (ch = 91; ch <= 126; ch++)
	{
		printf("is_consonant('%c'): %d\n", ch, is_consonant(ch));
	}

	return 0;
}
