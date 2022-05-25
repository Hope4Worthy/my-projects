// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment03: testcase07a.c
// ===========================
// This test case calls your shrink_glowie() function. If that function works correctly, then the
// output produced by this program will match the output specified in sample_output/output07a.txt.


#include <stdio.h>

void shrink_glowie(int *head);

int main(void)
{
	int tail = 3, head = 9;

	shrink_glowie(&head);

	if (tail == 3 && head == 8)
	{
		printf("Hooray!\n");
	}
	else
	{
		printf("oh no :(\n");
	}

	return 0;
}
