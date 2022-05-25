// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment03: testcase10a.c
// ===========================
// This test case calls your print_magical_translocational_glowworm() function. If that function
// works correctly, then the output produced by this program will match the output specified in
// sample_output/output10a.txt.


#include <stdio.h>

void print_magical_translocational_glowworm(int tail, int head, int platform_length, int is_alive);

int main(void)
{
	// ~OG
	// ======
	//
	print_magical_translocational_glowworm(0, 2, 6, 1);

	// ~oOG
	// ======
	//
	print_magical_translocational_glowworm(0, 3, 6, 1);

	// ~ooOG
	// ======
	//
	print_magical_translocational_glowworm(0, 4, 6, 1);

	// ~oooOG
	// ======
	//
	print_magical_translocational_glowworm(0, 5, 6, 1);

	//  ~oOG
	// ======
	//
	print_magical_translocational_glowworm(1, 4, 6, 1);

	//   ~oOG
	// ======
	//
	print_magical_translocational_glowworm(2, 5, 6, 1);

	//  ~ooOG
	// =======
	//
	print_magical_translocational_glowworm(1, 5, 7, 1);

	//  ~oooOG
	// =======
	//
	print_magical_translocational_glowworm(1, 6, 7, 1);

	return 0;
}
