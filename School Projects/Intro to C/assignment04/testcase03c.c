// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2018

// ===========================
// assignment04: testcase03c.c
// ===========================
// FUNCTION TESTED: shift_letter()
// OUTPUT FILE: sample_output/output03c.txt


#include <stdio.h>

char shift_letter(char ch, int offset);

int main(void)
{
	char ch;

	printf("offset: 26\n");
	printf("==========\n");

	for (ch = 'a'; ch <= 'z'; ch++)
	{
		printf("%c -> %c\n", ch, shift_letter(ch, 26));
	}

	printf("\n");

	for (ch = 'A'; ch <= 'Z'; ch++)
	{
		printf("%c -> %c\n", ch, shift_letter(ch, 26));
	}

	return 0;
}
