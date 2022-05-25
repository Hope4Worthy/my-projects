// name - COP 3223H - Fall 2019 - br727153

//#include "assignment02.h"
#include <stdio.h>

void print_one_through_n (int n) // Case 1
{
	int count;
	for(count = 1; count <= n; count ++)
	{
		printf("%d\n", count);
	}
	return;
}

void print_n_through_one (int n) // Case 2
{
	while (n >= 1)
	{
		printf("%d\n", n);
		n--;
	}
	return;
}

void PrintSpaces (int spaces) // Helper
{
	while(spaces > 0)
	{
		printf(" ");
		spaces--;
	}
}

void tada (int n) // Case 3
{
	int spaces = 0;
	int count = 1;
	while (count <= n)
	{
		PrintSpaces(spaces);
		printf("%d...\n", count);
		count++;
		spaces = count - 1;

	}
	PrintSpaces(spaces);
	printf("Tada!\n");
	return;
}

void print_multiples_of_ten (int n) // Case 4
{
	int count;
	int math;
	for (int count = 1; count <= n; count++)
	{
		math = 10 * count;
		printf("%d\n", math);
	}
	return;
}

void print_comma_separated_multiples_of_ten (int n) // Case 5
{
	int count;
	int math;
	for (int count = 1; count <= n; count++)
	{
		math = 10 * count;
		printf("%d, ", math);
	}
	printf("\n");
	return;
}

void print_comma_separated_multiples_of_ten_fancy (int n) // Case 6
{
	int count;
	int math;
	for (int count = 1; count <= n; count++)
	{
		math = 10 * count;
		printf("%d", math);
		if(count != n)
		{
			printf(", ");
		}
		else
		{
			printf("\n");
		}
	}
	return;
}

void print_duet_symmetric (int n, char yin, char yang) // Case 7
{
	int count;
	for (count = 0; count < n; count ++)
	{
		printf("%c", yin);
	}
	for (count = 0; count < n; count ++)
	{
		printf("%c", yang);
	}
	printf("\n");
	return;
}

void print_duet (int m, int n, char yin, char yang) // Case 8
{
	int count;
	for (count = 0; count < m; count ++)
	{
		printf("%c", yin);
	}
	for (count = 0; count < n; count ++)
	{
		printf("%c", yang);
	}
	printf("\n");
	return;
}

void print_duet_half_and_half (int n, char yin, char yang) // Case 9
{
	int Half_N = n / 2;
	print_duet_symmetric(Half_N, yin, yang);
	return;
}

void print_duet_with_yin_dominating (int n, char yin, char yang) // Case 10
{
	int CountYin;
	int CountYang;
	if((n % 2) == 0)
	{
		CountYin = n / 2;
		CountYang = CountYin;
	}
	else
	{
		CountYin = (n / 2) + 1;
		CountYang = n / 2;
	}
	print_duet(CountYin, CountYang, yin, yang);
	return;
}

void print_duet_with_yang_dominating (int n, char yin, char yang) // Case 11
{
	int CountYin;
	int CountYang;
	if((n % 2) == 0)
	{
		CountYin = n / 2;
		CountYang = CountYin;
	}
	else
	{
		CountYang = (n / 2) + 1;
		CountYin = n / 2;
	}
	print_duet(CountYin, CountYang, yin, yang);
	return;
}

void print_glowie_basic (int num_spaces, int num_segments) // Case 12
{
	while(num_spaces > 0)
	{
		printf(" ");
		num_spaces--;
	}
	printf("~");
	while(num_segments > 0)
	{
		printf("o");
		num_segments--;
	}
	printf("OG\n");
	return;
}

void print_glowie_with_platform (int num_spaces, int num_segments) // Case 13
{
	if(num_spaces < 0)
	{
		num_spaces = 0;
	}
	int CharUsed = num_spaces + num_segments + 2;
	print_glowie_basic(num_spaces, num_segments);
	if(num_segments < 0)
	{
		CharUsed = num_spaces + 2;
	}
	while (CharUsed >= 0)
	{
		printf("=");
		CharUsed--;
	}
	printf("\n\n");
	return;
}

void print_glowie_from_coordinates (int tail_coordinate, int Head_coordinate) // Case 14
{
	int num_spaces = tail_coordinate;
	if (num_spaces < 0)
	{
		num_spaces = 0;
	}
	int num_segments = Head_coordinate - 2 - num_spaces;
	print_glowie_with_platform(num_spaces, num_segments);
}

void print_glowie_dead_or_alive (int tail_coordinate, int Head_coordinate, int is_alive) // Case 15
{
	int num_spaces = tail_coordinate;
	if (num_spaces < 0)
	{
		num_spaces = 0;
	}
	int num_segments = Head_coordinate - 2 - num_spaces;
	int CharUsed = num_spaces + num_segments + 2;
	if(num_segments < 0)
	{
		CharUsed = num_spaces + 2;
	}
	while(num_spaces > 0)
	{
		printf(" ");
		num_spaces--;
	}
	printf("~");
	while(num_segments > 0)
	{
		printf("o");
		num_segments--;
	}
	if (is_alive == 1)
	{
		printf("OG\n");	
	}
	else
	{
		printf("Xx\n");
	}
	
	while (CharUsed >= 0)
	{
		printf("=");
		CharUsed--;
	}
	printf("\n\n");
	return;
}

double difficulty_rating(void) // Case 16
{
	return 2;
}

double hours_invested(void) // Case 17
{
	return 2;
}

double prior_experience(void) // Case 18
{
	return 4;
}

int main (void)
{
	int i = 0;
	int tail_coordinate;
	int Head_coordinate;
	int is_alive;
	 while (i == 0)
	 {
	 	printf("Input Glowie Tail Cordinate\n");
	 	scanf("%d", &tail_coordinate);
	 	printf("Input Head Cordinate\n");
	 	scanf("%d", &Head_coordinate);
	 	printf("Dead or Alive\n");
	 	scanf("%d", &is_alive);
	 	if (tail_coordinate == 999 && Head_coordinate == 999)
	 	{
	 		i = -1;
	 	}
	 	else
	 	{
	 		i = 0;
	 		print_glowie_dead_or_alive(tail_coordinate, Head_coordinate, is_alive);
	 	}

	 }
}
