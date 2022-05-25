#include "spimcore.h"


/* ALU */
/* 10 Points */
void ALU(unsigned A,unsigned B,char ALU_Cont,unsigned *ALUresult,char *Zero)
{
	if(ALU_Cont == 0x0) // (000) add
	{
		*ALUresult = A + B;
	}
	else if(ALU_Cont == 0x1) // (001) subtract
	{
		*ALUresult = A - B;
	}
	else if(ALU_Cont == 0x2) // (010) if A < B Z = 1; else Z = 0
	{
		if((int)A < (int)B)
			*ALUresult = 1;
		else
			*ALUresult = 0;
	}
	else if(ALU_Cont == 0x3) // (011) if A < B Z = 1; else Z = 0 UNISGNED
	{
		if(A < B)
			*ALUresult = 1;
		else
			*ALUresult = 0;
	}
	else if(ALU_Cont == 0x4) // (100) A and B
	{
		*ALUresult = A & B;
	}
	else if(ALU_Cont == 0x5) // (101) A or B
	{
		*ALUresult = A | B;
	}
	else if(ALU_Cont == 0x6) // (110) shift B left by 16 bits
	{
		*ALUresult << 16;
	}
	else if(ALU_Cont == 0x7) // (111) not A
	{
		*ALUresult = ~A;
	}

	if((A-B) == 0) // check if result = 0 for BEQ
	{
		*Zero = 1;
	}
	else
	{
		*Zero = 0;
	}

		return;
}

/* instruction fetch */
/* 10 Points */
int instruction_fetch(unsigned PC,unsigned *Mem,unsigned *instruction)
{
	if(PC % 4 != 0) // address not word alligned
		return 1;

	*instruction = Mem[PC >> 2];

	return 0;

}

/* instruction partition */
/* 10 Points */
void instruction_partition(unsigned instruction, unsigned *op, unsigned *r1,unsigned *r2, unsigned *r3, unsigned *funct, unsigned *offset, unsigned *jsec)
{
	*op = (instruction & 0xfc000000) >> 26;
	*r1 = (instruction & 0x03e00000) >> 21;
	*r2 = (instruction & 0x001f0000) >> 16;
	*r3 = (instruction & 0x0000f800) >> 11;
	*funct = (instruction & 0x0000003f);
	*offset = (instruction & 0x0000ffff);
	*jsec = (instruction & 0x03ffffff); 

	return;

}

/* instruction decode */
/* 15 Points */
int instruction_decode(unsigned op,struct_controls *controls)
{
	if(op == 0x0) // +, -, &, |, <, < unsigned
	{
		*controls = (struct_controls) {1,0,0,0,0,7,0,0,1};
	}
	else if(op == 0x8) // +I
	{
		*controls = (struct_controls) {0,0,0,0,0,0,0,1,1};
	}
	else if(op == 0x23)// lw
	{
		*controls = (struct_controls) {0,0,0,1,1,0,0,1,1};
	}
	else if(op == 0x2b) // sw
	{
		*controls = (struct_controls) {0,0,0,0,0,0,1,1,0};
	}
	else if(op == 0xf) // lui
	{
		*controls = (struct_controls) {0,0,0,0,0,6,0,1,1};
	}
	else if(op == 0x4) // =
	{
		*controls = (struct_controls) {2,0,1,0,2,1,0,2,0};
	}
	else if(op == 0xa) // < I
	{
		*controls = (struct_controls) {0,0,0,0,0,2,0,1,1};
	}
	else if(op == 0xb) // < I unsigned
	{
		*controls = (struct_controls) {0,0,0,0,0,3,0,1,1};
	}
	else if(op == 0x2) // j
	{
		*controls = (struct_controls) {2,1,2,0,2,0,0,2,0};
	}
	else // wrong op code
		return 1;

	return 0;
}


/* Read Register */
/* 5 Points */
void read_register(unsigned r1,unsigned r2,unsigned *Reg,unsigned *data1,unsigned *data2)
{
	*data1 = Reg[r1];
	*data2 = Reg[r2];
	return;
}


/* Sign Extend */
/* 10 Points */
void sign_extend(unsigned offset,unsigned *extended_value)
{
	int sign = ((offset >> 15) == 1); // check sign of input

	if(sign) // negative
	{
		*extended_value = offset |  0xffff0000;
	}
	else // positive
	{
		*extended_value = offset & 0x0000ffff;
	}
	
	return;
}

/* ALU operations */
/* 10 Points */
int ALU_operations(unsigned data1,unsigned data2,unsigned extended_value,unsigned funct,char ALUOp,char ALUSrc,unsigned *ALUresult,char *Zero)
{
	unsigned input2;
	char ALU_Cont;

	if(ALUOp == 0x0 || ALUOp == 0x1 || ALUOp == 0x2 || ALUOp == 0x3 || ALUOp == 0x4 || ALUOp == 0x5 || ALUOp == 0x6) // +,-,<,< Unsigned, &< |< << 16
	{
		ALU_Cont = ALUOp;
	}
	else if(ALUOp == 0x7) // R-Types
	{
		if(funct == 0x20) // +
		{
			ALU_Cont = 0x0;
		}
		else if(funct == 0x24) // &
		{
			ALU_Cont = 0x4;
		}
		else if(funct == 0x25) // |
		{
			ALU_Cont = 0x5;
		}
		else if(funct == 0x2a) // <
		{
			ALU_Cont = 0x2;
		}
		else if(funct == 0x2b) // < unsigned
		{
			ALU_Cont = 0x3;
		}
		else // invalid funct code
		{
			return 1;
		}
	}
	else // invalid op code
	{
		return 1;
	}

	if(ALUSrc == 1) // determine input B
	{
		input2 = extended_value;
	}
	else
	{
		input2 = data2;
	}

	ALU(data1, input2, ALU_Cont, ALUresult, Zero);

	return 0;

}

/* Read / Write Memory */
/* 10 Points */
int rw_memory(unsigned ALUresult,unsigned data2,char MemWrite,char MemRead,unsigned *Memdata,unsigned *Mem)
{
	if(MemRead == 1) // read Memory
	{
		if(ALUresult % 4 == 0 && ALUresult < 65536) // read if all items are withing bouds
		{
			*Memdata = Mem[ALUresult >> 2];
		}
		else
		{
			return 1; // will go out of bounds so halt
		}
	}
	if(MemWrite == 1)
	{
		if(ALUresult % 4 == 0 && ALUresult < 65536) // set if all items are within bounds
		{
			Mem[ALUresult >> 2] = data2;
		}
		else
		{
			return 1; // will go out of bounds so halt
		}
	}

	return 0;
}


/* Write Register */
/* 10 Points */
void write_register(unsigned r2,unsigned r3,unsigned Memdata,unsigned ALUresult,char RegWrite,char RegDst,char MemtoReg,unsigned *Reg)
{
	if(RegWrite)
	{
		if(MemtoReg) // write Reg to Reg 
		{
			Reg[r2] = Memdata; 
		}
		else // write Memeory to Reg (i-type)
		{
			if(RegDst)
			{
				Reg[r3] = ALUresult; // (i-type)
			}
			else
			{
				Reg[r2] = ALUresult; // (r-type)
			}
			
		}
	}

	return;

}

/* PC update */
/* 10 Points */
void PC_update(unsigned jsec,unsigned extended_value,char Branch,char Jump,char Zero,unsigned *PC)
{
	*PC += 4;

	if(Zero && Branch)
	{
		*PC = *PC +(extended_value << 2);
	}

	if(Jump)
	{
		*PC = (*PC & 0xf0000000) | (jsec << 2);
	}

	return;

}