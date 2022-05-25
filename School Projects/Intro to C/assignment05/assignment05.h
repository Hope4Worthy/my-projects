// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!

#ifndef __ASSIGNMENT05_H
#define __ASSIGNMENT05_H


// Magic. This crushes your main() function so we can inject our own main() function into your code.

#define main __destroyed_main__


// Functional Prototypes

int get_char_count(char *str, char ch);

void print_char_count(char *str, char ch);

void print_char_counts(char **array, int num_strings, char ch);

void copy_string_reverse(char *destination, char *source);

void print_specific_row(int **array, int num_rows, int num_cols, int which_row);

void print_specific_row_comma_separated(int **array, int num_rows, int num_cols, int which_row);

void print_specific_column_in_reverse(int **array, int num_rows, int num_cols, int which_col);

void fill_matrix(int **array, int num_rows, int num_cols, int fill_value);

void checker_matrix(int **array, int num_rows, int num_cols);

double difficulty_rating(void);

double hours_invested(void);

double prior_experience(void);


#endif
