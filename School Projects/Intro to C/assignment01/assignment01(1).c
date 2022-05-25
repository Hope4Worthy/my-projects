// name - COP 3223H - Fall 2019 - br727153

#include "assignment01.h"
#include <stdio.h>

int return_five(void) // test case 1
{
	return 5;
}

int pancake_printer(void) // test case 2
{
	printf("\"Pancake Breakfast with Professor Patrick!\"\n");
	return 52847;
}

double get_pancake_count(double minutes, double pancakes_per_minute) // test case 3
{
	double NumConsumed; // Num Pancakes Consumed

	NumConsumed = minutes * pancakes_per_minute;
	return NumConsumed;

}

double get_pancakes_per_minute(double minutes, double pancake_count) // test case 4
{
	double AveragePPM; //average panckes consumber per minute
	AveragePPM = pancake_count / minutes;
	return AveragePPM;
}

double get_minutes_spent_munching (double pancake_count, double pancakes_per_minute) // test case 5
{
	double MinEating; //Minutes spent eating
	
	MinEating = pancake_count / pancakes_per_minute;
	return MinEating;
}

void print_pancake_count (double minutes, double pancakes_per_minute) // test case 6
{
	double NumConsumed; //Number of pancakes consumed
	
	NumConsumed = minutes * pancakes_per_minute;
	printf("Pancakes consumed: %.3f\n", NumConsumed );
	return;
}

void print_pancakes_per_minute (double minutes, double pancake_count) // test case 7
{
	double AveragePPM; //average panckes per minute
	AveragePPM = pancake_count / minutes;
	printf("Pancakes per minute: %.3f\n", AveragePPM );
	return;
}

void print_minutes_spent_munching (double pancake_count, double pancakes_per_minute) // test case 8
{
	double MinEating; //Minutes spent eating
	
	MinEating = pancake_count / pancakes_per_minute;
	printf("Minutes spent munching: %.3f\n",MinEating );
	return;
}

double get_pancake_data(double pancake_count, double pancakes_per_minute, double minutes) // test case 9
{
	if (pancake_count == 0)
	{
		pancake_count = minutes * pancakes_per_minute;
		return pancake_count;
	}

	else if (pancakes_per_minute == 0)
	{
		pancakes_per_minute = pancake_count / minutes;
		return pancakes_per_minute;
	}

	else
	{
		minutes = pancake_count / pancakes_per_minute;
		return minutes;
	}
}

void print_pancake_data(double pancake_count, double pancakes_per_minute, double minutes) // test case 10
{
	if (pancake_count == 0)
	{
		pancake_count = minutes * pancakes_per_minute;
		printf("Pancakes consumed: %.3f\n", pancake_count);
		return;
	}

	else if (pancakes_per_minute == 0)
	{
		pancakes_per_minute = pancake_count / minutes;
		printf("Pancakes per minute: %.3f\n", pancakes_per_minute);
		return;
	}

	else
	{
		minutes = pancake_count / pancakes_per_minute;
		printf("Minutes spent munching: %.3f\n", minutes);
		return;
	}
}

int round_up_or_down (double dub) // test case 11
{
	int result;
	int intermediateInt; // intermediate integer value
	double intermediateDub; // intermediate double vlaue

	intermediateInt = dub;
	intermediateDub = dub - intermediateInt;

	if(intermediateDub >= .5)
	{
		result = (dub + 1);
	}
	else
	{
		result = dub;
	}
	
}

int get_median_of_three(int a, int b, int c) // test case 12
{
	int result;

	if (a <= b && b <= c || c <= b && b <= a) // b is median
	{
		return b;
	}

	else if (b <= a && a <= c || c <= a && a <= b) // a is median
	{
		return a;
	}

	else // c is median
	{
		return c;

	}

}

void print_median_of_three(int a, int b, int c) // test case 13
{
	int result;

	if (a <= b && b <= c || c <= b && b <= a) // b is median
	{
		printf("%d\n", b);
		return;
	}

	else if (b <= a && a <= c || c <= a && a <= b) // a is median
	{
		printf("%d\n", a);
		return;
	}

	else // c is median
	{
		printf("%d\n", c);
		return;

	}

}

int get_ordinal_day(int month, int day) // test case 14
{
	int result;

	if(month == 1)
	{
		result = day;
	}

	else if(month == 2)
	{
		result = day + 31;
	}

	else if(month == 3)
	{
		result = day + 59;
	}

	else if(month == 4)
	{
		result = day + 90;
	}

	else if(month == 5)
	{
		result = day + 120;
	}

	else if(month == 6)
	{
		result = day + 151;
	}

	else if(month == 7)
	{
		result = day + 181;
	}

	else if(month == 8)
	{
		result = day + 212;
	}

	else if(month == 9)
	{
		result = day + 243;
	}

	else if(month == 10)
	{
		result = day + 273;
	}

	else if(month == 11)
	{
		result = day + 304;
	}

	else
	{
		result = day + 334;
	}
	return result;
}

void PrintMonthAndDay (int day, int result) // test case 15
{
	if((day % 10) == 1) // input is a -st number
		{
			printf("%dst is the ", day);
		}

		else if((day % 10) == 2) // input is a -nd number
		{
			printf("%dnd is the ", day);
		}

		else if((day % 10) == 3) // input is a -rd number
		{
			printf("%drd is the ", day);
		}

		else // input is a -th number
		{
			printf("%dth is the ", day);
		}


		if((result % 10) == 1) // result is a -st number
		{
			printf("%dst day of the year.\n", result);
		}
		else if((result % 10) == 2) // result is a -nd number
		{
			printf("%dnd day of the year.\n", result);
		}
		else if((result % 10) == 3) // result is a -rd number
		{
			printf("%drd day of the year.\n", result);
		}
		else // result is a -th number
		{
			printf("%dth day of the year.\n", result);
		}
}

int print_ordinal_day(int month, int day) // test case 15
{
	int result;

	if(month == 1)
	{
		result = day;
		printf("January ");
		PrintMonthAndDay(day, result);
	}

	else if(month == 2)
	{
		result = day + 31;
		printf("February ");
		PrintMonthAndDay(day, result);
	}

	else if(month == 3)
	{
		result = day + 59;
		printf("March ");
		PrintMonthAndDay(day, result);
	}

	else if(month == 4)
	{
		result = day + 90;
		printf("April ");
		PrintMonthAndDay(day, result);
	}

	else if(month == 5)
	{
		result = day + 120;
		printf("May ");
		PrintMonthAndDay(day, result);
	}

	else if(month == 6)
	{
		result = day + 151;
		printf("June ");
		PrintMonthAndDay(day, result);
	}

	else if(month == 7)
	{
		result = day + 181;
		printf("July ");
		PrintMonthAndDay(day, result);
	}

	else if(month == 8)
	{
		result = day + 212;
		printf("August ");
		PrintMonthAndDay(day, result);
	}

	else if(month == 9)
	{
		result = day + 243;
		printf("September ");
		PrintMonthAndDay(day, result);
	}

	else if(month == 10)
	{
		result = day + 273;
		printf("October ");
		PrintMonthAndDay(day, result);
	}

	else if(month == 11)
	{
		result = day + 304;
		printf("November ");
		PrintMonthAndDay(day, result);
	}

	else
	{
		result = day + 334;
		printf("December ");
		PrintMonthAndDay(day, result);
	}
	return result;
}

int get_ordinal_day_extended (int month, int day, int leapyear) // test case 16
{
	int result;

	if(month == 1)
	{
		result = day;
	}

	else if(month == 2)
	{
		result = day + 31;
	}

	else if(month == 3)
	{
		result = day + 59;
		if(leapyear == 1)
		{
			result = result + 1;
		}
	}

	else if(month == 4)
	{
		result = day + 90;
		if(leapyear == 1)
		{
			result = result + 1;
		}
	}

	else if(month == 5)
	{
		result = day + 120;
		if(leapyear == 1)
		{
			result = result + 1;
		}
	}

	else if(month == 6)
	{
		result = day + 151;
		if(leapyear == 1)
		{
			result = result + 1;
		}
	}

	else if(month == 7)
	{
		result = day + 181;
		if(leapyear == 1)
		{
			result = result + 1;
		}
	}

	else if(month == 8)
	{
		result = day + 212;
		if(leapyear == 1)
		{
			result = result + 1;
		}
	}

	else if(month == 9)
	{
		result = day + 243;
		if(leapyear == 1)
		{
			result = result + 1;
		}
	}

	else if(month == 10)
	{
		result = day + 273;
		if(leapyear == 1)
		{
			result = result + 1;
		}
	}

	else if(month == 11)
	{
		result = day + 304;
		if(leapyear == 1)
		{
			result = result + 1;
		}
	}

	else
	{
		result = day + 334;
		if(leapyear == 1)
		{
			result = result + 1;
		}
	}
	return result;
}

int get_ordinal_day_with_error_checking (int month, int day, int leapyear) // test case 17
{
	int result;

	if (month > 0 && month <=12)
	{

		if(month == 1) // January
		{
			if (day <= 31)
			{
				result = day;	
			}
			else
			{
				result = -1;
			}
		}

		else if(month == 2) // February
		{
			if (leapyear == 0)
			{
				if (day <= 28)
				{
					result = day + 31;
				}
				else
				{
					result = -1;
				}
			}
			else
			{
				if (day <= 29)
				{
					result = day + 31;
				}
				else
				{
					result = -1;
				}
			}

			
		}

		else if(month == 3) // March
		{
			if (day <= 31)
			{
				result = day + 59;
				if(leapyear == 1)
				{
					result = result + 1;
				}
			}
			else
			{
				result = -1;
			}
			
		}

		else if(month == 4) // April
		{
			if (day <= 30)
			{
				result = day + 90;
				if(leapyear == 1)
				{
					result = result + 1;
				}
			}
			else
			{
				result = -1;
			}
		}

		else if(month == 5) // May
		{
			if (day <= 31)
			{
				result = day + 120;
				if(leapyear == 1)
				{
					result = result + 1;
				}
			}
			else
			{
				result = -1;
			}
		}

		else if(month == 6) // June
		{
			if (day <= 30)
			{
				result = day + 151;
				if(leapyear == 1)
				{
					result = result + 1;
				}
			}
			else
			{
				result = -1;
			}
		}

		else if(month == 7) // July
		{
			if (day <= 31)
			{
				result = day + 181;
				if(leapyear == 1)
				{
					result = result + 1;
				}
			}
			else
			{
				result = -1;
			}
		}

		else if(month == 8) // August
		{
			if (day <= 31)
			{
				result = day + 212;
				if(leapyear == 1)
				{
					result = result + 1;
				}
			}
			else
			{
				result = -1;
			}
		}

		else if(month == 9) // Spetember
		{
			if (day <= 30)
			{
				result = day + 243;
				if(leapyear == 1)
				{
					result = result + 1;
				}
			}
			else
			{
				result = -1;
			}
		}

		else if(month == 10) // October
		{
			if (day <= 31)
			{
				result = day + 273;
				if(leapyear == 1)
				{
					result = result + 1;
				}
			}
			else
			{
				result = -1;
			}
		}

		else if(month == 11) // November
		{
			if (day <= 30)
			{
				result = day + 304;
				if(leapyear == 1)
				{
					result = result + 1;
				}
			}
			else
			{
				result = -1;
			}
		}

		else // December
		{
			if (day <= 31)
			{
				result = day + 334;
				if(leapyear == 1)
				{
					result = result + 1;
				}
			}
			else
			{
				result = -1;
			}
		}
	}

	else
	{
		result = -1;
	}

	return result;
}

double difficulty_rating (void) // test case 18
{
	return 2.5;
}

double hours_invested (void) // test case 19
{
	return 4;
}

double prior_experience (void) // test case 20
{
	return 3.5;
}
