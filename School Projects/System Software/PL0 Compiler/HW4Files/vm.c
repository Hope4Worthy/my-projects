#include <stdio.h>
#include "compiler.h"

const int MAX_PAS_LENGTH = 500;

struct ir // Instruction Register
{
	int op; // Operation Code
	int l; // Lexicographical Level
	int m; // Op Codde Dependent Value
} typedef ir;

int pc, bp, sp, dp, gp, FREE; // pointers for PAS
int pas [500]; // proccessor address space
int opc;
int obp;
int jpcFlag;

int base (int l)
{
	int arb = bp;
	for(;l > 0;l--)
	{
		arb = pas[arb+2];
	}
	return arb;
}

void execute_program (instruction *code, int outputs)
{
	int i; // loping variable
	int HaltFlag = 1; // 1 to run program || 0 to stop program
	char * CmdCode; // used for printing commad codes
	int ic; // used for loading the program
	ir IR; // instruction register



	/* ----- load program ----- */
	ic = 0; // initilive ic for load
	for(i = 0;code[i].opcode != -1; i++) // load program
	{
		pas[ic] = code[i].opcode;
		pas[ic+1] = code[i].l;
		pas[ic+2] = code[i].m;
		ic += 3;
	}

	/* ----- initilizations ----- */
	for(i = ic; i < MAX_PAS_LENGTH; i++)
	{
		pas[i] = 0; // initilize pas registers to 0
	}

	pc = 0;
	sp = MAX_PAS_LENGTH;
	bp = gp = ic;
	dp = bp-1;
	FREE = gp + 40;
	jpcFlag = 0;

	/* ----- print initial values for trace ---- */
	if(outputs)
	{
		printf("\t\t\tPC\tBP\tSP\tDP\tdata\n");
		printf("Initial values:\t%*d\t%*d\t%*d\t%*d\n", 2,pc, 2,bp, 3,sp, 2,dp);
	}
	

	/* ----- run proccess ---- */
	while(HaltFlag) 
	{
		/* ----- fetch ----- */
		IR.op = pas[pc];
		IR.l = pas[pc+1];
		IR.m = pas[pc+2];
		
		pc += 3; // move to next command	

		/* ----- execute ----- */
		switch(IR.op) 
		{
			/*
				execute an instructon ased on the operation code
				1 - load a literal
				2 - arithmatic / logical operations
				3 - load from memory
				4 - write to memory
				5 - call new proccess
				6 - increment data / stack pointer
				7 - unconditional jump
				8 - conditional jump
				9 - system call
				see each case for more information
			*/
			case 1: // LIT
				/* 
					load a literal into memory or the top of the stack / data
					m = literal value
				*/
				CmdCode = "LIT"; // set command code for print
				if(bp == gp)
				{
					dp += 1;
					pas[dp] = IR.m;
				}
				else
				{
					sp -= 1;
					pas[sp] = IR.m;
				}
				break;
			case 2: // OPR
				/*
					 perform an operation based on the value of m
					 0 - return from a proccess
					 1 - negate value at top of the stack / data
					 2 - add top 2 value of the stack / data
					 3 - subtract the top 2 value of the stack / data
					 4 - multiply the top 2 value of the stack / data
					 5 - divide the top 2 value of the stack / data
					 6 - dotermine if the top value of the stack / data is odd or even
					 7 - mou the top 2 value of the stack / data
					 8 - equvalence
					 9 - non equavalence
					 10 - less than
					 11 - less than or equal to
					 12 - greater than
					 13 - greater than or equal to 
					 see each case for more info
				*/
				switch(IR.m)
				{
					case 0: // RTN
						/*
							return from a proccess
						*/
						CmdCode = "RTN"; // set command code for print
						obp = bp;
						pc = pas[sp+1]; // RA
						sp = obp+4; // SL
						bp = pas[sp - 3]; // DL
						opc = pc;
						break;
					case 1: // NEG
						/*
							negate the value on the top of the stack / data
							done in place
						*/
						CmdCode = "NEG"; // set command code for print
						if(bp == gp)
						{
							pas[dp] = pas[dp] * -1;
						}
						else
						{
							pas[sp] = pas[sp] * -1;
						}
						break;
					case 2: // ADD
						/*
							add the value of the top 2 elements in the stack / data
							and place at the top of the stack / data
						*/
						CmdCode = "ADD"; // set command code for print
						if(bp == gp)
						{
							dp -= 1;
							pas[dp] = pas[dp] + pas[dp + 1];
						}
						else
						{
							sp += 1;
							pas[sp] = pas[sp] + pas[sp - 1];
						}
						break;
					case 3: // SUB
						/*
							subtract the value of the top 2 elements in the stack / data
							and place at the top of the stack / data
						*/
						CmdCode = "SUB"; // set command code for print
						if(bp == gp)
						{
							dp -= 1;
							pas[dp] = pas[dp] - pas[dp + 1];
						}
						else
						{
							sp += 1;
							pas[sp] = pas[sp] - pas[sp - 1];
						}
						break;
					case 4: // MUL
						/*
							multiply the value of the top 2 elements in the stack / data
							and place at the top of the stack / data
						*/
						CmdCode = "MUL"; // set command code for print
						if(bp == gp)
						{
							dp -= 1;
							pas[dp] = pas[dp] * pas[dp + 1];
						}
						else
						{
							sp += 1;
							pas[sp] = pas[sp] * pas[sp - 1];
						}
						break;
					case 5: // DIV
						/*
							divide the value of the top 2 elements in the stack / data
							and place at the top of the stack / data
						*/
						CmdCode = "DIV"; // set command code for print
						if(bp == gp)
						{
							dp -= 1;
							pas[dp] = pas[dp] / pas[dp + 1];
						}
						else
						{
							sp += 1;
							pas[sp] = pas[sp] / pas[sp - 1];
						}
						break;
					case 6: // ODD
						/*
							place a value on the top of stack / data if value at the top of stack / data is even or odd
							0 if even | 1 if odd
						*/
						CmdCode = "ODD"; // set command code for print
						if(bp == gp)
						{
							pas[dp] = pas[dp] % 2;
						}
						else
						{
							pas[sp] = pas[sp] % 2;
						}
						break;
					case 7: // MOD
						/*
							mods the value of the top 2 elements in stack / data
							and place at the top of stack / data
						*/
						CmdCode = "MOD"; // set command code for print
						if(bp == gp)
						{
							dp -= 1;
							pas[dp] = pas[dp] % pas[dp + 1];
						}
						else
						{
							sp += 1;
							pas[sp] = pas[sp] % pas[sp - 1];
						}
						break;
					case 8: // EQL
						/*
							checks if the 2nd value in stack / data is equal to the value infront of it
							places the result in the top of stack / data
							1 if true | 0 if false
						*/
						CmdCode = "EQL"; // set command code for print
						if(bp == gp)
						{			
							dp -= 1;			
							if(pas[dp] == pas[dp + 1])
							{
								pas[dp] = 1;								
							}
							else
							{
								pas[dp] = 0;
							}
						}
						else
						{
							sp++;
							if(pas[sp] == pas[sp - 1])
							{
								pas[sp] = 1;								
							}
							else
							{
								pas[sp] = 0;
							}
						}
						break;
					case 9: // NEQ
						/*
							checks if the 2nd value in stack / data is not equal the value infront of it
							places the result in the top of stack / data
							1 if true | 0 if false
						*/
						CmdCode = "NEQ"; // set command code for print
						if(bp == gp)
						{						
							dp -= 1;
							if(pas[dp] != pas[dp + 1])
							{
								pas[dp] = 1;								
							}
							else
							{
								pas[dp] = 0;
							}
						}
						else
						{
							sp += 1;
							if(pas[sp] != pas[sp - 1])
							{
								pas[sp] = 1;								
							}
							else
							{
								pas[sp] = 0;
							}
						}
						break;
					case 10: // LSS
						/*
							checks if the 2nd value in stack / data is less than the value infront of it
							places the result in the top of stack / data
							1 if true | 0 if false
						*/
						CmdCode = "LSS"; // set command code for print
						if(bp == gp)
						{				
							dp -= 1;		
							if(pas[dp] < pas[dp + 1])
							{
								pas[dp] = 1;								
							}
							else
							{
								pas[dp] = 0;
							}
						}
						else
						{
							sp += 1;
							if(pas[sp] < pas[sp - 1])
							{
								pas[sp] = 1;								
							}
							else
							{
								pas[sp] = 0;
							}
						}
						break;
					case 11: // LEQ
						/*
							checks if the 2nd value in stack / data is less than or equal to the value infront of it
							places the result in the top of stack / data
							1 if true | 0 if false
						*/
						CmdCode = "LEQ"; // set command code for print
						if(bp == gp)
						{
							dp -= 1;		
							if(pas[dp] <= pas[dp + 1])
							{
								pas[dp] = 1;								
							}
							else
							{
								pas[dp] = 0;
							}
						}
						else
						{
							sp += 1;
							if(pas[sp] <= pas[sp - 1])
							{
								pas[sp] = 1;								
							}
							else
							{
								pas[sp] = 0;
							}
						}
						break;
					case 12: // GTR
						/*
							checks if the 2nd value in stack / data is greater than the value infront of it
							places the result in the top of stack / data
							1 if true | 0 if false
						*/
						CmdCode = "GTR"; // set command code for print
						if(bp == gp)
						{		
							dp -= 1;				
							if(pas[dp] > pas[dp + 1])
							{
								pas[dp] = 1;								
							}
							else
							{
								pas[dp] = 0;
							}
						}
						else
						{
							sp += 1;
							if(pas[sp] > pas[sp - 1])
							{
								pas[sp] = 1;								
							}
							else
							{
								pas[sp] = 0;
							}
						}
						break;
					case 13: // GEQ
						/*
							checks if the 2nd value in stack / data is greater than or equal to the value infront of it
							places the result in the top of stack / data
							1 if true | 0 if false
						*/
						CmdCode = "GEQ"; // set command code for print
						if(bp == gp)
						{				
							dp -= 1;		
							if(pas[dp] >= pas[dp + 1])
							{
								pas[dp] = 1;								
							}
							else
							{
								pas[dp] = 0;
							}
						}
						else
						{
							sp += 1;
							if(pas[sp] >= pas[sp - 1])
							{
								pas[sp] = 1;								
							}
							else
							{
								pas[sp] = 0;
							}
						}
						break;
				}
				break;
			case 3: // LOD
				/*
					load a value form memory onto the top of the stack / data
					l - lexicographical level
					m - offset
				*/
				CmdCode = "LOD"; // set command code for print
				if(bp == gp)
				{
					//printf("\tLOD1\n");
					dp += 1;
					pas[dp] = pas[gp+IR.m];
				}
				else if(base(IR.l) == gp)
				{
					//printf("\tLOD2\n");
					sp -= 1;
					pas[sp] = pas[gp + IR.m];
				}
				else
				{
					//printf("\tLOD3\n");
					sp -= 1; 
					pas[sp] = pas[(base(IR.l) - IR.m) + 2];
				}
				break;
			case 4: // STO
				/*
					store a value from the top of the stack / data to memory
					l - lexicographical level
					m - offset
				*/
				CmdCode = "STO"; // set command code for print
				if(bp == gp)
				{
					//printf("\tSTO1\n");
					pas[gp+IR.m] = pas[dp];
					dp -= 1;
				}
				else if(base(IR.l) == gp)
				{
					//printf("\tSTO2\n");
					pas[gp + IR.m] = pas[sp];
					sp += 1;
				}
				else
				{
					//printf("\tSTO3\n");
					pas[base(IR.l) - IR.m + 2] = pas[sp];
					sp += 1; 
				}
				break;
			case 5: // CAL
				/*
					call a new proccess
					l = static link
					m = address of new proccess
					bp = dynomic link
					pc = return address
				*/
				CmdCode = "CAL"; // set command code for print
				pas[sp - 1] = 0; // FV
				pas[sp - 2] = base(IR.l); // SL
				pas[sp - 3] = bp; // DL
				pas[sp - 4] = pc; // RA
				bp = sp - 4;
				opc = pc;
				pc = IR.m;
				break;
			case 6: // INC
				/*
					increment either the data pointer or the stack pointer
					m = increment ammount
				*/
				CmdCode = "INC"; // set command code for print
				if(bp == gp)
				{
					dp += IR.m;
				}
				else
				{
					sp -= (IR.m);
				}
				break;
			case 7: // JMP
				/*
					unconditional jump
					m = address of jump location
				*/
				CmdCode = "JMP"; // set command code for print
				opc = pc;
				pc = IR.m;
				break;
			case 8: // JPC
				/*
					jump if top of stack / data == 0
					m = addess of jump location
				*/
				CmdCode = "JPC"; // set command code for print
				if(bp == gp)
				{
					if(pas[dp] == 0)
					{
						jpcFlag = 1;
						opc = pc;
						pc = IR.m;
					}
					dp -= 1;
				}
				else
				{
					if(pas[sp] == 0)
					{
						jpcFlag = 1;
						opc = pc;
						pc = IR.m;
					}
					sp += 1;
				}
				break;
			case 9: // SYS
				/*
					system operation depending on m
					1 - print the value on he top of the stack / data to the screen
					2 - load a value form user input to the top of the stack / data
					3 - end program
				*/
				CmdCode = "SYS"; // set command code for print
				if (IR.m == 1)
				{
					if(bp == gp)
					{
						printf("Top of Stack Value: %d\n", pas[dp]);
						dp -= 1;
					}
					else
					{
						printf("Top of Stack Value: %d\n", pas[sp]);
						sp += 1;
					}
				}
				else if (IR.m == 2)
				{
					if(bp == gp)
					{
						printf("Please Enter an Integer: ");
						dp += 1;
						scanf("%d", &pas[dp]);
					}
					else
					{
						printf("Please Enter an Integer: ");
						sp -= 1;
						scanf("%d", &pas[sp]);
					}
				}
				else if (IR.m == 3)
				{
					HaltFlag = 0;
				}
				break;	

		}

		/* ----- print trace ----- */
		if(outputs)
		{
			if(IR.op ==  5 || IR.op == 7 || (IR.op == 2 && IR.m == 0) || jpcFlag)
			{
				printf("%*d ",2,(opc-3)/3); // print input line number	
				jpcFlag = 0;
			}
			else
			{
				printf("%*d ",2,(pc-3)/3); // print input line number
			}

			printf("\t%s ", CmdCode); // print command code

			printf("\t%*d\t%*d\t%*d\t%*d\t%*d\t%*d\t", -1,IR.l, -1,IR.m, -2,pc, -2,bp, -3,sp, -2,dp); // print command and pointer values

			for(i = gp; i <= dp; i++) // print data
			{
				printf(" %d", pas[i]);
			}

			printf("\n\tstack : ");

			for(i = MAX_PAS_LENGTH-1; i >= sp; i--) // print stack
			{
				printf("%d ", pas[i]);
			}

			printf("\n");	
		}
		

	}

}
