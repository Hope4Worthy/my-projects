// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2018

// ===========================
// assignment04: testcase03e.c
// ===========================
// FUNCTION TESTED: shift_letter()
// OUTPUT FILE: sample_output/output03e.txt


#include <stdio.h>

char shift_letter(char ch, int offset);

int main(void)
{
	char ch;

	printf("offset: -28\n");
	printf("===========\n");

	for (ch = 'a'; ch <= 'z'; ch++)
	{
		printf("%c -> %c\n", ch, shift_letter(ch, -28));
	}

	printf("\n");

	for (ch = 'A'; ch <= 'Z'; ch++)
	{
		printf("%c -> %c\n", ch, shift_letter(ch, -28));
	}

	return 0;
}
