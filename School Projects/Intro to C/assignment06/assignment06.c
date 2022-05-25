#include "assignment06.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
typedef struct pancake_info
{
char *name;
double pancake_count;
double pancakes_per_minute;
double minutes_spent_munching;
} pancake_info;
*/

void print_pancake_report(pancake_info p) // test case 1
{
	printf("Name: %s\n", p.name);
	printf("Pancakes Consumed: %.3f\n", p.pancake_count);
	printf("Pancakes Per Minute: %.3f\n", p.pancakes_per_minute);
	printf("Minutes Spent Munching: %.3f\n", p.minutes_spent_munching);
}

double get_missing_pancake_info(pancake_info p) // test case 2
{
	if(p.pancake_count == 0)
	{
		return (p.pancakes_per_minute * p.minutes_spent_munching);
	}
	else if(p.pancakes_per_minute == 0)
	{
		return (p.pancake_count / p.minutes_spent_munching);
	}
	else
	{
		return (p.pancake_count / p.pancakes_per_minute);
	}
}

void update_missing_pancake_info(pancake_info *p) // test case 3
{
	if(p->pancake_count == 0)
	{
		p->pancake_count = (p->pancakes_per_minute * p->minutes_spent_munching);
	}
	else if(p->pancakes_per_minute == 0)
	{
		p->pancakes_per_minute = (p->pancake_count / p->minutes_spent_munching);
	}
	else
	{
		p->minutes_spent_munching = (p->pancake_count / p->pancakes_per_minute);
	}
}

pancake_info *make_pancake_info(char *name, double count, double rate, double minutes) // test case 4
{
	pancake_info *p;
	p = malloc(sizeof(pancake_info));
	p->name = malloc(sizeof(char) * (strlen(name)+1));

	strcpy(p->name, name);
	p->pancake_count = count;
	p->pancakes_per_minute = rate;
	p->minutes_spent_munching = minutes;

	return p;
}

pancake_info *clone_pancake_info(pancake_info source) // test case 5
{
	pancake_info *copied_info;
	copied_info = malloc(sizeof(pancake_info));
	copied_info->name = malloc(sizeof(char) * (strlen(source.name)+1));

	strcpy(copied_info->name, source.name);
	copied_info->pancake_count = source.pancake_count;
	copied_info->pancakes_per_minute = source.pancakes_per_minute;
	copied_info->minutes_spent_munching = source.minutes_spent_munching;

	return copied_info;
}

double difficulty_rating(void)
{
	return 2;
}

double hours_invested(void)
{
	return 1;
}

double prior_experience(void)
{
	return 4;
}