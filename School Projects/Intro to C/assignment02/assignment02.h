// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!

#ifndef __ASSIGNMENT02_H
#define __ASSIGNMENT02_H


// Magic. This crushes your main() function so we can inject our own main() function into your code.

#define main __destroyed_main__


// Functional Prototypes

void print_one_through_n(int n);

void print_n_through_one(int n);

void tada(int n);

void print_multiples_of_ten(int n);

void print_comma_separated_multiples_of_ten(int n);

void print_comma_separated_multiples_of_ten_fancy(int n);

void print_duet_symmetric(int n, char yin, char yang);

void print_duet(int m, int n, char yin, char yang);

void print_duet_half_and_half(int n, char yin, char yang);

void print_duet_with_yin_dominating(int n, char yin, char yang);

void print_duet_with_yang_dominating(int n, char yin, char yang);

void print_glowie_basic(int num_spaces, int num_segments);

void print_glowie_with_platform(int num_spaces, int num_segments);

void print_glowie_from_coordinates(int tail_coordinate, int head_coordinate);

void print_glowie_dead_or_alive(int tail_coordinate, int head_coordinate, int is_alive);

double difficulty_rating(void);

double hours_invested(void);

double prior_experience(void);


#endif
