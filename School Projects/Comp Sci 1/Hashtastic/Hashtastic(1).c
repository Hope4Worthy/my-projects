// name
// br727153

#include "Hashtastic.h"

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int nextPrime(int n)
{
	int i, root, keepGoing = 1;

	if (n % 2 == 0)
		++n;

	while (keepGoing)
	{
		keepGoing = 0;

		// =============================================================
		// Compilation Note Related to sqrt() Function
		// =============================================================
		// Be sure to #include <math.h> and use the -lm flag to compile:
		//
		//    gcc Hashtastic.c -lm
		// =============================================================

		root = sqrt(n);

		for (i = 3; i <= root; i++)
		{
			if (n % i == 0)
			{
				// Move on to the next candidate for primality. Since n is odd,
				// we don't want to increment it by 1. That would give us an
				// even integer greater than 2, which would necessarily be
				// non-prime.
				n += 2;
				keepGoing = 1;

				// Leave for-loop. Move on to next iteration of while-loop.
				break;
			}
		}
	}

	return n;	
}

HashTable *makeHashTable(int capacity)
{
	int i;
	HashTable *new_hash = malloc(sizeof(HashTable));

	if(new_hash == NULL)
		return NULL;

	if(capacity <= 0)
		new_hash->capacity = DEFAULT_CAPACITY;
	else
		new_hash->capacity = capacity;

	new_hash->probing = 0;

	new_hash->array = malloc(sizeof(int) * new_hash->capacity);

	if(new_hash->array == NULL)
	{
		free(new_hash);
		return NULL;
	}

	for(i = 0; i < new_hash->capacity; i++)
	{
		new_hash->array[i] = UNUSED;
	}

	new_hash->size = 0;

	new_hash->stats.opCount = 0;
	new_hash->stats.collisions = 0;

	unsigned int (*hashFunction)(int) = NULL;

	return new_hash;
}

HashTable *destroyHashTable(HashTable *h)
{
	free(h->array);
	free(h);
	return NULL;
}

int setProbingMechanism(HashTable *h, ProbingType probing)
{
	if(h == NULL)
	{
		return HASH_ERR;
	}

	h->probing = probing;

	return HASH_OK;
}

int setHashFunction(HashTable *h, unsigned int (*hashFunction)(int))
{
	if(h == NULL)
		return HASH_ERR;

	h->hashFunction = (*hashFunction);

	return HASH_OK;
}

int isAtLeastHalfEmpty(HashTable *h)
{
	if(h == NULL || h->capacity == 0)
		return 0;

	if(h->size <= ((h->capacity) /2))
		return 1;

	return 0;
}

int expandHashTable(HashTable *h)
{
	int i, j;
	int index;
	int old_cap;
	int *new_array;

	if(h == NULL || h->hashFunction == NULL)
	{
		return HASH_ERR;
	}

	old_cap = h->capacity;

	if(h->probing == 0)
	{
		h->capacity = ((h->capacity) * 2) + 1;
	}
	else
	{
		h->capacity = nextPrime(((h->capacity) * 2) + 1);
	}

	new_array = malloc(sizeof(int) * h->capacity);

	for(i = 0; i < h->capacity; i++)
	{
		new_array[i] = UNUSED;
	}

	for(i = 0; i < old_cap; i++)
	{
		if(h->array[i] == UNUSED || h->array[i] == DIRTY)
		{
			continue;
		}

		index = (h->hashFunction(h->array[i])) % h->capacity;

		if(new_array[index] != UNUSED)
		{
			if(h->probing == 0)
			{
				while(new_array[index] != UNUSED)
				{
					h->stats.collisions += 1;
					index = (index + 1) % h->capacity; 
				}
			}
			else
			{
				for(j = 1; new_array[index] != UNUSED; j++)
				{
					index = (index - ((j-1)*(j-1))) % h->capacity;
					index = (index + (j*j)) % h->capacity;
				}
				h->stats.collisions += (j-1);
			}
		}
		new_array[index] = h->array[i];
	}
	free(h->array);
	h->array = new_array;

	return HASH_OK;
}

int insert(HashTable *h, int key)
{
	int i;
	int index;

	if(h == NULL || h->hashFunction == NULL)
		return HASH_ERR;

	if(!isAtLeastHalfEmpty(h))
	{
		if(expandHashTable(h) == HASH_ERR)
			return HASH_ERR;
	}

	index = (h->hashFunction(key)) % h->capacity;

	if(h->array[index] != UNUSED && h->array[index] != DIRTY)
	{
		if(h->probing == 0)
		{
			while(h->array[index] != UNUSED && h->array[index] != DIRTY)
			{
				h->stats.collisions += 1;
				index = (index + 1) % h->capacity;
			}
		}
		else
		{
			for(i = 1; h->array[index] != UNUSED && h->array[index] != DIRTY; i++)
			{
				index = (index - ((i-1)*(i-1))) % h->capacity;
					index = (index + (i*i)) % h->capacity;
			}
			h->stats.collisions += (i-1);
		}
	}

	h->array[index] = key;
	h->stats.opCount += 1;
	h->size += 1;

	return HASH_OK;
}

int search(HashTable *h, int key)
{
	int i;
	int index;
	int search_count = 0;

	h->stats.opCount += 1;

	if(h == NULL || h->hashFunction == NULL)
		return -1;

	index = (h->hashFunction(key)) % h->capacity;

	if(h->array[index] != key)
	{
		if(h->probing == 0)
		{
			while(h->array[index] != key && search_count != h->capacity)
			{
				if(h->array[index] == UNUSED)
					return -1;

				search_count++;
				h->stats.collisions += 1;
				index = (index + 1) % h->capacity; 
			}
		}
		else
		{
			for(i = 1; h->array[index] != key && search_count != h->capacity; i++)
			{
				if(h->array[index] == UNUSED)
				{
					h->stats.collisions += (i - 1);
					return -1;
				}

				search_count++;
				index = (index + (i*i)) % h->capacity; 
			}
			h->stats.collisions += (i - 1);
		}
	}

	if(search_count == h->capacity)
		return -1;

	return index;
}

int delete(HashTable *h, int key)
{
	int index = search(h, key);

	if(index == -1)
		return -1;

	h->array[index] = DIRTY;
	h->size -= 1;
	return index;
}

double difficultyRating(void)
{
	return 4;
}

double hoursSpent(void)
{
	return 10;
}
