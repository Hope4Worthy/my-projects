// NOTE:
// =====
// You do NOT need to #include this file from assignment06.c. Simply #including
// "assignment06.h" will do that for you.


// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!

#ifndef __PANCAKE_STUFF_H
#define __PANCAKE_STUFF_H


// Yay, structs!

typedef struct pancake_info
{
	char *name;                     // Individual's full name.
	double pancake_count;           // Number of pancakes eaten.
	double pancakes_per_minute;     // Pancakes consumed per minute.
	double minutes_spent_munching;  // Minutes spent eating pancakes.
} pancake_info;


// Here be the functional prototypes.

void print_pancake_report(pancake_info p);

double get_missing_pancake_info(pancake_info p);

void update_missing_pancake_info(pancake_info *p);

pancake_info *make_pancake_info(char *name, double count, double rate, double minutes);

pancake_info *clone_pancake_info(pancake_info source);

double difficulty_rating(void);

double hours_invested(void);

double prior_experience(void);


#endif
