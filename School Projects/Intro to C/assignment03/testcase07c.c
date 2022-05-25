// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment03: testcase07c.c
// ===========================
// This test case calls your shrink_glowie() function. If that function works correctly, then the
// output produced by this program will match the output specified in sample_output/output07c.txt.


#include <stdio.h>

void shrink_glowie(int *head);

int main(void)
{
	int tail = 0, head = 3;

	shrink_glowie(&head);

	if (tail == 0 && head == 2)
	{
		printf("Hooray!\n");
	}
	else
	{
		printf("oh no :(\n");
	}

	return 0;
}
