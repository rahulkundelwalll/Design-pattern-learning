#include <bits/stdc++.h>
using namespace std;

bool is_possible(int N, const unordered_set<int>& boosters, const vector<vector<int>>& adj, int P) {
    vector<int> steps(N + 1, -1);
    steps[1] = P; // Initialize starting node

    priority_queue<pair<int, int>> pq;
    pq.push({steps[1], 1});

    while (!pq.empty()) {
        int current_steps = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (u == N) return true;
        if (current_steps < steps[u]) continue; // Skip outdated entries

        for (int v : adj[u]) {
            if (current_steps < 1) continue; // Not enough power to move

            int new_steps = current_steps - 1;
            if (boosters.count(v)) {
                new_steps = P; // Reset to P if v is a booster
            }

            if (new_steps >= 0 && steps[v] < new_steps) {
                steps[v] = new_steps;
                pq.push({new_steps, v});
            }
        }
    }

    return false;
}

int solve(int N, int M, int K, int* energy, int** edges) {
    unordered_set<int> boosters;
    for (int i = 0; i < K; ++i) {
        boosters.insert(energy[i]);
    }

    // Build adjacency list
    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < M; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int low = 1;
    int high = N;
    int ans = -1;

    while (low <= high) {
        int mid = (low + high) / 2;
        if (is_possible(N, boosters, adj, mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return ans;
}

int main() {
    int N, M, K;
    cin >> N >> M >> K;

    int* energy = new int[K];
    for (int i = 0; i < K; i++) {
        cin >> energy[i];
    }

    int** edges = new int*[M];
    for (int i = 0; i < M; i++) {
        edges[i] = new int[2];
        cin >> edges[i][0] >> edges[i][1];
    }

    int result = solve(N, M, K, energy, edges);
    cout << result << endl;

    // Free dynamically allocated memory
    delete[] energy;
    for (int i = 0; i < M; i++) {
        delete[] edges[i];
    }
    delete[] edges;

    return 0;
}