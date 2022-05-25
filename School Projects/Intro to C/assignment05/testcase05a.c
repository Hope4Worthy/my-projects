// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


// Sean Szumlanski
// COP 3223, Fall 2019

// ===========================
// assignment05: testcase05a.c
// ===========================
// FUNCTION TESTED: print_specific_row()
// OUTPUT FILE: sample_output/output05a.txt


#include <stdio.h>
#include <stdlib.h>

void print_specific_row(int **array, int num_rows, int num_cols, int which_row);

void print_int_matrix(int **array, int num_rows, int num_cols, int field_width)
{
	int i, j;

	for (i = 0; i < num_rows; i++)
	{
		for (j = 0; j < num_cols; j++)
		{
			printf("%*d", field_width, array[i][j]);
		}
		printf("\n");
	}
}

int **create_int_matrix(int num_rows, int num_cols)
{
	int i;

	int **array = malloc(sizeof(int *) * num_rows);

	for (i = 0; i < num_rows; i++)
	{
		array[i] = malloc(sizeof(int) * num_cols);
	}

	return array;
}

void destroy_int_matrix(int **array, int num_rows)
{
	int i;

	for (i = 0; i < num_rows; i++)
	{
		free(array[i]);
	}

	free(array);
}

void copy_array(int *target, int *source, int n)
{
	int i;

	for (i = 0; i < n; i++)
	{
		target[i] = source[i];
	}
}

int main(void)
{
	int num_rows = 2, num_cols = 3, **array;

	int row0[] = {9, 12, 7};
	int row1[] = {4, 1, 8};

	// This effectively creates the following 2x3 array:
	//
	//   9  12  7
	//   4   1  8

	array = create_int_matrix(num_rows, num_cols);
	copy_array(array[0], row0, num_cols);
	copy_array(array[1], row1, num_cols);

	// Here's the main event.
	print_specific_row(array, 2, 3, 0);

	// Clean up dynamically allocated memory.
	destroy_int_matrix(array, num_rows);

	return 0;
}
