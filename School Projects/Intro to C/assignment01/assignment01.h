// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!


#ifndef __ASSIGNMENT01_H
#define __ASSIGNMENT01_H


// Magic. This crushes your main() function so we can inject our own main() function into your code.

#define main __destroyed_main__


// Functional Prototypes

int return_five(void);

int pancake_printer(void);

double get_pancake_count(double minutes, double pancakes_per_minute);

double get_pancakes_per_minute(double minutes, double pancake_count);

double get_minutes_spent_munching(double pancake_count, double pancakes_per_minute);

void print_pancake_count(double minutes, double pancakes_per_minute);

void print_pancakes_per_minute(double minutes, double pancake_count);

void print_minutes_spent_munching(double pancake_count, double pancakes_per_minute);

double get_pancake_data(double pancake_count, double pancakes_per_minute, double minutes);

void print_pancake_data(double pancake_count, double pancakes_per_minute, double minutes);

int round_up_or_down(double dub);

int get_median_of_three(int a, int b, int c);

void print_median_of_three(int a, int b, int c);

int get_ordinal_day(int month, int day);

int print_ordinal_day(int month, int day);

int get_ordinal_day_extended(int month, int day, int leapyear);

int get_ordinal_day_with_error_checking(int month, int day, int leapyear);

double difficulty_rating(void);

double hours_invested(void);

double prior_experience(void);


#endif
