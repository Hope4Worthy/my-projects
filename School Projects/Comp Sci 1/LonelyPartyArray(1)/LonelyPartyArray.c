// name
// COP 3502C - Spring
// br727153

#include "LonelyPartyArray.h"
#include <stdio.h>
#include <stdlib.h>

int index_validity_check(LonelyPartyArray *party, int index)
{
	if(index < 0 || index > (getCapacity(party) - 1))
	{
		return 1;
	}
	return 0;
}

int low_indicie_finder(LonelyPartyArray *party, int fragment_pos)
{
		return ((fragment_pos) * party->fragment_length);
}

int high_indice_finder(LonelyPartyArray *party, int fragment_pos)
{
	return ((fragment_pos + 1) * party->fragment_length) - 1;
}

void create_fragment(LonelyPartyArray *party, int fragment_pos)
{
	int i;
	party->fragments[fragment_pos] = malloc(sizeof(int) * party->fragment_length);

	party->num_active_fragments++;

	for(i = 0; i < party->fragment_length; i++)
	{
		party->fragments[fragment_pos][i] = UNUSED;
	}

	printf("-> Spawned fragment %d. (capacity: %d, indices: %d..%d)\n", fragment_pos, party->fragment_length, low_indicie_finder(party, fragment_pos), high_indice_finder(party, fragment_pos));
}

void destroy_fragment(LonelyPartyArray *party, int fragment_pos)
{
	party->num_active_fragments--;
	free(party->fragments[fragment_pos]);
	party->fragments[fragment_pos] = NULL;

	printf("-> Deallocated fragment %d. (capacity: %d, indices: %d..%d)\n", fragment_pos, party->fragment_length, low_indicie_finder(party, fragment_pos), high_indice_finder(party, fragment_pos));
	
}

int getSize(LonelyPartyArray *party)
{
	if(party == NULL)
	{
		return -1;
	}
	return party->size;
}

int getCapacity(LonelyPartyArray *party)
{
	if(party == NULL)
	{
		return -1;
	}

	return (party->num_fragments * party->fragment_length);
}

int getAllocatedCellCount(LonelyPartyArray *party)
{
	if(party == NULL)
	{
		return -1;
	}

	return (party->num_active_fragments * party->fragment_length);
}

long long unsigned int getArraySizeInBytes(LonelyPartyArray *party)
{
	if(party == NULL)
	{
		return 0;
	}

	return (getCapacity(party) * sizeof(int));
}

long long unsigned int getCurrentSizeInBytes(LonelyPartyArray *party)
{
	if(party == NULL)
	{
		return 0;
	}

	return(sizeof(LonelyPartyArray*) + sizeof(LonelyPartyArray) + (sizeof(int*) * party->num_fragments) + (sizeof(int) * party->num_fragments) + ((party->num_active_fragments * party->fragment_length) * sizeof(int)));
}

LonelyPartyArray *createLonelyPartyArray(int num_fragments, int fragment_length)
{
	int i;
	LonelyPartyArray *LPA = malloc(sizeof(LonelyPartyArray));

	if(num_fragments <= 0 || fragment_length <= 0)
	{
		return NULL;
	}

	LPA->num_fragments = num_fragments;
	LPA->fragment_length = fragment_length;
	LPA->fragments = malloc(sizeof(int*) * num_fragments);
	LPA->fragment_sizes = malloc(sizeof(int) * num_fragments);

	if(LPA->fragments == NULL || LPA->fragment_sizes == NULL)
	{
		free(LPA->fragments);
		free(LPA->fragment_sizes);
		return NULL;
	}

	for(i = 0; i < num_fragments; i++)
	{
		LPA->fragments[i] = NULL;
	}
	for(i = 0; i < num_fragments; i++)
	{
		LPA->fragment_sizes[i] = 0;
	}

	printf("-> A new LonelyPartyArray has emerged from the void. (capacity: %d, fragments: %d)\n", (num_fragments * fragment_length), num_fragments);
	
	return LPA;
}

LonelyPartyArray *destroyLonelyPartyArray(LonelyPartyArray *party)
{
	int i;

	if(party == NULL)
	{
		return NULL;
	}

	for(i = 0; i < party->num_fragments; i++)
	{
		free(party->fragments[i]);
	}
	free(party->fragment_sizes);
	free(party->fragments);
	free(party);

	printf("-> The LonelyPartyArray has returned to the void.\n");

	return NULL;
}

int set(LonelyPartyArray *party, int index, int key)
{
	int fragment_pos, index_pos;

	if(party == NULL)
	{
		printf("-> Bloop! NULL pointer detected in set().\n");
		return LPA_FAILURE;
	}

	fragment_pos = index / party->fragment_length;
	index_pos = index % party->fragment_length;

	if(index_validity_check(party, index))
	{
		printf("-> Bloop! Invalid access in set(). (index: %d, fragment: %d, offset: %d)\n", index, fragment_pos, index_pos);
		return LPA_FAILURE;
	}

	if(party->fragments[fragment_pos] == NULL)
	{
		create_fragment(party, fragment_pos);

		if(party->fragments[fragment_pos] == NULL)
		{
			return LPA_FAILURE;
		}

	}
	if(party->fragments[fragment_pos][index_pos] == UNUSED)
	{
		party->size++;
		party->fragment_sizes[fragment_pos]++;
	}
	party->fragments[fragment_pos][index_pos] = key;

	return LPA_SUCCESS;

	
}

int get(LonelyPartyArray *party, int index)
{
	int fragment_pos, index_pos;

	if(party == NULL)
	{
		printf("-> Bloop! NULL pointer detected in get().\n");
		return LPA_FAILURE;
	}

	fragment_pos = index / party->fragment_length;
	index_pos = index % party->fragment_length;

	if(index_validity_check(party, index))
	{
		printf("-> Bloop! Invalid access in get(). (index: %d, fragment: %d, offset: %d)\n", index, fragment_pos, index_pos);
		return LPA_FAILURE;
	}

	if(party->fragments[fragment_pos] == NULL)
	{
		return UNUSED;
	}
	if(party->fragments[fragment_pos][index_pos] == UNUSED)
	{
		return UNUSED;
	}

	return party->fragments[fragment_pos][index_pos];
}

int delete(LonelyPartyArray *party, int index)
{
	int fragment_pos, index_pos;

	if(party == NULL)
	{
		printf("-> Bloop! NULL pointer detected in delete().\n");
		return LPA_FAILURE;
	}

	fragment_pos = index / party->fragment_length;
	index_pos = index % party->fragment_length;

	if(index_validity_check(party, index))
	{
		printf("-> Bloop! Invalid access in delete(). (index: %d, fragment: %d, offset: %d)\n", index, fragment_pos, index_pos);
		return LPA_FAILURE;
	}

	if(party->fragments[fragment_pos] == NULL)
	{
		return LPA_FAILURE;
	}
	if(party->fragments[fragment_pos][index_pos] == UNUSED)
	{
		return LPA_FAILURE;
	}

	party->fragments[fragment_pos][index_pos] = UNUSED;
	party->fragment_sizes[fragment_pos]--;	
	party->size--;

	if(party->fragment_sizes[fragment_pos] <= 0)
	{
		destroy_fragment(party, fragment_pos);
	}

	return LPA_SUCCESS;
}

int containsKey(LonelyPartyArray *party, int key)
{
	int i, j;
	if(party == NULL)
	{
		return 0;
	}

	for(i = 0; i < party->num_fragments; i++)
	{
		for(j = 0; j < party->fragment_length; j++)
		{
			if(party->fragments[i][j] == key);
			{
				return 1;
			}
		}
	}

	return 0;
}

int isSet(LonelyPartyArray *party, int index)
{
	int fragment_pos, index_pos;

	if(party == NULL || index_validity_check(party, index))
	{
		return 0;
	}

	fragment_pos = index / party->fragment_length;
	index_pos = index % party->fragment_length;

	if(party->fragments[fragment_pos] == NULL || party->fragments[fragment_pos][index_pos] == UNUSED)
	{
		return 0;
	}

	return 1;
}

int printIfValid(LonelyPartyArray *party, int index)
{
	int fragment_pos, index_pos;

	if(party == NULL)
	{
		return LPA_FAILURE;
	}

	if(index_validity_check(party, index))
	{
		return LPA_FAILURE;
	}

	fragment_pos = index / party->fragment_length;
	index_pos = index % party->fragment_length;

	if(party->fragments[fragment_pos] == NULL)
	{
		return LPA_FAILURE;
	}

	if(party->fragments[fragment_pos][index_pos] == UNUSED)
	{
		return LPA_FAILURE;
	}

	printf("%d\n", party->fragments[fragment_pos][index_pos]);

	return LPA_SUCCESS;
}

LonelyPartyArray *resetLonelyPartyArray(LonelyPartyArray *party)
{
	int i;

	if(party == NULL)
	{
		printf("-> Bloop! NULL pointer detected in resetLonleyPartyArray().");
		return party;
	}

	party->num_active_fragments = 0;
	party->size = 0;

	for(i = 0; i < party->num_fragments; i++)
	{
		free(party->fragments[i]);
		party->fragments[i] = NULL;
	}

	for(i = 0; i < party->fragment_length; i++)
	{
		party->fragment_sizes[i] = 0;
	}

	printf("-> The LonelyPartyArray has returned to its nascent state. (capacity: %d, fragments: %d)\n", (getCapacity(party)), party->num_fragments);

	return party;
}

double difficultyRating(void)
{
	return 2;
}

double hoursSpent(void)
{
	return 6;
}
