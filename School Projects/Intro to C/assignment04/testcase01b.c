// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2018

// ===========================
// assignment04: testcase01b.c
// ===========================
// FUNCTION TESTED: is_consonant()
// OUTPUT FILE: sample_output/output01b.txt


#include <stdio.h>

int is_consonant(char ch);

int main(void)
{
	char ch;

	ch = '9';
	printf("is_consonant('%c'): %d\n", ch, is_consonant(ch));

	ch = '.';
	printf("is_consonant('%c'): %d\n", ch, is_consonant(ch));

	ch = ' ';
	printf("is_consonant('%c'): %d\n", ch, is_consonant(ch));

	ch = 'T';
	printf("is_consonant('%c'): %d\n", ch, is_consonant(ch));

	return 0;
}
