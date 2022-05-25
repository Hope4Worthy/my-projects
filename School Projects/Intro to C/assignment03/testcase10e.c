// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment03: testcase10e.c
// ===========================
// This test case calls your print_magical_translocational_glowworm() function. If that function
// works correctly, then the output produced by this program will match the output specified in
// sample_output/output10e.txt.


#include <stdio.h>

void print_magical_translocational_glowworm(int tail, int head, int platform_length, int is_alive);

int main(void)
{
	// oooXx  ~oo
	// ==========
	//
	print_magical_translocational_glowworm(7, 4, 10, 0);

	// oooXx   ~o
	// ==========
	//
	print_magical_translocational_glowworm(8, 4, 10, 0);

	// oooXx    ~
	// ==========
	//
	print_magical_translocational_glowworm(9, 4, 10, 0);

	// Xx   ~
	// ======
	//
	print_magical_translocational_glowworm(5, 1, 6, 0);

	// Xx  ~o
	// ======
	//
	print_magical_translocational_glowworm(4, 1, 6, 0);

	// Xx ~oo
	// ======
	//
	print_magical_translocational_glowworm(3, 1, 6, 0);

	// Xx~ooo
	// ======
	//
	print_magical_translocational_glowworm(2, 1, 6, 0);

	//  ~oooXx
	// =======
	//
	print_magical_translocational_glowworm(1, 6, 7, 0);

	return 0;
}
