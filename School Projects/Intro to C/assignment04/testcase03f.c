// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2018

// ===========================
// assignment04: testcase03f.c
// ===========================
// FUNCTION TESTED: shift_letter()
// OUTPUT FILE: sample_output/output03f.txt


#include <stdio.h>

char shift_letter(char ch, int offset);

int main(void)
{
	char ch;

	printf("offset: 1\n");
	printf("=========\n");

	for (ch = 91; ch <= 126; ch++)
	{
		printf("%c -> %c\n", ch, shift_letter(ch, 1));
	}

	return 0;
}
