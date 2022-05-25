// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment02: testcase15.c
// ==========================
// Various tests of your print_glowie_dead_or_alive() function.


void print_glowie_dead_or_alive(int tail_coordinate, int head_coordinate, int is_alive);

int main(void)
{
	// These lines call your print_glowie_dead_or_alive() function. If it produces the correct
	// output (as specified in sample_output/output15.txt), and you will pass this test case.

	// Living glowies.
	print_glowie_dead_or_alive(0, 2, 1);
	print_glowie_dead_or_alive(0, 3, 1);
	print_glowie_dead_or_alive(0, 4, 1);
	print_glowie_dead_or_alive(1, 4, 1);
	print_glowie_dead_or_alive(2, 4, 1);
	print_glowie_dead_or_alive(2, 5, 1);
	print_glowie_dead_or_alive(2, 6, 1);

	// Same glowies as above, but no longer alive.
	print_glowie_dead_or_alive(0, 2, 0);
	print_glowie_dead_or_alive(0, 3, 0);
	print_glowie_dead_or_alive(0, 4, 0);
	print_glowie_dead_or_alive(1, 4, 0);
	print_glowie_dead_or_alive(2, 4, 0);
	print_glowie_dead_or_alive(2, 5, 0);
	print_glowie_dead_or_alive(2, 6, 0);

	return 0;
}
