#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int *ptr = malloc(sizeof(int));
	*ptr = 999;
	return 0;
}
