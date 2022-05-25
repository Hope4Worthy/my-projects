import java.io.*;
import java.util.*;

class coord
{
	public int x;
	public int y;

	public coord (int x, int y)
	{
		this.x = x;
		this.y = y;
	}

	public boolean equals(Object o)
	{
		coord c = (coord)o;

		if(this.x == c.x && this.y == c.y)
		{
			return true;
		}

		return false;
	}

	public int hashCode()
	{
		return (this.x + this.y) % Integer.MAX_VALUE;
	}

	public String toString()
	{
		return "(" + this.x + "," + this.y + ")";
	}

}

public class SneakyKnights
{

	// takes an array of string coordintates, and an int boardsize
	// returns a boolean if all the knigtns in the input are safe
	public static boolean allTheKnightsAreSafe (ArrayList<String> coordinateStrings, int boardSize)
	{
		int[] coordPair = new int[2];
		HashSet<coord> board = new HashSet<coord>();
		ArrayList<coord> attacks = new ArrayList<coord>();
		coord temp;

		for(String s : coordinateStrings)
		{
			// get loction indecies
			coordPair = decodeCoord(s);

			
			// generate && chock all possible attakcs
			
			if(	   board.contains(new coord(coordPair[0] + 2, coordPair[1] + 1))
				|| board.contains(new coord(coordPair[0] + 2, coordPair[1] - 1))
				|| board.contains(new coord(coordPair[0] - 2, coordPair[1] + 1))
				|| board.contains(new coord(coordPair[0] - 2, coordPair[1] - 1))
				|| board.contains(new coord(coordPair[0] + 1, coordPair[1] + 2))
				|| board.contains(new coord(coordPair[0] + 1, coordPair[1] - 2))
				|| board.contains(new coord(coordPair[0] - 1, coordPair[1] + 2))
				|| board.contains(new coord(coordPair[0] - 1, coordPair[1] - 2)))
			{
				return false;
			}

			// check if duplicate knight && add
			if(!board.add(new coord(coordPair[0], coordPair[1])))
			{
				return false;
			}
		}

		// all knights are safe
		return true;

	}

	public static double difficultyRating()
	{
		return 4.5;
	}

	public static double hoursSpent()
	{
		return 20;
	}

	public static int[] decodeCoord(String coordString)
	{
		String letters = "";
		String numbers = "";
		int[] coords = new int[2];
		int count;
		int i;
		
		// seperates the letters and numbers form the input string
		for(i = 0; i < coordString.length(); i++)
		{
			if(Character.isLetter(coordString.charAt(i)))
			{
				letters += coordString.charAt(i);
			}
			else
			{
				numbers += coordString.charAt(i);
			}
		}

		// convert strings to int coordinates
		coords[1] = Math.abs(Integer.parseInt(numbers));

		count = 1;
		for(i = letters.length()-1; i >= 0; i--)
		{
			coords[0] += ((letters.charAt(i) - ('a' - 1)) * count);
			count *= 26;
		}

		coords[0] -= 1;

		return coords;
	}

	public static void main(String[] args) 
	{
		System.out.println((int)('a' - ('a'-1)));
		return;
	}
}