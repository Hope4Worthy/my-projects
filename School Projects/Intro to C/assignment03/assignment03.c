// name - COP 3223H - Fall 2019 - br7153

#include "assignment03.h"
#include <stdio.h>

void sort_ascending(int *a, int *b, int *c)
{
	int temp;
	if(*a <= *c && *c <= *b) // a<c<b
	{
		temp = *b;
		*b = *c;
		*c = temp;
	}

	else if(*b <= *a && *a <= *c) // b<a<c
	{
		temp = *a;
		*a = *b;
		*b = temp;
	}

	else if(*b <= *c && *c <= *a) // b<c<a
	{
		temp = *c;
		*c = *a;
		*a = *b;
		*b = temp;

	}

	else if(*c <= *a && *a <= *b) // c<a<b
	{
		temp = *b;
		*b = *a;
		*a = *c;
		*c = temp;
	}

	else if(*c <= *b && *b <= *a) //c<b<a
	{
		temp = *a;
		*a = *c;
		*c = temp;
	}

	return;
}

void sort_ascending_with_repeats_allowed(int *a, int *b, int *c)
{
	sort_ascending(a, b, c);
}

void sort_descending(int *a, int *b, int *c)
{
	sort_ascending(c, b, a);
}

void sort_descending_with_repeats_allowed(int *a, int *b, int *c)
{
	sort_ascending(c, b, a);
}

int *get_pointer_to_median(int *a, int *b, int *c)
{
	if(*a <= *b && *b <= *c || *c <= *b && *b <= *a) // b is median
	{
		return b;
	}

	else if(*b <= *a && *a <= *c || *c <= *a && *a <= *b) // a is median
	{
		return a;
	}

	else // c is median
	{
		return c;

	}
}

void grow_glowie(int *head)
{
	*head = *head + 1;
}

void shrink_glowie(int *head)
{
	*head = *head - 1;
}

void move_glowie_forward (int *tail, int *head)
{
	*tail = *tail + 1;
	*head = *head + 1;
}

int feed_glowworm(int *tail, int *head, int *is_alive, char *snack)
{
	int snack_eaten_flag;
	if(*snack == 'o' || *snack == 'O' || *snack == '@')
	{
		grow_glowie(head);
		printf("Glowworm munches on a snack that causes it to grow! Om nom nom.\n");
		snack_eaten_flag = 1;
	}

	else if(*snack == 's' || *snack == 'S') 
	{
		shrink_glowie(head);
		printf("Glowworm munches on a snack that causes it to shrink!\n");
		snack_eaten_flag = 1;
	}

	else if(*snack == '-' || *snack == '=')
	{
		move_glowie_forward(tail, head);
		printf("Glowworm feels energetic after its snack and inches forward!\n");
		snack_eaten_flag = 1;
	}

	else if(*snack == 'x' || *snack == 'X' || *snack == '%')
	{
		*is_alive = 0;
		printf("That snack poisoned the glowworm. SAD.\n");
		snack_eaten_flag = 1;
	}
	else
	{
		printf("The glowworm looks at the snack skeptically.\n");
		snack_eaten_flag = 0;
	}
	if (snack_eaten_flag)
	{
		*snack = ' ';
	}
	if (*is_alive == 0 || snack_eaten_flag == 0)
	{
		return 0;
	}
	else
	{
		return 1;
	}
}

void print_platform (int platform_length)
{
	printf("\n");
	int i;
	for (i = 0; i < platform_length; i++)
	{
		printf("=");
	}
	printf("\n\n");
}

void print_spaces(int num_spaces)
{
	int i;
	for(i = 0; i < num_spaces; i++)
	{
		printf(" ");	
	}
}

void print_segments(int num_segments)
{
	int i;
	for(i = 0; i < num_segments; i++)
	{
		printf("o");	
	}
}

void print_head(int is_alive)
{
	if(is_alive == 1)
		{
			printf("OG");
		}

		else
		{
			printf("Xx");
		}
	
}
void print_magical_translocational_glowworm(int tail, int head, int platform_length, int is_alive)
{
		int num_segments;
		int num_spaces;
		int wrapped_chars;
		int unwrapped_chars;
		int total_segments;

	if(tail < head)
	{

		num_spaces = tail;
		num_segments = head - tail - 2;

		print_spaces(num_spaces);
		printf("~");
		print_segments(num_segments);
		print_head(is_alive);
		print_platform(platform_length);
	}
	if(head < tail)
	{
		if(head < 1)
		{
			head = 1;
		}

		if(tail > platform_length - 1)
		{
			tail = platform_length - 1;
		}

		num_spaces = tail - head -1;
		unwrapped_chars = platform_length - tail - 1;
		wrapped_chars = head - 1;

		if(wrapped_chars < 0)
		{
			wrapped_chars = 0;
		}

		if(unwrapped_chars < 0)
		{
			unwrapped_chars = 0;
		}

		print_segments(wrapped_chars);
		print_head(is_alive);
		print_spaces(num_spaces);
		printf("~");
		print_segments(unwrapped_chars);
		print_platform(platform_length);
	}
}

double difficulty_rating(void)
{
	return 4.0;
}

double hours_invested(void)
{
	return 6.0;
}

double prior_experience(void)
{
	return 4.0;
}

int main(void)
{
	int tail = 0;
	int head = 0;
	int platform = 0;
	int alive = 0;

	while(tail != 999 && head != 999 && platform != 999 && alive != 999)
	{
	printf("tail:");
	scanf("%d",&tail);
	printf("head:");
	scanf("%d",&head);
	printf("platform:");
	scanf("%d",&platform);
	printf("alive:");
	scanf("%d",&alive);

	print_magical_translocational_glowworm(tail, head, platform, alive);
	}

	return 0;
}
