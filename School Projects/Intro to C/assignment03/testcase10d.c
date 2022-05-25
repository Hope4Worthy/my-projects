// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment03: testcase10d.c
// ===========================
// This test case calls your print_magical_translocational_glowworm() function. If that function
// works correctly, then the output produced by this program will match the output specified in
// sample_output/output10d.txt.


#include <stdio.h>

void print_magical_translocational_glowworm(int tail, int head, int platform_length, int is_alive);

int main(void)
{
	// ~Xx
	// ======
	//
	print_magical_translocational_glowworm(0, 2, 6, 0);

	// ~oXx
	// ======
	//
	print_magical_translocational_glowworm(0, 3, 6, 0);

	// ~ooXx
	// ======
	//
	print_magical_translocational_glowworm(0, 4, 6, 0);

	// ~oooXx
	// ======
	//
	print_magical_translocational_glowworm(0, 5, 6, 0);

	//  ~oXx
	// ======
	//
	print_magical_translocational_glowworm(1, 4, 6, 0);

	//   ~oXx
	// ======
	//
	print_magical_translocational_glowworm(2, 5, 6, 0);

	//  ~ooXx
	// =======
	//
	print_magical_translocational_glowworm(1, 5, 7, 0);

	//  ~oooXx
	// =======
	//
	print_magical_translocational_glowworm(1, 6, 7, 0);

	return 0;
}
