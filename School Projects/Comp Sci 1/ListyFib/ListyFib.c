#include "ListyFib.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

Node *create_Node(void)
{
	Node *new = malloc(sizeof(Node));

	if(new == NULL)
		return NULL;

	new->digit = 0;
	new->next = NULL;

	return new;
}

Node *destroy_head(ListyInt *listy)
{
	Node *temp;

	if(listy == NULL)
	{
		return NULL;
	}

	temp = listy->head;
	listy->head = temp->next;

	(listy->length)--;
	free(temp);

	return NULL;
}

int insert_Node(ListyInt *listy, int data)
{
	int i;
	Node *Node;

	if(listy == NULL)
	{
		return 1;
	}


	if(listy->head == NULL)
	{
		listy->head = create_Node();
		listy->head->digit = data;
	}
	else
	{
		Node = listy->head;
		for(i = 0; i < ((listy->length)-1); i++)
		{
			Node = Node->next;
		}

		Node->next = create_Node();

		if(Node->next == NULL)
		{
			return 1;
		}
		else
		{
			Node->next->digit = data;
		}
	}

	(listy->length) ++;

	return 0;
}

int add_listy_Node(ListyInt *result_list, ListyInt *p, ListyInt *q, int index, int carry)
{
	int p_value, q_value, result, i;
	Node *p_pointer, *q_pointer, *result_pointer;

	p_pointer = p->head;
	q_pointer = q->head;
	result_pointer = result_list->head;

	if(p == NULL || q == NULL)
		return INT_MIN;

	for(i = 0; i < index; i++)
	{
		p_pointer = p_pointer->next;
		q_pointer = q_pointer->next;
	}

	if(p_pointer == NULL || q_pointer == NULL)
		return INT_MIN;

	result = p_pointer->digit + q_pointer->digit + carry;

	if(result >= 10)
	{
		carry = result / 10;
		result = result % 10;
	}
	else
		carry = 0;

	for(i = 1; i < index; i++)
	{
		result_pointer = result_pointer->next;
		
	}

	result_pointer->next = create_Node();

	if(result_pointer->next == NULL)
		return INT_MIN;

	result_pointer = result_pointer->next;

	result_pointer->digit = result;

	return carry;
}

ListyInt * create_listy_int(void)
{
	ListyInt *listy = malloc(sizeof(ListyInt));

	if(listy == NULL)
		return NULL;

	listy->head = NULL;
	listy->length = 0;
	return listy;
}

Node *destroy_listy(ListyInt *listy)
{
	Node *temp;
	if(listy == NULL)
	{
		return NULL;
	}

	while(listy->head != NULL)
	{
		destroy_head(listy);
	}

	return NULL;
}

ListyInt *destroyListyInt(ListyInt *listy)
{
	if(listy == NULL)
		return NULL;

	listy->head = destroy_listy(listy);
	free(listy);
}

ListyInt *stringToListyInt(char *str)
{
	int i, len;
	char value[0];
	ListyInt *listy;

	if(str == NULL || strcmp(str, "") == 0)
	{
		return NULL; 
	}

	len = strlen(str) - 1;

	listy = create_listy_int();

	if(listy == NULL)
	{
		return NULL;
	}


	for(i = len; i >= 0; i--)
	{
		value[0] = str[i];
		insert_Node(listy, atoi(value));
	}

	return listy;
}

int power(int power)
{
	int i, result;

	if(power == 0)
	{
		return 1;
	}
	else
	{
		for(i = 1, result = 10; i < power; i++)
		{
			result *= 10;
		}
	}

	return result;

}

char itoa(int i)
{
	char result;

	if(i == 0)
		return '0';

	if(i == 9)
		return '9';

	if(i == 8)
		return '8';

	if(i == 7)
		return '7';

	if(i == 6)
		return '6';

	if(i == 5)
		return '5';

	if(i == 4)
		return '4';

	if(i == 3)
		return '3';

	if(i == 2)
		return '2';

	if(i == 1)
		return '1';


}
char *listyIntToString(ListyInt *listy)
{
	char *str, temp[1];
	int i;
	Node *Node;

	if(listy == NULL)
		return NULL;

	str = calloc(listy->length, sizeof(char));

	if(str == NULL)
		return NULL;

	for(i = listy->length, Node = listy->head; Node != NULL && i > 0; i--, Node = Node->next)
	{
		str[i-1] = itoa(Node->digit);
	}

	return str;
}



ListyInt *uintToListyInt(unsigned int n)
{
	ListyInt *listy;
	int i;

	listy = create_listy_int();

	if(n == 0)
	{
		insert_Node(listy, 0);
	}
	else
	{
		for(i = 0; n > 0; i++)
		{
			if(insert_Node(listy, n%10) == 1)
			{
				destroy_listy(listy);
				return NULL;
			}
			
			n = n / 10;
		}
	}

	return listy;
}

unsigned int *listyIntToUint(ListyInt *listy)
{
	Node *Node;
	unsigned int value, last_value, *return_value;
	int i;

	value = 0;
	last_value = 0;

	if(listy == NULL)
		return NULL;

	i = 0;
	
	for(Node = listy->head; Node != NULL; Node = Node->next, i++)
	{
		value += (unsigned int)(Node->digit * power(i));

		if(value < last_value)
			return NULL;
		else
			last_value = value;
	}

	return_value = malloc(sizeof(unsigned int));
	*return_value = value;
	return return_value;


}

ListyInt *listyAdd(ListyInt *p, ListyInt *q)
{
	int i, carry, length, p_val, q_val, result;
	Node *p_pos, *q_pos;
	ListyInt *sum;

	carry = 0;

	sum = create_listy_int();

	if(p->length > q->length)
		length = p->length;
	else
		length = q->length;

	p_pos = p->head;
	q_pos = q->head;

	for(i = 0; i < length || carry != 0; i++)
	{
		if(p_pos == NULL)
		{
			p_val = 0;
		}
		else
		{
			p_val = p_pos->digit;
		}

		if(q_pos == NULL)
		{
			q_val = 0;
		}
		else
		{
			q_val = q_pos->digit;
		}

		result = p_val + q_val + carry;

		insert_Node(sum, (result %10));

		if(p_pos != NULL)
		{
			p_pos = p_pos->next;
		}
		if(q_pos != NULL)
		{
			q_pos = q_pos->next;
		}

		carry = ((result / 10) % 10);
	}

	return sum;
}

void plusPlus(ListyInt *listy)
{
	int carry = 1;
	Node *Node;

	if(listy == NULL)
		return;

	Node = listy->head;
	while(carry > 0)
	{
		Node->digit += carry;
		carry = (Node->digit / 10);
		Node = Node->next;
	}
}

void copy_list(ListyInt *destination, ListyInt *source)
{
	Node *Node;
	destroy_listy(destination);

	for(Node = source->head; Node != NULL; Node = Node->next)
	{
		insert_Node(destination, Node->digit);
	}
}

ListyInt *fib(unsigned int n)
{
	int i;
	ListyInt *value = create_listy_int();
	ListyInt *last_value = create_listy_int();
	ListyInt *last_value_2 = create_listy_int();
	ListyInt *temp = create_listy_int();

	insert_Node(value, 0);
	insert_Node(last_value, 0);
	insert_Node(last_value_2, 1);


	for(i = 0; i < n; i++)
	{
		destroyListyInt(value);
		value = listyAdd(last_value, last_value_2);
		copy_list(temp, value);
		copy_list(last_value_2, last_value);
		copy_list(last_value, temp);

	}

	destroyListyInt(last_value);
	destroyListyInt(last_value_2);
	destroyListyInt(temp);

	return value;
}

double difficultyRating(void)
{
	return 3;
}

double hoursSpent(void)
{
	return 10;
}
