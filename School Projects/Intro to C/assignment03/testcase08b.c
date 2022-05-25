// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment03: testcase08b.c
// ===========================
// This test case calls your move_glowie_forward() function. If that function works
// correctly, then the output produced by this program will match the output specified
// in sample_output/output08b.txt.


#include <stdio.h>

void move_glowie_forward(int *tail, int *head);

int main(void)
{
	int tail = 3, head = 5;

	move_glowie_forward(&tail, &head);

	if (tail == 4 && head == 6)
	{
		printf("Hooray!\n");
	}
	else
	{
		printf("oh no :(\n");
	}

	return 0;
}
