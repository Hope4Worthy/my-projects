/* 
	This is the lex.c file for the UCF Fall 2021 Systems Software Project.
	For HW2, you must implement the function lexeme *lexanalyzer(char *input).
	You may add as many constants, global variables, and support functions
	as you desire.
	
	If you choose to alter the printing functions or delete list or lex_index, 
	you MUST make a note of that in you readme file, otherwise you will lose 
	5 points.

	lexanalyzer() edited by
	&
	isspecial, createEntry, getValue, getType created by
	
	name
*/

#include <limits.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "compiler.h"
#define MAX_NUMBER_TOKENS 500
#define MAX_IDENT_LEN 11
#define MAX_NUMBER_LEN 5

lexeme *list;
int lex_index;

void printlexerror(int type);
void printtokens();
int isspecial(char c);
lexeme createEntry(char *s);
int getValue(char* s);
token_type getType(char* s);
int isOp(char* o);

lexeme *lexanalyzer(char *input, int printFlag)
{
	lexeme *tokens = malloc(sizeof(lexeme) * MAX_NUMBER_TOKENS);
	lex_index = 0;
	char temp [MAX_IDENT_LEN + 1]; // temp for token name

	char c; // working char
	int i = 0;
	int j;

	while(i < MAX_NUMBER_TOKENS)
	{
		c = input[i];

		if(c == '/') // possible comment detected
		{
			i++;
			if(input[i] == '/') // comment detected
			{
				for(;input[i] != '\n'; i++); // skip to new line
				continue;
			}
			else // divSym
			{
				temp[0] = c;
				tokens[lex_index] = createEntry(temp);
				lex_index++;
				memset(temp, 0, strlen(temp)); // clear temp
			}
		}
		else if(isalpha(c)) // word detected
		{
			j = 0;
			do
			{
				if(j > MAX_IDENT_LEN) // identifier too leng
				{
					printlexerror(4);
					return NULL;
				}

				if(isalnum(c))
				{
					temp[j] = c;
				}

				i++;
				j++;

				c = input[i];
			}
			while(isalnum(c));

			tokens[lex_index] = createEntry(temp); // create lexeme entry
			lex_index++; // move token pointer
			memset(temp, 0, strlen(temp)); // clear temp
		}
		else if(isdigit(c)) // number detected
		{
			j = 0;
			do
			{
				if(j > MAX_NUMBER_LEN) // number too leng
				{
					printlexerror(3);
					return NULL;
				}

				temp[j] = c;

				i++;
				j++;
				
				c = input[i];
			}
			while(isdigit(c));

			if(isalpha(c))
			{
				printlexerror(2);
				return NULL;
			}

			tokens[lex_index] = createEntry(temp); // create lexeme entry
			lex_index++; // move token pointer
			memset(temp, 0, strlen(temp)); // clear temp
		}
		else if(isspecial(c)) // operaton detected
		{
			j = 0;
			do
			{
				temp[j] = c;

				if(c == '!')
				{
					i++;
					j++;

					c = input[i];
					if(c == '=')
					{
						temp[j] = c;
					}
					else
					{
						printlexerror(1);
						return NULL;
					}
				}
				if(c == '<' || c == '>')
				{
					i++;
					j++;

					c = input[i];

					if(c == '=')
					{
						temp[j] = c;
					}
				}

				if(isOp(temp))
				{
					i++;
					c = input[i];
					break;
				}
				else if(j > 2) // operator too leng
				{
					printlexerror(1);
					return NULL;
				}
				if(c == '\0')
				{
					break;
				}


				i++;
				j++;
				
				c = input[i];
			}
			while(isspecial(c));

			tokens[lex_index] = createEntry(temp); // create lexeme entry
			lex_index++; // move token pointer
			memset(temp, 0, strlen(temp)); // clear temp
		}
		else if(c == '\0') // end of input
		{
			list = tokens;
			if(printFlag)
			{
				printtokens();	
			}
			return list;
		}
		else if(isspace(c)) // space detected
		{
			for(;isspace(input[i]); i++); // skip spaces
		}
		else // invalid character
		{
			printlexerror(1);
			return list;
		}
	}
}


void printtokens()
{
	int i;
	printf("Lexeme Table:\n");
	printf("lexeme\t\ttoken type\n");
	for (i = 0; i < lex_index; i++)
	{
		switch (list[i].type)
		{
			case constsym:
				printf("%11s\t%d", "const", constsym);
				break;
			case varsym:
				printf("%11s\t%d", "var", varsym);
				break;
			case procsym:
				printf("%11s\t%d", "procedure", procsym);
				break;
			case dosym:
				printf("%11s\t%d", "do", dosym);
				break;
			case odsym:
				printf("%11s\t%d", "od", odsym);
				break;
			case whilesym:
				printf("%11s\t%d", "while", whilesym);
				break;
			case elsedosym:
				printf("%11s\t%d", "elsedo", elsedosym);
				break;
			case callsym:
				printf("%11s\t%d", "call", callsym);
				break;
			case writesym:
				printf("%11s\t%d", "write", writesym);
				break;
			case readsym:
				printf("%11s\t%d", "read", readsym);
				break;
			case identsym:
				printf("%11s\t%d", list[i].name, identsym);
				break;
			case numbersym:
				printf("%11d\t%d", list[i].value, numbersym);
				break;
			case assignsym:
				printf("%11s\t%d", ":=", assignsym);
				break;
			case addsym:
				printf("%11s\t%d", "+", addsym);
				break;
			case subsym:
				printf("%11s\t%d", "-", subsym);
				break;
			case multsym:
				printf("%11s\t%d", "*", multsym);
				break;
			case divsym:
				printf("%11s\t%d", "/", divsym);
				break;
			case modsym:
				printf("%11s\t%d", "%", modsym);
				break;
			case eqlsym:
				printf("%11s\t%d", "==", eqlsym);
				break;
			case neqsym:
				printf("%11s\t%d", "!=", neqsym);
				break;
			case lsssym:
				printf("%11s\t%d", "<", lsssym);
				break;
			case leqsym:
				printf("%11s\t%d", "<=", leqsym);
				break;
			case gtrsym:
				printf("%11s\t%d", ">", gtrsym);
				break;
			case geqsym:
				printf("%11s\t%d", ">=", geqsym);
				break;
			case oddsym:
				printf("%11s\t%d", "odd", oddsym);
				break;
			case lparensym:
				printf("%11s\t%d", "(", lparensym);
				break;
			case rparensym:
				printf("%11s\t%d", ")", rparensym);
				break;
			case commasym:
				printf("%11s\t%d", ",", commasym);
				break;
			case periodsym:
				printf("%11s\t%d", ".", periodsym);
				break;
			case semicolonsym:
				printf("%11s\t%d", ";", semicolonsym);
				break;
			case whensym:
				printf("%11s\t%d", "when", whensym);
				break;
		}
		printf("\n");
	}
	printf("\n");
	printf("Token List:\n");
	for (i = 0; i < lex_index; i++)
	{
		if (list[i].type == numbersym)
			printf("%d %d ", numbersym, list[i].value);
		else if (list[i].type == identsym)
			printf("%d %s ", identsym, list[i].name);
		else
			printf("%d ", list[i].type);
	}
	printf("\n");
	list[lex_index++].type = -1;
}

void printlexerror(int type)
{
	if (type == 1)
		printf("Lexical Analyzer Error: Invalid Symbol\n");
	else if (type == 2)
		printf("Lexical Analyzer Error: Invalid Identifier\n");
	else if (type == 3)
		printf("Lexical Analyzer Error: Excessive Number Length\n");
	else if (type == 4)
		printf("Lexical Analyzer Error: Excessive Identifier Length\n");
	else
		printf("Implementation Error: Unrecognized Error Type\n");
	
	free(list);
	return;
}

int isspecial(char c)
{
	char validOps [15] = {':', '+', '-', '*', '/', '%', '=', '!', '<', '>', '(', ')', ',', '.', ';'};
	int i;

	for(i = 0; i < 15; i++)
	{
		if(c == validOps[i])
		{
			//printf("special %c found @ %d\n", c, i);
			return 1;
		}
	}

	return 0;
}

int isOp(char* o)
{
	char validOps[17][3] = {":=", "+", "-", "*", "/", "%", "==", "!=", "<", "<=", ">", ">=", "(", ")", ",", ".", ";"};
	int i;

	for(i = 0; i < 17; i++)
	{
		if(strcmp(o, validOps[i]) == 0)
		{
			//printf("OP %s found @ %d\n", o, i);
			return 1;
		}
	}

	//printf("OP %s not fonud\n", o);
	return 0;
}


lexeme createEntry(char *s)
{
	lexeme new;

	strcpy(new.name, s);
	new.value = getValue(s);
	new.type = getType(s);
	return new;
}

int getValue(char* s)
{
	if(isdigit(s[0]))
	{
		return atoi(s);
	}

	return INT_MIN; // placeholder value for words and operators
}

token_type getType(char* s)
{
	char tokenList[33][11] = {
	"const" , "var" , "procedure", "do" , "od" , "while" , "when" , "elsedo" , "call" ,
	"write" , "read" , "identifier", "number" , ":=" , "+" , "-" , "*" , "/" , "%" , "==" ,
	"!=" , "<" , "<=", ">" , ">=" , "odd" , "(" , ")" , "," , "." , ";"
	};

	int i;

	if(isdigit(s[0])) // is number
	{
		return numbersym;
	}

	for(i = 0; i < 33; i++)
	{
		if(!strcmp(s, tokenList[i]))
		{
			return i + 1;
		}
	}

	return identsym;
}
