/*=============================================================================
| Assignment: pa01 - Encrypting a plaintext file using the Vigenere cipher
|
| Author: name
| Language: c, c++, Java
|
| To Compile: javac pa01.java
| gcc -o pa01 pa01.c
| g++ -o pa01 pa01.cpp
|
| To Execute: java -> java pa01 kX.txt pX.txt
| or c++ -> ./pa01 kX.txt pX.txt
| or c -> ./pa01 kX.txt pX.txt
| where kX.txt is the keytext file
| and pX.txt is plaintext file
|
| Note: All input files are simple 8 bit ASCII input
|
| Class: CIS3360 - Security in Computing - Fall 2021
| Instructor: McAlpin
| Due Date: per assignment
|
+=============================================================================*/

import java.util.*;
import java.io.*;

public class pa01
{
	private static char[] readFile(File f, int maxSize, int mode) throws IOException
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

		// ouput char array && index pointer
		char[] rtn = new char[maxSize];
		int p = 0;

		// program varriables
		int i;
		String input;

		while(scnr.hasNext())
		{
			input = scnr.next();

			for(i = 0; i < input.length(); i++)
			{
				if(p >= maxSize) // max sized reach
				{
					scnr.close();
					return rtn;
				}

				if(!Character.isLetter(input.charAt(i))) // invalid character
				{
					continue;
				}

				rtn[p] = Character.toLowerCase(input.charAt(i));
				p++;
			}
		}

		if(mode == 1) // reading plaintext && must pad
		{
			for(; p < maxSize; p++)
			{
				rtn[p] = 'x';
			}
		}

		scnr.close();
		return rtn;

	}

	private static char[] encrypt(char[] key, char[] plaintext, int maxSize)
	{
		/*
			inputs: a char[] "key", a char[] plaintext, an int maxSize
				key: 	   the key used for encryption
				plaintext: the text to encrypt
				maxSize:   maximum size of output

			outputs: a char[] of encrypted text
		*/

		// index pointers
		int kp = 0;
		int cp = 0;

		// program varriables
		int keyLength;
		int kNum;
		int pNum;
		int cNum;

		// output char array
		char[] ciphertext = new char[maxSize];

		// find length of key
		for(keyLength = 0; key[keyLength] != (char)0; keyLength++);
		// encrypt plaintext
		for(char c : plaintext)
		{
			kNum = key[kp] - 'a';
			pNum = c - 'a';

			cNum = (kNum + pNum) % 26;
			ciphertext[cp] = (char)(cNum + 'a');
			cp++;
			kp = (kp+1) % keyLength;
		}

		return ciphertext;
	}

	private static void print(char[] s)
	{
		/*
			inputs: char[] "s"
				s: the text to be printed

			outputs: none

			prints "s" to screen
		*/

		// maximum length of each line
		int maxLength = 80;

		// program varriables
		int i = 0;
		
		for(char c : s)
		{
			if(i >= maxLength)
			{
				System.out.println();
				i = 0;
			}

			if(Character.isLetter(c)) // needed for printing keys of length < maxSize
			{
				System.out.print(c);
				i++;
			}
		}
	}

	public static void main(String[] args) throws IOException
	{
		// maximum size of inputs / output
		int maxSize = 512;

		// char[]'s to store text
		char[] key = new char[maxSize];
		char[] plaintext = new char[maxSize];
		char[] ciphertext = new char[maxSize];

		// input Files
		File keyFile = new File(args[0]);
		File plaintextFile = new File(args[1]);

		// read files
		key = readFile(keyFile, maxSize, 0);
		plaintext = readFile(plaintextFile, maxSize, 1);

		// encrypt text
		ciphertext = encrypt(key, plaintext, maxSize);

		// print
		System.out.printf("\n\nVigenere Key:\n\n");
		print(key);
		System.out.printf("\n\n\nPlaintext:\n\n");
		print(plaintext);
		System.out.printf("\n\n\nCiphertext:\n\n");
		print(ciphertext);
		System.out.printf("\n");

	}
}

/*=============================================================================
| I name (4591561) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+=============================================================================*/
