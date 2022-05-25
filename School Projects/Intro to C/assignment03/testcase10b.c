// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment03: testcase10b.c
// ===========================
// This test case calls your print_magical_translocational_glowworm() function. If that function
// works correctly, then the output produced by this program will match the output specified in
// sample_output/output10b.txt.


#include <stdio.h>

void print_magical_translocational_glowworm(int tail, int head, int platform_length, int is_alive);

int main(void)
{
	// oooOG  ~oo
	// ==========
	//
	print_magical_translocational_glowworm(7, 4, 10, 1);

	// oooOG   ~o
	// ==========
	//
	print_magical_translocational_glowworm(8, 4, 10, 1);

	// oooOG    ~
	// ==========
	//
	print_magical_translocational_glowworm(9, 4, 10, 1);

	return 0;
}
