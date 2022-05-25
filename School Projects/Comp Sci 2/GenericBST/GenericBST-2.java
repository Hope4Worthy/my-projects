// Sean Szumlanski
// COP 3503, Fall 2021

// ====================
// GenericBST: BST.java
// ====================
// Basic binary search tree (BST) implementation that supports insert() and
// delete() operations. This framework is provided for you to modify as part of
// Programming Assignment #2.

// Edited and made generic by:
// name - br727153
// COP3503 - Fall 2021


import java.io.*;
import java.util.*;

class Node <T>
{
	T data;
	Node<T> left, right;

	Node(T data)
	{
		this.data = data;
	}
}

public class GenericBST <T extends Comparable<T>>
{
	private Node<T> root;

	// helper function
	// calls insert() with the root node and data to be inserted
	public void insert(T data)
	{
		root = insert(root, data);
	}

	// takes the root node and data
	// returns the root node
	// finds the correct place to put the input data and creates a node there
	private Node<T> insert(Node<T> root, T data)
	{
		if (root == null)
		{
			return new Node<T>(data);
		}
		// data <= data at root
		else if (data.compareTo(root.data) <= 0)
		{
			root.left = insert(root.left, data);
		}
		// data > data at root
		else if (data.compareTo(root.data) > 0)
		{
			root.right = insert(root.right, data);
		}

		return root;
	}

	// helper function
	// calls delete() with the root node and the data to be deleted
	public void delete(T data)
	{
		root = delete(root, data);
	}

	// takes the root node and data
	// returns the root node
	// finds the input data and removes it
	private Node<T> delete(Node<T> root, T data)
	{
		if (root == null)
		{
			return null;
		}
		// data < data at root
		else if (data.compareTo(root.data) < 0)
		{
			root.left = delete(root.left, data);
		}
		// data > data at root
		else if (data.compareTo(root.data) > 1)
		{
			root.right = delete(root.right, data);
		}
		// data == data at root
		else
		{
			// input was a leaf node
			if (root.left == null && root.right == null)
			{
				return null;
			}
			// input has right child only
			else if (root.left == null)
			{
				return root.right;
			}
			// input has left child only
			else if (root.right == null)
			{
				return root.left;
			}
			// input has 2 children
			else
			{
				root.data = findMax(root.left);
				root.left = delete(root.left, root.data);
			}
		}

		return root;
	}

	// This method assumes root is non-null, since this is only called by
	// delete() on the left subtree, and only when that subtree is not empty.
	private T findMax(Node<T> root)
	{
		while (root.right != null)
		{
			root = root.right;
		}

		return root.data;
	}

	// helper function
	// calls contains() with the root node and data to look for
	public boolean contains(T data)
	{
		return contains(root, data);
	}

	// takes the root node and data
	// returns the true or false
	// finds the input data and returns accordingly
	private boolean contains(Node<T> root, T data)
	{
		if (root == null)
		{
			return false;
		}
		// data < data at root
		else if (data.compareTo(root.data) < 0)
		{
			return contains(root.left, data);
		}
		// data > data at root
		else if (data.compareTo(root.data) > 0)
		{
			return contains(root.right, data);
		}
		// data == data at root
		else
		{
			return true;
		}
	}

	// helper function
	// calls inorder() with the root node
	// starts the printing proccess and fisishes with a new line 
	public void inorder()
	{
		System.out.print("In-order Traversal:");
		inorder(root);
		System.out.println();
	}

	// takes root node
	// recursivly prints the tree in numeric order
	// print order: left -> root -> right
	private void inorder(Node root)
	{
		if (root == null)
			return;

		inorder(root.left);
		System.out.print(" " + root.data);
		inorder(root.right);
	}

	// helper function
	// calls preorder() with the root node
	// starts the printing proccess and fisishes with a new line 
	public void preorder()
	{
		System.out.print("Pre-order Traversal:");
		preorder(root);
		System.out.println();
	}

	// takes root node
	// recursivly prints the tree from top to bottom
	// print order: root -> left -> right
	private void preorder(Node<T> root)
	{
		if (root == null)
			return;

		System.out.print(" " + root.data);
		preorder(root.left);
		preorder(root.right);
	}

	// helper function
	// calls postorder() with the root node
	// starts the printing proccess and fisishes with a new line 
	public void postorder()
	{
		System.out.print("Post-order Traversal:");
		postorder(root);
		System.out.println();
	}

	// takes root node
	// recursivly prints the tree from bottom to top
	// print order: left -> right -> root
	private void postorder(Node<T> root)
	{
		if (root == null)
			return;

		postorder(root.left);
		postorder(root.right);
		System.out.print(" " + root.data);
	}

	public static void main(String [] args)
	{
		GenericBST<Integer> myTree = new GenericBST<>();

		for (int i = 0; i < 10; i++)
		{
			int r = (int)(Math.random() * 150) + 1;
			System.out.println("Inserting " + r + "...");
			myTree.insert(r);
		}

		myTree.inorder();
		myTree.preorder();
		myTree.postorder();
	}

	public static double difficultyRating()
	{
		return 2.0;
	}

	public static double hoursSpent()
	{
		return 2.0;
	}
}
