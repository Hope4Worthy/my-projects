// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2018

// ===========================
// assignment04: testcase02b.c
// ===========================
// FUNCTION TESTED: is_terminating_punctuator()
// OUTPUT FILE: sample_output/output02b.txt


#include <stdio.h>

int is_terminating_punctuator(char ch);

int main(void)
{
	char ch;

	ch = '9';
	printf("is_terminating_punctuator('%c'): %d\n", ch, is_terminating_punctuator(ch));

	ch = '.';
	printf("is_terminating_punctuator('%c'): %d\n", ch, is_terminating_punctuator(ch));

	ch = ' ';
	printf("is_terminating_punctuator('%c'): %d\n", ch, is_terminating_punctuator(ch));

	ch = 'T';
	printf("is_terminating_punctuator('%c'): %d\n", ch, is_terminating_punctuator(ch));

	return 0;
}
