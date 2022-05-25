#include "Domichar.h"

#include <ctype.h>
#include <stdio.h>
#include <string.h>

int isVowel(char c)
{
	if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
	{
		return 1;
	}
	if(c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int isNonalphabetic(char c)
{
	if(isalpha(c))
	{
		return 0;
	}
	else
	{
		return 1;
	}
}

int isConsonant(char c)
{
	if(isVowel(c) || isNonalphabetic(c))
	{
		return 0;
	}
	else
	{
		return 1;
	}
}

void printDomichar(char *str)
{

	double string_length = 0;

	int num_const = 0;
	int num_vowel = 0;
	int num_non_letter = 0;
	int i = 0;

	double percent_const;
	double percent_vowel;
	double percent_non_letter;

	char current_char;

	for(i = 0; str[i] != '\0'; i++)
	{
		current_char = str[i];

		if(isConsonant(current_char))
		{
			num_const++;
		}
		else if(isVowel(current_char))
		{
			num_vowel++;
		}
		else if(isNonalphabetic(current_char))
		{
			num_non_letter++;
		}
		printf("%c", current_char);
	}

	string_length = i;

	if(num_vowel == num_non_letter && num_vowel == num_const)
	{
		printf(" (vc~)\n");
	}
	else if(num_vowel == num_non_letter && num_vowel > num_const) 
	{
		printf(" (v~)\n");
	}
	else if(num_const == num_non_letter && num_const > num_vowel)
	{
		printf(" (c~)\n");
	}
	else if(num_vowel == num_const && num_vowel > num_non_letter)
	{
		printf(" (vc)\n");
	}
	else if ((num_vowel / string_length) > 0.50)
	{
		printf(" (m:v)\n");
	}
	else if ((num_const / string_length) > 0.50)
	{
		printf(" (m:c)\n");
	}
	else if((num_non_letter / string_length) > 0.50)
	{
		printf(" (m:~)\n");
	}
	else if (num_vowel > num_const && num_vowel > num_non_letter)
	{
		printf(" (p:v)\n");
	}
	else if (num_const > num_vowel && num_const > num_non_letter)
	{
		printf(" (p:c)\n");
	}
	else if (num_non_letter > num_const && num_non_letter > num_vowel)
	{
		printf(" (p:~)\n");
	}
}

double difficultyRating(void)
{
	return 3;
}

double hoursSpent(void)
{
	return 5;
}


int main(int argc, char **argv)
{
	int i;
	for(i = 1; i < argc; i++)
	{
		printDomichar(argv[i]);
	}
	return 0;
}
