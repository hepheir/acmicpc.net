#include "bogoSort.h"

std::vector<int> bubble(int N, int x)
{
	std::vector<int> v = copy_array();
	int e = N-1;
	while (v.at(x) != x)
	{
		while (v.at(e) != x) e--;
		shuffle_array(x, e);
		v = copy_array();
	}
	return v;
}

void sort_array(int N)
{
	std::vector<int> v = copy_array();
	int s = 0;
	int e = N - 1;
	while (s < N)
	{
		while (v.at(s) == s && s < e) s++;
		while (v.at(e) == e && s < e) e--;
		v = bubble(N, s);
		s++;
	}
}
