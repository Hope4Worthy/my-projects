import java.util.*;
import java.lang.*;

class Node <t extends Comparable<t>>
{
	private int height;
	private ArrayList<Node<t>> next;
	private t data;

	// ----- Constructors ----- //

	public Node(int height)
	{
		this.height = height;
		this.next = new ArrayList<>();

		// ititilive next references
		for(int i = 0; i < height; i++)
		{
			this.next.add(null);
		}
	}

	public Node(int height, t data)
	{
		this.height = height;
		this.data = data;
		this.next = new ArrayList<>();

		// ititilive next references
		for(int i = 0; i < height; i++)
		{
			this.next.add(null);
		}
	}

	// ----- Getters ----- //

	public t value()
	{
		return this.data;
	}

	public int height()
	{
		return this.height;
	}

	public Node<t> next(int level)
	{
		if(level >= this.next.size())
		{
			// ensure level is within bounds
			return null;
		}

		return this.next.get(level);
	}

	// ----- setters ----- //

	public void setNext(int level, Node<t> node)
	{
		if(level >= this.next.size())
		{
			// is level is outside of bounds add new reference
			// used to add reference after growing node

			this.next.add(node);
			return;
		}

		this.next.set(level, node);
	}

	public void grow()
	{
		// grows node regardless of probability

		this.height++;
		this.next.add(null);
	}

	public boolean probGrow()
	{
		// 50% chance to grow a node
		// returns true if node grew || false if it did not

		if(Math.random() > 0.5)
		{
			this.grow();
			return true;
		}

		return false;
	}

	public void trim(int height)
	{
		// removes references untill node height is given height

		while(this.height > height)
		{
			this.next.remove(this.height-1);
			this.height--;
		}
	}

}

public class SkipList <t extends Comparable<t>>
{
	private Node<t> head;
	private int size;
	private int height;

	// ----- constructors ----- //

	public SkipList()
	{
		this.height = 0;
		this.size = 0;
		this.head = new Node<t>(0);
	}

	public SkipList(int height)
	{
		this.height = (height < 0 ? 0 : height);
		this.size = 0;
		this.head = new Node<t>(this.height);
	}

	// ----- Getters ----- //

	public int size()
	{
		return this.size;
	}

	public int height()
	{
		return this.height;
	}

	public Node<t> head()
	{
		return this.head;
	}

	public boolean contains(t data)
	{
		// ruterns true or false if the list contains "data"
		return this.get(data) == null ? false : true;

	}

	public Node<t> get (t data)
	{
		// takes a piece of data
		// returns the first occurace of Node containg the data
		// returns null if data is not in the list

		Node<t> current = this.head;

		for(int i = this.height; i >= 0; i--)
		{
			while (current.next(i) != null && current.next(i).value().compareTo(data) < 0)
			{
				// keep searching for the data
				current = current.next(i);	
			}

			if(current.next(i) != null && current.next(i).value().compareTo(data) == 0)
			{
				// node found
				return current.next(i);
			}
		}

		// move to node containtig data
		current = current.next(0);

		// ensure node contains data
		if(current.value().compareTo(data) == 0)
		{
			return current;
		}
		else
		{
			// node not found
			return null;
		}
	}

	// ----- Height Functions ----- //

	private int calcMaxHeight(int size)
	{
		// calculates the max height of the list based on the "size"
		// uses celing(log2("size")) -- done with the change of base formula

		if(size == 1)
		{
			return 1;
		}
		return (int)Math.ceil(Math.log(size) / Math.log(2));
	}

	private int genHeght(int maxHeight)
	{
		// generates a random height
		// returns a number from 1 to maxHeight

		int h = 1;

		while(Math.random() > 0.5)
		{
			if(h >= maxHeight)
				break;
			else
				h++;
		}

		return h;
	}

	private void growList()
	{
		// grows list if size changes
		// used during insertion

		Node<t> current = this.head;
		Node<t> last = this.head;
		int level = this.height - 1;

		// ensure level is within lower bound
		if(level < 0)
			level = 0;


		// grow head node
		current.grow();

		current = current.next(level);

		// grow all nodes in the list
		while(current != null)
		{
			if(current.height() == this.height)
			{
				if(current.probGrow());
				{
					last.setNext(this.height, current);
					last = current;
				}
			}
			current = current.next(level);
		}

		// increase list height
		this.height++;

	}

	private void trimList()
	{
		// trims the list by 1 level
		// used during deletion

		Node<t> current = this.head;
		Node<t> next;
		int level = this.height - 1;

		// ensure level is within lower bound
		if(level < 0)
			level = 0;

		// if size io 0, height is 0
		if(this.size == 0)
		{
			this.height = 0;
			return;
		}

		// trim all nodes in the list
		while(current != null)
		{
			next = current.next(level);
			current.trim(level);
			current = next;
		}

		// decrease list height
		this.height--;
	}

	// ----- delete / insert ----- //

	public void delete(t data)
	{
		// deletes first occurance of data within list

		ArrayList<Node<t>> references = new ArrayList<Node<t>>();
		Node<t> current = this.head;

		for(int i = 0; i <= this.height; i++)
		{
			// initilize references
			references.add(null);
		}

		for(int i = this.height; i >= 0; i--)
		{

			while(current.next(i) != null && current.next(i).value().compareTo(data) < 0)
			{
				// searh for node
				current = current.next(i);
			}

			// set reference when you drop down a level
			references.set(i, current);
		}

		// move to node containg data
		current = current.next(0);

		if(current == null)
		{
			// data not in the list
			return;
		}
		if(current.value().compareTo(data) != 0)
		{
			// data not in list
			return;
		}

		// re-link references to delete node
		for(int i = 0; i < this.height; i++)
		{
			if(references.get(i).next(i) != current)
			{
				break;
			}
			else
			{
				references.get(i).setNext(i, current.next(i));
			}
		}

		// decrese size of the list
		this.size--;

		if(this.size == 0)
		{
			// if size is 0, make height 0;

			this.height = 0;
			this.head.trim(0);
			return;
		}
		while(this.height > calcMaxHeight(this.size))
		{
			// if size changes trim the list
			trimList();
		}
	}

	public void insert(t data)
	{
		Node<t> current = this.head;
		Node<t> newNode = new Node<t>(genHeght(this.height), data);
		ArrayList<Node<t>> references = new ArrayList<Node<t>>();

		int level = this.height - 1;

		for(int i = 0; i <= this.height; i++)
		{
			// initilize references
			references.add(null);
		}

		for(int i = this.height; i >= 0; i--)
		{
			while(current.next(i) != null && current.next(i).value().compareTo(data) < 0)
			{
				// search for node
				current = current.next(i);
			}

			// set to references when you drop down a level
			references.set(i, current);
		}

		// move to node that comes before the new node
		current = current.next(0);

		for(int i = 0; i < newNode.height(); i++)
		{
			// move references to include new node
			newNode.setNext(i, references.get(i).next(i));
			references.get(i).setNext(i, newNode);
		}

		// increase size of the list
		this.size++;

		// check if sive changes
		while(this.height < calcMaxHeight(this.size))
		{
			// grow list if needed
			growList();
		}

	}

	public void insert(t data, int height)
	{
		Node<t> current = this.head;
		Node<t> newNode = new Node<t>(height, data);
		ArrayList<Node<t>> references = new ArrayList<Node<t>>();

		int level = this.height - 1;

		for(int i = 0; i <= this.height; i++)
		{
			// initilize references
			references.add(null);
		}

		for(int i = this.height; i >= 0; i--)
		{
			while(current.next(i) != null && current.next(i).value().compareTo(data) < 0)
			{
				// search for node
				current = current.next(i);
			}

			// set to references when you drop down a level
			references.set(i, current);
		}

		// move to node that comes before the new node
		current = current.next(0);

		for(int i = 0; i < newNode.height(); i++)
		{
			// move references to include new node
			newNode.setNext(i, references.get(i).next(i));
			references.get(i).setNext(i, newNode);
		}

		// increase size of the list
		this.size++;

		// check if sive changes
		while(this.height < calcMaxHeight(this.size))
		{
			// grow list if needed
			growList();
		}

	}

	public static double difficultyRating()
	{
		return 3.0;
	}

	public static double hoursSpent()
	{
		return 30.0;
	}
}
