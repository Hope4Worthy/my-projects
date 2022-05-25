// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ==========================
// assignment02: testcase14.c
// ==========================
// Various tests of your print_glowie_from_coordinates() function.


void print_glowie_from_coordinates(int tail_coordinate, int head_coordinate);

int main(void)
{
	// These lines call your print_glowie_from_coordinates() function. If it produces the correct
	// output (as specified in sample_output/output14.txt), and you will pass this test case.
	print_glowie_from_coordinates(0, 2);
	print_glowie_from_coordinates(0, 3);
	print_glowie_from_coordinates(0, 4);
	print_glowie_from_coordinates(1, 4);
	print_glowie_from_coordinates(2, 4);
	print_glowie_from_coordinates(2, 5);
	print_glowie_from_coordinates(2, 6);

	return 0;
}
