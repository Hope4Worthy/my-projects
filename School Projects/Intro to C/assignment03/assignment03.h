// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!

#ifndef __ASSIGNMENT03_H
#define __ASSIGNMENT03_H


// Magic. This crushes your main() function so we can inject our own main() function into your code.

#define main __destroyed_main__


// Functional Prototypes

void sort_ascending(int *a, int *b, int *c);

void sort_ascending_with_repeats_allowed(int *a, int *b, int *c);

void sort_descending(int *a, int *b, int *c);

void sort_descending_with_repeats_allowed(int *a, int *b, int *c);

int *get_pointer_to_median(int *a, int *b, int *c);

void grow_glowie(int *head);

void shrink_glowie(int *head);

void move_glowie_forward(int *tail, int *head);

int feed_glowworm(int *tail, int *head, int *is_alive, char *snack);

void print_magical_translocational_glowworm(int tail, int head, int platform_length, int is_alive);

double difficulty_rating(void);

double hours_invested(void);

double prior_experience(void);


#endif
