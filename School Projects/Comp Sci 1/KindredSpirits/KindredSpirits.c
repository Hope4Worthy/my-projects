// name Deiens
// br727153
#include "KindredSpirits.h"
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

/*
typedef struct node
{
int data;
struct node *left, *right;
} node;
*/

typedef struct list_node
{
	int data;
	struct list_node *next;
	struct list_node *tail;
}list_node;


list_node *create_list(void)
{
	list_node *list = malloc(sizeof(list_node));
	list->data = 0;
	list->next = NULL;
	list->tail = list;
}
list_node *destroy_list(list_node *head)
{
	if(head == NULL)
		return NULL;
	destroy_list(head->next);
	free(head);
	return NULL;
}
void insert_node_with_data(list_node*head, int data)
{
	list_node *new = malloc(sizeof(list_node));
	new->next = NULL;
	new->data = data;
	new->tail = NULL;

	head->tail->next = new;
	head->tail = new;

}

node *create_tree_node(void)
{
	node *new;

	new = malloc(sizeof(node));

	new->data = 0;
	new->left = NULL;
	new->right = NULL;

	return new;
}

list_node *post_order(node *root, list_node *list)
{
	if(root == NULL)
		return list;

	if(root->left != NULL)
		post_order(root->left, list);
	if(root->right != NULL)
		post_order(root->right, list);

	insert_node_with_data(list, root->data);

	return list;
}

list_node *post_order_traverse (node *root)
{
	list_node *list = create_list();
	return post_order(root, list);
}

list_node *pre_order(node *root, list_node *list)
{
	if(root == NULL)
		return list;

	insert_node_with_data(list, root->data);

	if(root->left != NULL)
		pre_order(root->left, list);
	if(root->right != NULL)
		pre_order(root->right, list);

	return list;
}

list_node *pre_order_traverse (node *root)
{
	list_node *list = create_list();
	return pre_order(root, list);
}

int list_compare(list_node *a, list_node *b)
{
	if(a == NULL && b == NULL)
		return 1;
	if(a == NULL || b == NULL)
		return 0;
	if(a->data == b->data)
	{
		return(1 && list_compare(a->next, b->next));
	}
	else
		return 0;
}

int isReflection(node *a, node *b)
{
	if(a == NULL && b == NULL)
		return 1;

	if(a == NULL || b == NULL)
		return 0;

	if(a->data == b->data)
	{
		if(isReflection(a->left, b->right) == isReflection(a->right, b->left));
			return 1;
	}

	else
		return 0;
}

node *reflection_maker(node *root, node *dest)
{
	if(root == NULL)
	{
		return NULL;
	}

	if(dest == NULL)
	{
		dest = create_tree_node();
	}
	dest->data = root->data;
	if(root->left != NULL)
	{
		if(dest->right == NULL)
		{
			dest->right = create_tree_node();
		}
		reflection_maker(root->left, dest->right);
	}
	if(root->right != NULL)
		if(dest->left == NULL)
		{
			dest->left = create_tree_node();
		}
		reflection_maker(root->right, dest->left);

	return dest;

}

node *makeReflection(node *root)
{
	node *dest = NULL;
	dest = reflection_maker(root, dest);

	return dest;
	
}

int kindredSpirits(node *a, node *b)
{
	int compare_result;
	list_node *lista, *listb;
	if(a == NULL && b == NULL)
		return 1;

	if(a == NULL || b == NULL)
		return 0;

	lista = post_order_traverse(a);
	listb = pre_order_traverse(b);
	compare_result = list_compare(lista, listb);
	if(!compare_result)
	{
		lista = pre_order_traverse(a);
		listb = post_order_traverse(b);
		compare_result = list_compare(lista, listb);
	}

	destroy_list(lista);
	destroy_list(listb);
	return compare_result;

}

double difficultyRating(void)
{
	return 3;
}

double hoursSpent(void)
{
	return 5;
}
