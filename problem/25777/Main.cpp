#include <iostream>
#include <queue>

#define MAX_N 1000
#define MAX_K 20

using namespace std;

int N;
int K;
char WORDS[MAX_N][MAX_K+1];

// union-find

int uf_rank[MAX_N];

void uf_init(int N) {
    for (int i = 0; i < N; i++) {
        uf_rank[i] = i;
    }
}

int uf_find(int u)
{
    if (uf_rank[u] != uf_rank[uf_rank[u]])
        uf_rank[u] = uf_find(uf_rank[u]);
    return uf_rank[u];
}

void uf_union(int u, int v) {
    u = uf_find(u);
    v = uf_find(v);
    if (u > v) {
        uf_union(v, u);
    } else {
        uf_rank[v] = uf_rank[u];
    }
}

//

int calc_edge_cost(int u, int v) {
    int cost = 0;
    for (int i = 0; i < K; i++) {
        cost += abs(WORDS[u][i] - WORDS[v][i]);
    }
    return cost;
}

int main()
{
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);

    cin >> N >> K;
    for (int i = 0; i < N; i++) {
        cin >> WORDS[i];
    }

    uf_init(N);

    priority_queue<pair<int, pair<int, int>>> pq;
    for (int u = 0; u < N; u++) {
        for (int v = 0; v < u; v++) {
            int w = calc_edge_cost(u, v);
            pq.push(make_pair(-w, make_pair(u, v)));
        }
    }

    int max_w = 0;
    while (!pq.empty()) {
        pair<int, pair<int, int>> node = pq.top();
        pq.pop();
        int u = node.second.first;
        int v = node.second.second;
        int w = -node.first;
        if (uf_find(u) != uf_find(v)) {
            uf_union(u, v);
            if (w > max_w) {
                max_w = w;
            }
        }
    }
    cout << max_w << endl;
    return 0;
}