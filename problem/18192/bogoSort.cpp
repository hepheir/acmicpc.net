#include "bogoSort.h"


void sort_array(int N)
{
	int i, j;
	std::vector<int> dest, curr;
	curr = copy_array();
	for (i = 0; i < N; i++)
		dest.push_back(curr.at(i));
	// Selection Sort: O(N^2)
	for (i = 0; i < N; i++)
		for (j = i+1; j < N; j++)
			if (dest.at(i) > dest.at(j))
				std::swap(dest[i], dest[j]);
	// Bogo Sort
	i = 0;
	j = N-1;
	while (i < j)
	{
		shuffle_array(i, j);
		curr = copy_array();
		while (curr.at(i) == dest.at(i) && i+1 < N) i++;
		while (curr.at(j) == dest.at(j) && 0 <= j-1) j--;
	}
}
