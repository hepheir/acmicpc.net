#include <cstring>
#include <iostream>

#define MAX_N 3000
#define CACHE_UNDETERMINED -1
#define CACHE_WIN 1
#define CACHE_LOSE 0

using namespace std;

int N;
int A[MAX_N];
int cache[MAX_N][MAX_N][2][2];

bool can_win(int s, int e, bool p1_is_odd, bool p2_is_odd)
{
    // e is exclusive
    if (s == e)
        return !p1_is_odd;
    if (cache[s][e][p1_is_odd][p2_is_odd] == CACHE_UNDETERMINED)
    {
        cache[s][e][p1_is_odd][p2_is_odd] = CACHE_LOSE;
        if ((s + 1 < e) && !can_win(s + 2, e, p2_is_odd, (p1_is_odd + A[s] + A[s + 1]) % 2))
            cache[s][e][p1_is_odd][p2_is_odd] = CACHE_WIN;
        if ((s < e - 1) && !can_win(s, e - 2, p2_is_odd, (p1_is_odd + A[e - 1] + A[e - 2]) % 2))
            cache[s][e][p1_is_odd][p2_is_odd] = CACHE_WIN;
        if (!can_win(s + 1, e, p2_is_odd, (p1_is_odd + A[s]) % 2))
            cache[s][e][p1_is_odd][p2_is_odd] = CACHE_WIN;
        if (!can_win(s, e - 1, p2_is_odd, (p1_is_odd + A[e - 1]) % 2))
            cache[s][e][p1_is_odd][p2_is_odd] = CACHE_WIN;
    }
    return cache[s][e][p1_is_odd][p2_is_odd];
}

int main()
{
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);

    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> A[i];
    memset(cache, CACHE_UNDETERMINED, sizeof(cache));
    cout << ((can_win(0, N, 0, 0) == CACHE_WIN) ? "Yes" : "No") << endl;

    return 0;
}