#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int *data = malloc(sizeof(int) * 100);
	data[100] = 0;
	return 0;
}
