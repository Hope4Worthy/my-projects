// Sean Szumlanski
// COP 3223, Fall 2019
//
// ==============
// print_glowie.c
// ==============
// This is one version of the print_glowie_dead_or_alive() function I wrote for Assignment #2.
// You are welcome to re-purpose this for Assignment #3. If you use any of this code directly, you
// should include a comment attributing it to me (to protect yourself in case your code gets flagged
// for plagiarism.)


#include <stdio.h>

void print_glowie_dead_or_alive(int tail_coordinate, int head_coordinate, int is_alive)
{
	int i;
	int num_spaces;
	int num_segments;
	int platform_length;

	// Note: The number of segments is (head - tail - 2) because (head - tail - 1) tells us
	// how many characters there are between the '~' and the 'G', and then we subtract an extra
	// 1 to account for the 'O' that's right before the 'G'. The remaining number there is the
	// number of small 'o' segments we need to print.

	num_spaces = tail_coordinate;
	num_segments = head_coordinate - tail_coordinate - 2;
	platform_length = head_coordinate + 1;

	for (i = 0; i < num_spaces; i++)
	{
		printf(" ");
	}

	printf("~");

	for (i = 0; i < num_segments; i++)
	{
		printf("o");
	}

	if (is_alive == 1)
	{
		printf("OG\n");
	}
	else
	{
		printf("Xx\n");
	}

	for (i = 0; i < platform_length; i++)
	{
		printf("=");
	}

	printf("\n\n");
}

int main(void)
{
	print_glowie_dead_or_alive(0, 3, 1);
	print_glowie_dead_or_alive(0, 4, 1);
	print_glowie_dead_or_alive(1, 4, 1);
	print_glowie_dead_or_alive(1, 5, 1);
	print_glowie_dead_or_alive(1, 6, 1);
	print_glowie_dead_or_alive(1, 7, 1);

	return 0;
}
