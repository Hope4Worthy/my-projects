#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include "assignment04.h"

int is_consonant(char ch) // test case 1
{
	if (!isalpha(ch))
	{
		return 0;
	}
	else if(ch == 'a' || ch == 'e' || ch == 'i'|| ch == 'o' || ch == 'u')
	{
		return 0;
	}
	else if(ch == 'A' || ch == 'E' || ch == 'I'|| ch == 'O' || ch == 'U')
	{
		return 0;
	}
	else
	{
		return 1;
	}
}

int is_terminating_punctuator(char ch) // test case 2
{
	if(!ispunct(ch))
	{
		return 0;
	}
	else if(ch == '?' || ch == '.' || ch == '!')
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

char shift_letter(char letter, int offset) // test case 3
{
	char shifted_letter = letter;
	int i;
	if(letter >= 'a' && letter <= 'z')
	{
		if(offset > 0)
		{
			for(i = 0; i < offset; i++)
			{
				shifted_letter += 1;
				if (shifted_letter > 'z')
				{
					shifted_letter = 'a';
				}
			}
		}
		else if(offset < 0)
		{
			for(i = 0; i > offset; i--)
			{
				shifted_letter -= 1;
				if (shifted_letter < 'a')
				{
					shifted_letter = 'z';
				}
			}
		}
	}
	else if(letter >='A' && letter <= 'Z')
	{
		if(offset > 0)
		{
			for(i = 0; i < offset; i++)
			{
				shifted_letter += 1;
				if (shifted_letter > 'Z')
				{
					shifted_letter = 'A';
				}
			}
		}
		else if(offset < 0)
		{
			for(i = 0; i > offset; i--)
			{
				shifted_letter -= 1;
				if (shifted_letter < 'A')
				{
					shifted_letter = 'Z';
				}
			}
		}
	}
	else
	{
		shifted_letter = letter;
	}
	return shifted_letter;
}

int cipher(char *filename, int key) // test case 4
{
	FILE *input_file = fopen(filename , "r");
	char ch;

	if(input_file == NULL)
	{
		printf("Could not open file. Womp womp. :(\n");
		return -1;
	}

	while(fscanf(input_file, "%c",&ch) != EOF)
	{
		printf("%c", shift_letter(ch, key));
	}
	fclose(input_file);
	return 0;
}

int print_first_word_beginning_with_character (char *filename, char ch) //test case 5
{
	int first_read_flag = 1;
	int word_found_flag = 0;
	FILE *input_file;
	char ch1;
	char last_ch;
	if((input_file = fopen(filename, "r")) == NULL)
	{
		printf("Could not open file. Womp womp. :(\n");
		return -1;
	}
	while((fscanf(input_file, "%c", &ch1)) != EOF)
	{
		if((ch1 == ch && last_ch == ' ') || (first_read_flag && ch1 == ch))
		{
			printf("%c", ch1);
			for(fscanf(input_file, "%c", &ch1); !isspace(ch1); fscanf(input_file, "%c", &ch1))
			{
				printf("%c", ch1);
			}
			printf("\n");
			word_found_flag = 1;
		}
		last_ch = ch1;
		first_read_flag = 0;
	}
	fclose(input_file);
	if(word_found_flag == 1)
	{
		fclose(input_file);
		return 0;
	}
	else
	{
		printf("No such word in input file. :(\n");
		return -1;
	}
}

double difficulty_rating(void) // test case 6
{
	return 3;
}

double hours_invested (void) // test case 7
{
	return 2;
}

double prior_experience(void) // test case 8
{
	return 4;
}

int main(void)
{
	print_first_word_beginning_with_character("sweater-plaintext.txt", 'd');
}