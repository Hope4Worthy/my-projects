// name
// Br727153
// COP 3503 Fall 2021

import java.util.*;
import java.lang.Math;

class SneakyQueens
{
	public static boolean allTheQueensAreSafe (ArrayList<String> coordinatStrings, int boardSize)
	{
		int [] horrizontal = new int [boardSize+1];
		int [] vertical = new int [boardSize+1];
		int [] transposeHorr = new int [(3*boardSize)];
		int [] transposeVert = new int [(3*boardSize)];
		int [] coordPair = new int [2];
		int b;

		for(int i = 0; i < coordinatStrings.size(); i++)
		{
			coordPair = decodeCord(coordinatStrings.get(i));

			if(horrizontal[coordPair[0]] == 1)
			{
				return false;
			}
			else
			{
				horrizontal[coordPair[0]] = 1;
			}
			if(vertical[coordPair[1]] == 1)
			{
				return false;
			}
			else
			{
				vertical[coordPair[1]] = 1;
			}

			// positive slope clac
			b = coordPair[1] - coordPair[0] + boardSize;

			if(-b > 0 && transposeHorr[-b] == 1)
			{
				return false;
			}
			else
			{
				transposeHorr[b] = 1;
			}if(transposeVert[b] == 1)
			{
				return false;
			}
			else
			{
				transposeVert[b] = 1;
			}

			// negative slope calc
			b = coordPair[1] + coordPair[0] + boardSize;
			if(transposeHorr[b] == 1)
			{
				return false;
			}
			else
			{
				transposeHorr[b] = 1;
			}if(transposeVert[b] == 1)
			{
				return false;
			}
			else
			{
				transposeVert[b] = 1;
			}
		}

		return true;
	}

	public static int[] decodeCord(String coordinate)
	{
		int [] coordPair = new int[2];
		String nums = "";
		String letts = "";

		for(int i = 0; i < coordinate.length(); i++)
		{
			if(Character.isDigit(coordinate.charAt(i)))
			{
				nums += coordinate.charAt(i);
			}
			else
			{
				letts += coordinate.charAt(i);
			}

		}

		coordPair[1] = decodeLetCoord(letts);
		coordPair[0] = convertNumCoord(nums);

		return coordPair;
	}

	public static int convertNumCoord(String nums)
	{
		int result = 0;
		int power = 1;
		for(int i = nums.length()-1; i >= 0; i--)
		{
			result += (nums.charAt(i) - '0') * power;
			power *= 10;
		}
		return result;
	}

	public static int decodeLetCoord(String letts)
	{
		int result = 0;
		int power = 1;
		for(int i = letts.length()-1;  i >= 0; i--)
		{
			result += (letts.charAt(i) - ('a' - 1)) * power;
			power = power * 26;
		}
		return result - 1;
	}

	public static double difficultyRating()
	{
		return 3.5;
	}

	public static double hoursSpent()
	{
		return 10;
	}
}
