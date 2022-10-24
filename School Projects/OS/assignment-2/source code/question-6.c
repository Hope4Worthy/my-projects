#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int i;
	int *data = malloc(sizeof(int) * 100);
	for (i = 0; i < 100; i++)
	{
		data[i] = i + 1;
	}
	free(data);
	printf("%d\n", data[0]);
	return 0;
}
