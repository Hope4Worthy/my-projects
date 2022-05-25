import java.util.*;
import java.io.*;

public class pa02
{
	/*=============================================================================
	|
	|	Assignment: pa02 - Calculating an 8, 16, or 32 bit
	|
	|	checksum on an ASCII input file
	|
	|
	|	Author: name
	|
	|	Language: c, c++, Java
	|
	|
	|	To Compile: javac pa02.java
	|
	|	gcc -o pa02 pa02.c
	|
	|	g++ -o pa02 pa02.cpp
	|
	|
	|	To Execute: java -> java pa02 inputFile.txt 8
	|
	|	or
	|	c++ -> ./pa02 inputFile.txt 8
	|
	|	or
	|	c -> ./pa02 inputFile.txt 8
	|
	|	where inputFile.txt is an ASCII input file
	|
	|	and the number 8 could also be 16 or 32
	|
	|	which are the valid checksum sizes, all
	|
	|	other values are rejected with an error message
	|
	|	and program termination
	|
	|
	|	Note: All input files are simple 8 bit ASCII input
	|
	|
	|	Class: CIS3360 - Security in Computing - Fall 2021
	|
	|	Instructor: McAlpin
	|
	|	Due Date: per assignment
	|
	+=============================================================================*/

	public static void main(String[] args) throws IOException
	{
		
		int blockSize;
		File ifp;
		ArrayList<Character> message;
		int checkSum;
		String temp;
		int[] arry = new int[8];

		if(args.length == 0)
		{
			System.err.println("Missing input file or checksum size argument");
			return;
		}

		blockSize = Integer.parseInt(args[1]);

		// input File
		File inFile = new File(args[0]);
		message = readFile(inFile, blockSize);

		print(message);


		if(blockSize != 8 && blockSize != 16 && blockSize != 32)
		{
			System.err.println("Valid checksum sizes are 8, 16, 32");
		}

		checkSum = calcCheckSum(message, blockSize);
		System.out.println(blockSize + " bit checksum value is " + Integer.toHexString(checkSum) + " for all " + message.size() + " characters");


	}

	private static int[] charToBinArray(char c)
	{
		int[] rtn = new int[8];
		String temp = Integer.toBinaryString(c);
		int i = temp.length() - 1;
		int j = rtn.length - 1;
		while(i >= 0 && j >= 0)
		{
			rtn[j] = (temp.charAt(i) - '0');
			i--;
			j--;
		}

		return rtn;
	}

	private static int[] twoComp(int[] value, int blockSize)
	{
		int[] add = {0,0,0,0,0,0,0,1};
		for(int i = 0; i < blockSize; i++)
		{
			if(value[i] == 0)
			{
				value[i] = 1;
			}
			else
			{
				value[i] = 0;
			}
		}

		return add(value, add, blockSize);
	}

	private static int binArraytoInt(int[] value, int blockSize)
	{
		int result = 0;
		int mult = 1;
		if(value[0] == 1)
		{
			//value = twoComp(value, blockSize);
		}
		
		for(int i = blockSize-1; i >= 0; i--)
		{
			result += (value[i] * mult);
			mult *= 2;
		}

		return result;
	}

	private static int [] add(int[] v1, int[] v2, int blockSize)
	{
		int carry = 0;
		int[] result = new int[blockSize];

		for(int i = blockSize - 1; i >= 0; i--)
		{
			result[i] = v1[i] + v2[i] + carry;
				
			if(result[i] > 1)
			{
				carry = 1;
				result[i] = result[i] % 2;
			}
			else
			{
				carry = 0;
			}
		}

		//System.out.println(Arrays.toString(v1) + " + " + Arrays.toString(v2) + " = " + Arrays.toString(result));
		return result;
	}

	private static int calcCheckSum(ArrayList<Character> message, int blockSize)
	{
		int[] value = new int[blockSize];
		int[] temp = new int[blockSize];
		int[] hold;
		Arrays.fill(value, 0);

		if(blockSize == 8)
		{
			for(int i = 0; i < message.size(); i++)
			{
				hold = charToBinArray(message.get(i));
				value = add(value, hold, blockSize);	
			}
		
		}
		else if(blockSize == 16)
		{
			for(int i = 0; i < message.size(); i++)
			{
				hold = charToBinArray(message.get(i));
				temp = cat(temp, hold);
				if((i%2) == 0)
				{
					temp = shift(temp, blockSize);
				}
				if((i % 2) == 1)
				{
					value = add(value, temp, blockSize);
					Arrays.fill(temp, 0);
				}
			}


		}
		else // blocksize == 32
		{
			for(int i = 0; i < message.size(); i++)
			{
				hold = charToBinArray(message.get(i));
				temp = cat(temp, hold);
				if((i%4) == 3)
				{
					value = add(value, temp, blockSize);
				}
				else
				{
					temp = shift(temp, blockSize);
				}
			}
		}

		return binArraytoInt(value, blockSize);

	}
	private static int[] shift(int[] v1, int blockSize)
	{
		int p1 = v1.length - 1;
		int p2 = p1 - 8;
		int p3 = p2 - 8;
		int p4 = p3 - 8;
		int shiftAmnt = p2;

		//System.out.println(p1 + " - " + p2 + " - " + p3 + " - " + p4);
		//System.out.print(Arrays.toString(v1) + " << " + 8 + " = ");
		if(blockSize == 16)
		{
			while(p1 > shiftAmnt)
			{
				v1[p2--] = v1[p1];
				v1[p1--] = 0;
			}
		}
		else
		{
			while(p1 > shiftAmnt)
			{
				v1[p4--] = v1[p3];
				v1[p3--] = v1[p2];
				v1[p2--] = v1[p1];
				v1[p1--] = 0;
			}
		}

		//System.out.println(Arrays.toString(v1));
		return v1;
	}

	private static int[] cat(int[] v1, int[] v2)
	{
		int p1 = v1.length - 1;
		int p2 = v2.length - 1;

		while(p2 > 0)
		{
			v1[p1] = v2[p2];
			p1--;
			p2--;
		}

		return v1;
	}

	private static void print(ArrayList<Character> s)
	{
		/*
			inputs: char[] "s"
				s: the text to be printed

			return value: none

			prints "s" to screen
		*/

		// maximum length of each line
		int maxLength = 80;

		// program varriables
		int i = 0;
		//System.out.print("<");
		for(char c : s)
		{
			if(i >= maxLength)
			{
				System.out.println();
				i = 0;
			}

			System.out.print(c);
			i++;
		}
		//System.out.print(">");
		System.out.println();
	}

	private static ArrayList<Character> readFile(File f, int blockSize) throws IOException
	{
		/*
			inputs: a File "f, an int "max size", and an int "mode"
				f:  	 File to read from
				maxSize: maximum length of output
				mode: 	 0 - key
					  	 1 - plaintext

			outputs: a char[] of only lowercase alphabetic characters 
		*/

		// scanner
		Scanner scnr = new Scanner(f);

		// ouput
		ArrayList<Character> rtn = new ArrayList<Character>();

		// program varriables
		String input;

			input = scnr.nextLine();

			for(int i = 0; i < input.length(); i++)
			{
				rtn.add(input.charAt(i));
			}

			rtn.add('\n');

			while((rtn.size() * 8) % blockSize != 0) // need to pad 
			{
				rtn.add('X');
			}

		scnr.close();
		return rtn;

	}

	/*=============================================================================
	|
	|	I name (br727153) affirm that this program is
	| entirely my own work and that I have neither developed my code together with
	| any another person, nor copied any code from any other person, nor permitted
	| my code to be copied or otherwise used by any other person, nor have I
	| copied, modified, or otherwise used programs created by others. I acknowledge
	| that any violation of the above terms will be treated as academic dishonesty.
	+=============================================================================*/
}
