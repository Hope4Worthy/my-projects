import java.io.*;
import java.util.*;

public class RunLikeHell
{
	public static int maxGain(int [] blocks)
	{
		int [] result = new int[3];
		
		for(int i = blocks.length - 1; i >= 0; i--)
		{
			result[i%3] = blocks[i] + Math.max(result[(i+2)%3], result[(i+3)%3]);
		}

		return Math.max(result[0], result[1]);
	}

	public static double difficultyRating()
	{
		return 2;
	}
	public static double hoursSpent()
	{
		return 1.5;
	}
}
