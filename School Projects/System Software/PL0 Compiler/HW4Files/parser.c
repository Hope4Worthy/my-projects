#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "compiler.h"

#define MAX_CODE_LENGTH 1000
#define MAX_SYMBOL_COUNT 100

instruction *code;
int cIndex;
symbol *table;
int tIndex;
lexeme *tokens;
lexeme currentToken;
int sp;
int level;
int curentLevel;
int symCount;
int tokenIndex;
int symIndex;
int docount;
int odcount;


void emit(int opname, int level, int mvalue);
void addToSymbolTable(int k, char n[], int v, int l, int a, int m);
void printparseerror(int err_code);
void printsymboltable();
void printassemblycode();
void program();
void block();
void constDeclaration();
int varDeclaraiton();
void procDeclaration();
void statement();
void condition();
void expression();
void term();
void factor();
void mark();
int multiDeclarationCheck(lexeme token);
int findSym(lexeme token, int type);
void getNext();
void getLast();

instruction *parse(lexeme *list, int printTable, int printCode)
{
	//printf("**-- PARSE --**\n");

	int temp;
	int i;
	cIndex = 0;
	tIndex = 0;
	tokenIndex = 0;
	code = NULL;
	tokens = list;
	code = malloc(sizeof(instruction) * MAX_CODE_LENGTH);
	table = malloc(sizeof(symbol) * MAX_SYMBOL_COUNT);
	docount = 0;
	odcount = 0;

	getNext();
	//printf("got first\n");
	program();

	if(docount != odcount)
	{
		printparseerror(16);
		exit(0);
	}

	for(i = 0; i <= tIndex; i++)
	{
		if(code[i].opcode == 5)
		{
			code[i].m = table[code[i].m].addr;
		}
	}

	code[0].m = table[0].addr;

	code[cIndex].opcode = -1;

	if(printTable)
	{
		//printf("printing table\n");
		printsymboltable();
	}
	if(printCode)
	{
		//printf("printing code\n");
		printassemblycode();
	}
	
	//printf("end parse\n");
	return code;
}

void program()
{
	//printf("**-- PROCGRAM --**\n");

	emit(7,0,0); // jmp
	addToSymbolTable(3, "main", 0, level, 0, 0);
	level = -1;
	block();

	if(currentToken.type != periodsym)
	{
		printparseerror(1);
		exit(0);
	}

	emit(9,0,3); // halt
}

void block()
{
	//printf("--** BLOCK **--\n");

	level++;
	int procIndex = tIndex -1;
	constDeclaration();
	int x = varDeclaraiton();

	procDeclaration();
	table[procIndex].addr = cIndex * 3;

	if(level == 0)
	{
		emit(6, 0, x); // INC
	}
	else
	{
		emit(6, 0, x+4); // INC
	}

	statement();
	mark();
	level--;
}

void constDeclaration()
{
	//printf("**-- CONST **--\n");

	char name [12];
	if(currentToken.type == constsym)
	{
		do
		{
			getNext();

			if(currentToken.type != identsym)
			{
				printparseerror(2);
				exit(0);
			}
			
			if(multiDeclarationCheck(currentToken) != -1)
			{
				printparseerror(18);
				exit(0);
			}

			strcpy(name, currentToken.name);
			getNext();

			if(currentToken.type != assignsym)
			{
				printparseerror(2);
				exit(0);
			}

			getNext();

			if(currentToken.type != numbersym)
			{
				printparseerror(2);
				exit(0);
			}

			addToSymbolTable(1, name, currentToken.value, level, 0, 0);

			getNext();
		}
		while(currentToken.type == commasym);

		if(currentToken.type != semicolonsym)
		{
			if(currentToken.type == identsym)
			{
				printparseerror(13);
			}
			else
			{
				//printf("1\n");
				printparseerror(14);
			}
			exit(0);
		}

		getNext();
	}
}

int varDeclaraiton()
{
	//printf("**-- VAR --**\n");

	int numVars = 0;
	if(currentToken.type == varsym)
	{
		do
		{
			numVars++;
			getNext();

			if(currentToken.type != identsym)
			{
				printparseerror(3);
				exit(0);
			}
			if(multiDeclarationCheck(currentToken) != -1)
			{
				printparseerror(18);
				exit(0);
			}
			if(level == 0)
			{
				addToSymbolTable(2, currentToken.name, 0, level, numVars-1, 0);
			}
			else
			{
				addToSymbolTable(2, currentToken.name, 0, level, numVars+2, 0);
			}
			getNext();
		}
		while(currentToken.type == commasym);

		if(currentToken.type != semicolonsym)
		{
			if(currentToken.type == identsym)
			{
				printparseerror(13);
			}
			else
			{
				//printf("2\n");
				printparseerror(14);
			}
			exit(0);
		}

		getNext();
		return numVars;
	}
	else
		return 0;
}

void procDeclaration()
{
	//printf("**-- PROC --**\n");

	while(currentToken.type == procsym)
	{
		getNext();
		if(currentToken.type != identsym)
		{
			printparseerror(4);
			exit(0);
		}

		if(multiDeclarationCheck(currentToken) != -1)
		{
			printparseerror(18);
			exit(0);
		}

		addToSymbolTable(3, currentToken.name, 0, level, 0, 0);

		getNext();
		if(currentToken.type != semicolonsym)
		{
			//printf("4\n");
			printparseerror(4);
			exit(0);
		}

		getNext();
		block();

		if(currentToken.type != semicolonsym)
		{
			//printf("5\n");
			printparseerror(14);
			exit(0);
		}

		getNext();
		emit(2,0,0); //RTN
	}
}

void statement()
{
	//printf("**-- STATEMENT --**\n");

	int symIndex;
	if(currentToken.type == identsym)
	{
		//printf("\t--**ident**--\n");
		symIndex = findSym(currentToken,2);
		if(symIndex == -1)
		{
			if(findSym(currentToken, 1) != findSym(currentToken, 3)) // ident is either const or proc
			{
				printparseerror(6);
			}
			else // ident not found
			{
				printparseerror(19);
			}
			exit(0);
		}

		getNext();

		if(currentToken.type != assignsym)
		{
			printparseerror(5);
			exit(0);
		}

		getNext();
		expression();

		if(currentToken.type == semicolonsym)
		{
			//getNext();
		}

		emit(4, level-table[symIndex].level, table[symIndex].addr); // STO
		return;
	}
	else if(currentToken.type == dosym)
	{
		//printf("\t--**do**--\n");
		do
		{
			getNext();
			//printf("\t do -> statement W/ <%s> - %d", currentToken.name, currentToken.type);
			statement();
		}
		while(currentToken.type == semicolonsym);

		if(currentToken.type != odsym)
		{
			if(currentToken.type == identsym || currentToken.type == dosym || currentToken.type == whensym
				|| currentToken.type == whilesym || currentToken.type == readsym || currentToken.type == writesym
				|| currentToken.type == callsym)
			{
				printparseerror(15);
			}
			else
			{
				printparseerror(16);
			}
			exit(0);
		}

		getNext();
		return;
	}
	else if(currentToken.type == whensym)
	{
		//printf("\t--**when**--\n");
		int jpcIndex;
		int jmpIndex;

		getNext();
		condition();
		jpcIndex = cIndex;

		emit(8, 0, jpcIndex); // JPC 

		if(currentToken.type != dosym)
		{
			printparseerror(8);
			exit(0);
		}

		getNext();
		docount--;
		statement();
		//printf("\tin statment -> when after statment call W/ <%s> - %d\n", currentToken.name, currentToken.type);
		getNext();

		if(currentToken.type == elsedosym)
		{
			//printf("in eisedo\n");
			jmpIndex = cIndex;

			emit(7, 0, jmpIndex); // JMP
			code[jpcIndex].m = cIndex*3;

			getNext();
			statement();

			code[jmpIndex].m = cIndex*3;
		}
		else
		{
			getLast();
			code[jpcIndex].m = cIndex*3;
		}
		//getLast();
		return;
	}
	else if(currentToken.type == whilesym)
	{
		//printf("\t--**while**--\n");
		int loopIndex;
		int jpcIndex;

		getNext();

		loopIndex = cIndex;
		condition();

		if(currentToken.type != dosym)
		{
			printparseerror(9);
			exit(0);
		}

		docount--;
		getNext();

		jpcIndex = cIndex;
		emit(8, 0, jpcIndex); // JPC

		statement();

		emit(7,0,loopIndex*3); // JMP

		code[jpcIndex].m = cIndex*3;
		return;
	}
	else if(currentToken.type == readsym)
	{
		//printf("\t--**read**--\n");
		int symIndex;

		getNext();
		if(currentToken.type != identsym)
		{
			printparseerror(6);
			exit(0);
		}

		symIndex = findSym(currentToken, 2);

		if(symIndex == -1)
		{
			if(findSym(currentToken, 1) != findSym(currentToken, 3)) // ident is a const or proc
			{
				printparseerror(6);
				exit(0);
			}
			else // ident not found
			{
				printparseerror(19);
				exit(0);
			}
		}

		getNext();
		emit(9, 0, 2); // READ
		emit(4, level-table[symIndex].level, table[symIndex].addr); // STO

		return;
	}
	else if(currentToken.type == writesym)
	{
		//printf("\t--**write**--\n");
		getNext();
		expression();
		emit(9, 0, 1); //WRITE
		return;
	}
	else if(currentToken.type == callsym)
	{
		//printf("\t--**call**--\n");
		int symIndex;

		getNext();
		symIndex = findSym(currentToken, 3);
		if(symIndex == -1) 
		{
			if(findSym(currentToken, 1) != findSym(currentToken, 2)) // ident is var or const
			{
				printparseerror(7);
			}
			else // ident not found
			{
				printparseerror(19);
			}
			exit(0);
		}
		getNext();
		emit(5, level-table[symIndex].level, table[symIndex].addr); // CAL
		return;
	}
	else
	{
		//printf("unknown @ %d\n", tokenIndex);
		return;
	}
}

void condition()
{
	//printf("**-- CONDITION --**\n");

	if(currentToken.type == oddsym)
	{
		getNext();
		expression();
		emit(2, 0, 6); // ODD
	}
	else
	{
		expression();
		if(currentToken.type == eqlsym)
		{
			getNext();
			expression();
			emit(2, 0, 8); // EQL
		}
		else if(currentToken.type == neqsym)
		{
			getNext();
			expression();
			emit(2, 0, 9); // NEQ
		}
		else if(currentToken.type == lsssym)
		{
			getNext();
			expression();
			emit(2, 0, 10); // LSS
		}
		else if(currentToken.type == leqsym)
		{
			getNext();
			expression();
			emit(2, 0, 11); // LEQ
		}
		else if(currentToken.type == gtrsym)
		{
			getNext();
			expression();
			emit(2, 0, 12); // GTR
		}
		else if(currentToken.type == geqsym)
		{
			getNext();
			expression();
			emit(2, 0, 13); // GEQ
		}
		else
		{
			printparseerror(10);
			exit(0);
		}
	}
}

void expression()
{
	//printf("**-- EXPRESSION --**\n");

	if(currentToken.type == subsym)
	{
		getNext();
		term();
		emit(2, 0, 1); // NEG

		while(currentToken.type == addsym || currentToken.type == subsym)
		{
			if(currentToken.type == addsym)
			{
				getNext();
				term();
				emit(2, 0, 2); // ADD
			}
			else
			{
				getNext();
				term();
				emit(2, 0, 3); // SUB
			}
		}
	}
	else
	{
		if(currentToken.type == addsym)
		{
			getNext();
		}

		term();

		while(currentToken.type == addsym || currentToken.type == subsym)
		{
			if(currentToken.type == addsym)
			{
				getNext();
				term();
				emit(2, 0, 2); // ADD
			}
			else
			{
				getNext();
				term();
				emit(2, 0, 3); // SUB
			}
		}
	}

	if(currentToken.type == lparensym || currentToken.type == identsym 
		|| currentToken.type == numbersym || currentToken.type == oddsym)
	{
		//printf("1 - @ %d - ", tokenIndex);
		printparseerror(17);
		exit(0);
	}
}

void term()
{
	//printf("**-- TERM --**\n");

	factor();
	while(currentToken.type == multsym || currentToken.type == divsym || currentToken.type == modsym)
	{
		if(currentToken.type == multsym)
		{
			getNext();
			factor();
			emit(2, 0, 4); // MUL
		}
		else if(currentToken.type == divsym)
		{
			getNext();
			factor();
			emit(2, 0, 5); // DIV
		}
		else if(currentToken.type == modsym)
		{
			getNext();
			factor();
			emit(2, 0, 7); // MOD
		}
	}
}

void factor()
{
	//printf("**-- FACTOR --**\n");

	int varIndex;
	int constIndex;

	if(currentToken.type == identsym)
	{
		varIndex = findSym(currentToken, 2);
		constIndex = findSym(currentToken, 1);
		if(varIndex == -1 && constIndex == -1) // ident is not var or const
		{
			if(findSym(currentToken, 3) == -1) // ident is proc
			{
				printparseerror(19);
			}
			else // ident not found
			{
				printparseerror(11);
			}
			exit(0);
		}
		if(varIndex == -1) // ident is a const
		{
			emit(1, 0, table[constIndex].val); // LIT
		}
		else if(constIndex == -1 || table[varIndex].level > table[constIndex].level) // ident is var
		{
			emit(3, level-table[varIndex].level, table[varIndex].addr); // LOD
		}
		else
		{
			emit(1, 0, table[constIndex].val); // LIT
		}
		getNext();
	}
	else if(currentToken.type == numbersym)
	{
		emit(1, 0, currentToken.value); // LIT
		getNext();
	}
	else if(currentToken.type == lparensym)
	{
		getNext();
		expression();
		if(currentToken.type != rparensym)
		{
			printparseerror(12);
			exit(0);
		}
		getNext();
	}
	else
	{
		//printf("2 - ");
		printparseerror(17);
		exit(0);
	}
}

void emit(int opname, int level, int mvalue)
{
	code[cIndex].opcode = opname;
	code[cIndex].l = level;
	code[cIndex].m = mvalue;
	cIndex++;
}

void addToSymbolTable(int k, char n[], int v, int l, int a, int m)
{
	table[tIndex].kind = k;
	strcpy(table[tIndex].name, n);
	table[tIndex].val = v;
	table[tIndex].level = l;
	table[tIndex].addr = a;
	table[tIndex].mark = m;
	tIndex++;
}


void printparseerror(int err_code)
{
	switch (err_code)
	{
		case 1:
			printf("Parser Error: Program must be closed by a period\n");
			break;
		case 2:
			printf("Parser Error: Constant declarations should follow the pattern 'ident := number {, ident := number}'\n");
			break;
		case 3:
			printf("Parser Error: Variable declarations should follow the pattern 'ident {, ident}'\n");
			break;
		case 4:
			printf("Parser Error: Procedure declarations should follow the pattern 'ident ;'\n");
			break;
		case 5:
			printf("Parser Error: Variables must be assigned using :=\n");
			break;
		case 6:
			printf("Parser Error: Only variables may be assigned to or read\n");
			break;
		case 7:
			printf("Parser Error: call must be followed by a procedure identifier\n");
			break;
		case 8:
			printf("Parser Error: when must be followed by do\n");
			break;
		case 9:
			printf("Parser Error: while must be followed by do\n");
			break;
		case 10:
			printf("Parser Error: Relational operator missing from condition\n");
			break;
		case 11:
			printf("Parser Error: Arithmetic expressions may only contain arithmetic operators, numbers, parentheses, constants, and variables\n");
			break;
		case 12:
			printf("Parser Error: ( must be followed by )\n");
			break;
		case 13:
			printf("Parser Error: Multiple symbols in variable and constant declarations must be separated by commas\n");
			break;
		case 14:
			printf("Parser Error: Symbol declarations should close with a semicolon\n");
			break;
		case 15:
			printf("Parser Error: Statements within do-od must be separated by a semicolon\n");
			break;
		case 16:
			printf("Parser Error: do must be followed by od\n");
			break;
		case 17:
			printf("Parser Error: Bad arithmetic\n");
			break;
		case 18:
			printf("Parser Error: Confliciting symbol declarations\n");
			break;
		case 19:
			printf("Parser Error: Undeclared identifier\n");
			break;
		default:
			printf("Implementation Error: unrecognized error code\n");
			break;
	}
	
	free(code);
	free(table);
}

void printsymboltable()
{
	int i;
	printf("Symbol Table:\n");
	printf("Kind | Name        | Value | Level | Address | Mark\n");
	printf("---------------------------------------------------\n");
	for (i = 0; i < tIndex; i++)
		printf("%4d | %11s | %5d | %5d | %5d | %5d\n", table[i].kind, table[i].name, table[i].val, table[i].level, table[i].addr, table[i].mark); 
	
	free(table);
	table = NULL;
}

void printassemblycode()
{
	int i;
	printf("Line\tOP Code\tOP Name\tL\tM\n");
	for (i = 0; i < cIndex; i++)
	{
		printf("%d\t", i);
		printf("%d\t", code[i].opcode);
		switch (code[i].opcode)
		{
			case 1:
				printf("LIT\t");
				break;
			case 2:
				switch (code[i].m)
				{
					case 0:
						printf("RTN\t");
						break;
					case 1:
						printf("NEG\t");
						break;
					case 2:
						printf("ADD\t");
						break;
					case 3:
						printf("SUB\t");
						break;
					case 4:
						printf("MUL\t");
						break;
					case 5:
						printf("DIV\t");
						break;
					case 6:
						printf("ODD\t");
						break;
					case 7:
						printf("MOD\t");
						break;
					case 8:
						printf("EQL\t");
						break;
					case 9:
						printf("NEQ\t");
						break;
					case 10:
						printf("LSS\t");
						break;
					case 11:
						printf("LEQ\t");
						break;
					case 12:
						printf("GTR\t");
						break;
					case 13:
						printf("GEQ\t");
						break;
					default:
						printf("err\t");
						break;
				}
				break;
			case 3:
				printf("LOD\t");
				break;
			case 4:
				printf("STO\t");
				break;
			case 5:
				printf("CAL\t");
				break;
			case 6:
				printf("INC\t");
				break;
			case 7:
				printf("JMP\t");
				break;
			case 8:
				printf("JPC\t");
				break;
			case 9:
				switch (code[i].m)
				{
					case 1:
						printf("WRT\t");
						break;
					case 2:
						printf("RED\t");
						break;
					case 3:
						printf("HAL\t");
						break;
					default:
						printf("err\t");
						break;
				}
				break;
			default:
				printf("err\t");
				break;
		}
		printf("%d\t%d\n", code[i].l, code[i].m);
	}
	if (table != NULL)
		free(table);
}

void mark()
{
	int i;
	//printf("Marking Level - %d\n", level);
	for(i = tIndex; i >= 0; i--)
	{
		if(table[i].mark == 1)
		{
			continue;
		}
		else
		{
			if(table[i].level == level)
			{
				//printf("\tMarknig Index - %d\n", i);
				table[i].mark = 1;
			}
			else if(table[i].level < level)
			{
				//printf("\tMark Break\n");
				//break;
			}
		}
	}
}

int multiDeclarationCheck(lexeme token)
{
	int type;
	int i;

	if(token.type == constsym)
		type = 1;
	else if(token.type == varsym)
		type = 2;
	else if (token.type == procsym)
		type = 3;
	for(i = 0; i <= tIndex; i++)
	{
		if(!strcmp(token.name, table[i].name))
		{
			if(table[i].mark == 0 && table[i].level == level)
			{
				return i;
			}

		}
	}

	return -1;
}

int findSym(lexeme token, int type)
{
	int rtn = -1;
	int i;

	//printf("looking for %s\n", token.name);

	for(i = 0; i <= tIndex; i++)
	{
		if(!strcmp(token.name, table[i].name) && table[i].kind == type && table[i].mark == 0)
		{
			//printf("found %s @ %d\n\n", table[i].name, i);
			if(rtn < i)
				rtn = i;
		}
	}

	//printf("found nothing\n\n");
	return rtn;
}

void getNext()
{
	currentToken = tokens[tokenIndex];
	//printf("getting next token %d - <%s>\n", tokenIndex, currentToken.name);
	fflush(stdin);
	tokenIndex++;
	if(currentToken.type == dosym)
		docount++;
	else if(currentToken.type == odsym)
		odcount++;
}

void getLast()
{
	//printf("getting last token %d - <%s>\n", tokenIndex, currentToken.name);
	tokenIndex -= 2;
	currentToken = tokens[tokenIndex];
	if(currentToken.type == dosym)
		docount--;
	else if(currentToken.type == odsym)
		odcount--;
}
