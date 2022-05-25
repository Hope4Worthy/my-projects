// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!
// DO NOT MODIFY THIS FILE!

#ifndef __ASSIGNMENT04_H
#define __ASSIGNMENT04_H


// Magic. This crushes your main() function so we can inject our own main() function into your code.

#define main __destroyed_main__


// Functional Prototypes

int is_consonant(char ch);

int is_terminating_punctuator(char ch);

char shift_letter(char ch, int offset);

int cipher(char *filename, int key);

int print_first_word_beginning_with_character(char *filename, char ch);

double difficulty_rating(void);

double hours_invested(void);

double prior_experience(void);


#endif
