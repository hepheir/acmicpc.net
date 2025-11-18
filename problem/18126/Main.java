// 18126번: 너구리 구구

import java.io.*;
import java.util.*;

class Main {
    public static final int MAX_N = 5000;
    public static final int MAX_C = 1000000000;
    public static final long INF = (long) MAX_N * (long) MAX_C;
    private static final BufferedReader br;
    private static final long[] dist = new long[MAX_N + 1];
    private static final Map<Integer, Map<Integer, Long>> graph = new HashMap<>();

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
        for (int u = 1; u <= MAX_N; u++) {
            dist[u] = INF;
            graph.put(u, new HashMap<>());
        }
    }

    public static void main(String[] args) throws IOException {
        String[] tokens;
        int A, B;
        long C;
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N - 1; i++) {
            tokens = br.readLine().split(" ");
            A = Integer.parseInt(tokens[0]);
            B = Integer.parseInt(tokens[1]);
            C = Long.parseLong(tokens[2]);
            if (graph.get(A).getOrDefault(B, INF) > C) {
                graph.get(A).put(B, C);
            }
            if (graph.get(B).getOrDefault(A, INF) > C) {
                graph.get(B).put(A, C);
            }
        }
        updateDist();
        System.out.println(findMaxDist(N));
    }

    private static void updateDist() {
        // via graph traversal at O(V+E)
        int u, v;
        long w;
        Stack<Integer> stack = new Stack<>();
        dist[1] = 0;
        stack.push(1);
        while (!stack.isEmpty()) {
            u = stack.pop();
            for (Map.Entry<Integer, Long> entry : graph.get(u).entrySet()) {
                v = entry.getKey();
                w = entry.getValue();
                if (dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;
                    stack.push(v);
                }
            }
        }
    }

    private static long findMaxDist(int N) {
        long maxDist = dist[1];
        for (int u = 2; u <= N; u++) {
            if (dist[u] != INF && dist[u] > maxDist) {
                maxDist = dist[u];
            }
        }
        return maxDist;
    }
}
