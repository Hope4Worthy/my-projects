#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int *data = malloc(sizeof(int) * 100);
    free(&data[50]);
	return 0;
}
