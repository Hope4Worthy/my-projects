// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase01.c
// ==========================
// This test case verifies that your return_five() function is implemented correctly.


#include <stdio.h>

int return_five(void);

int main(void)
{
	// This line calls your return_five() function. If that function returns 5, this program will
	// produce the correct output (as specified in sample_output/output01.txt), and you will pass
	// this test case.
	int result = return_five();

	printf("The function returned: %d\n\n", result);

	if (result == 5)
		printf("Hooray!\n");
	else
		printf("failwhale :(\n");

	return 0;
}
