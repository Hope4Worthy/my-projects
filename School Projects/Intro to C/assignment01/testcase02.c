// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment01: testcase02.c
// ==========================
// This test case verifies that your pancake_printer() function is implemented correctly.


#include <stdio.h>

int pancake_printer(void);

int main(void)
{
	// This line calls your pancake_printer() function. If that function produces the correct
	// output and returns the correct value, this test case will pass.
	int result = pancake_printer();

	if (result == 52847)
		printf("\nHooray!\n");
	else
		printf("\nfailwhale :(\n");

	return 0;
}
