#include "assignment05.h"
#include <stdio.h>
#include <string.h>

int get_char_count(char *str, char ch) // test case 1
{
	int i;
	int instances_of_ch = 0;
	if(strlen(str) != 0)
	{
		for(i = 0; str[i] != '\0'; i++)
		{
			if(str[i] == ch)
			{
				instances_of_ch++;
			}
		}

	}
	else
	{
		return 0;
	}
	return instances_of_ch;
}

void print_char_count(char *str, char ch) // test case 2
{
	printf("%d\n", get_char_count(str, ch));
	return;
}

void print_char_counts(char **array, int num_strings, char ch) // test case 3
{
	int i;
	int num;
	for(i = 0; i < num_strings; i++)
	{
		num = get_char_count(array[i], ch);

		printf("%s (%d occurrence", array[i], num);

		if(num == 1)
		{
			printf(" of \'%c\')\n", ch);
		}
		else
		{
			printf("s of \'%c\')\n", ch);
		}
	}
	return;
}

void copy_string_reverse(char *destination, char *source) // test case 4
{
	int loop_count_1 = strlen(source) - 1;
	int loop_count_2 = 0;

	if(loop_count_1 == 0)
	{
		printf("zero\n");
		destination[0] = '\0';
		return;
	}
	while(loop_count_1 >= 0)
	{
		destination[loop_count_2] = source[loop_count_1];
		loop_count_1--;
		loop_count_2++;
	}
	destination[loop_count_2] = '\0';
	return;
}

void print_specific_row(int **array, int num_rows, int num_cols, int which_row) // test case 5
{
	int i;
	if(which_row >= num_rows || which_row < 0)
	{
		printf("Invalid row index!\n");
		return;
	}
	else
	{
		for(i = 0; i < num_cols; i++)
		{
			printf("%d\n", array[which_row][i]);
		}
	}
	return;
}

void print_specific_row_comma_separated(int **array, int num_rows, int num_cols, int which_row) // test case 6
{
	int i;
	if(which_row >= num_rows || which_row < 0)
	{
		printf("Invalid row index!\n");
		return;
	}
	else
	{
		for(i = 0; i < (num_cols - 1); i++)
		{
			printf("%d, ", array[which_row][i]);
		}
		printf("%d\n", array[which_row][i]);
	}
	return;
}

void print_specific_column_in_reverse(int **array, int num_rows, int num_cols, int which_col) // test case 7
{
	int i;

	if(which_col >= num_cols)
	{
		printf("Invalid column index!\n");
		return;
	}

	else
	{
		for(i = num_rows - 1; i >= 0; i--)
		{
			printf("%d\n", array[i][which_col]);
		}

	}
	return;
	
}

void fill_matrix(int **array, int num_rows, int num_cols, int fill_value) // test case 8
{
	int i;
	int j;
	for(i = 0; i < num_rows; i++)
	{
		for(j = 0; j < num_cols; j++)
		{
			array[i][j] = fill_value;
		}
	}
	return;
}

void checker_matrix(int **array, int num_rows, int num_cols) // test case 9
{
	int i;
	int j;
	for(i = 0; i < num_rows; i++)
	{
		if((i % 2) == 0)
		{
			for(j = 0; j < num_cols; j++)
			{
				if((j % 2) == 0)
				{
					array[i][j] = 0;
				}
				else
				{
					array[i][j] = 1;
				}
			}
		}
		else
		{
			for(j = 0; j < num_cols; j++)
			{
				if((j % 2) == 0)
				{
					array[i][j] = 1;
				}
				else
				{
					array[i][j] = 0;
				}
			}
		}
	}
}

double difficulty_rating(void) // test case 10
{
	return 3;
}

double hours_invested(void) // test case 10
{
	return 4;
}

double prior_experience(void) // test case 10
{
	return 4;
}
