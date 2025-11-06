// 1446번: 지름길

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

class Main {
    public static final int MAX_D = 10000;
    private static final int[] dist = new int[MAX_D + 1];

    private static class Edge {
        public int v;
        public int w;

        Edge(int v, int w) {
            this.v = v;
            this.w = w;
        }
    }

    public static void main(String[] args) throws IOException {
        int N, D;
        int u, v, w;
        int i, d;
        Map<Integer, List<Edge>> adjList = new HashMap<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        for (i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            if (!adjList.containsKey(u)) {
                adjList.put(u, new ArrayList<>());
            }
            adjList.get(u).add(new Edge(v, w));
        }
        dist[0] = 0;
        for (d = 0; d < D; d++) {
            dist[d + 1] = dist[d] + 1;
        }
        for (d = 0; d < D; d++) {
            dist[d + 1] = Math.min(dist[d + 1], dist[d] + 1);
            if (adjList.containsKey(d)) {
                for (Edge edge : adjList.get(d)) {
                    dist[edge.v] = Math.min(dist[edge.v], dist[d] + edge.w);
                }
            }
        }
        System.out.print(dist[D]);
    }
}
