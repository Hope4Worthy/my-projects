import java.util.*;
import java.io.*;
import java.lang.*;

public class TopoPaths
{
	public static int countTopoPaths(String filename) throws IOException
	{
		int temp;
		int end = -1;
		int start = -1;

		File ifp = new File(filename);
		Scanner scnr = new Scanner(ifp);

		int numNodes = scnr.nextInt();
		ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
		int[] edgeOut = new int[numNodes];
		int[] edgeIn = new int[numNodes];

		// read and initilize adjacency list
		for(int i = 0; i < numNodes; i++)
		{
			// skip to next line then read first int (num of edges out)
			scnr.nextLine();
			edgeOut[i] = scnr.nextInt();
			adjList.add(new ArrayList<>());

			// read all edge connections
			for(int j = 0; j < edgeOut[i]; j++)
			{
				temp = scnr.nextInt() - 1;
				adjList.get(i).add(temp);
				edgeIn[temp] += 1;
			}
		}

		// find start && end nodes
		for(int i = 0; i < numNodes; i++)
		{
			if(edgeIn[i] == 0)
			{
				if(start == -1)
				{
					start = i;
				}
				else
				{
					// multiple nodes w/ 0 in degree
					// no paths
					return 0;
				}
			}

			if(edgeOut[i] == 0)
			{
				if(end == -1)
				{
					end = i;
				}
				else
				{
					// multiple nodes w/ 0 out degree
					// no paths
				}
			}
		}

		if(start == -1 || end == -1)
		{
			// no start or end nodes found
			return 0;
		}

		// find a path through every node so that you only take a node when its in degree is 0

		return findPath(start, end, edgeIn, adjList, numNodes);

	}

	private static int findPath(int start, int end, int[] edgeIn, ArrayList<ArrayList<Integer>> adjList, int numNodes)
	{
		boolean nodeChange;
		int current = start;
		int next = current;
		int nodeCount = 0;

		// loop from start to end
		while(current != end)
		{
			nodeChange = false;

			// decrement all adjacent in degrees
			for(int a : adjList.get(current))
			{
				// look for next node in path
				if(--edgeIn[a] == 0)
				{
					nodeChange = true;
					next = a;
				}
			}

			nodeCount++;
			current = next;

			// if node did not change this cycle there is no Topo Sort
			if(!nodeChange)
			{
				return 0;
			}

			// found embedded loop somehow
			if(nodeCount > numNodes)
			{
				return 0;
			}
		}


		if(nodeCount == numNodes - 1)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}


	public static double difficultyRating()
	{
		return 3;
	}

	public static double hoursSpent()
	{
		return 15;
	}
}
