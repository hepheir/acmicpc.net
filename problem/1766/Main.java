// 1766번: 문제집

import java.io.*;
import java.util.*;


class Main {
    private static final BufferedReader br;
    private static final Map<Integer, List<Integer>> graph;
    private static final Map<Integer, Integer> dependencies;
    private static String [] buffer;
    private static int N, M;

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
        graph = new HashMap<>();
        dependencies = new HashMap<>();
    }

    public static void main(String[] args) throws IOException {
        int A, B;
        buffer = br.readLine().split(" ");
        N = Integer.parseInt(buffer[0]);
        M = Integer.parseInt(buffer[1]);
        for (int n = 1; n <= N; n++) {
            graph.put(n, new ArrayList<>());
            dependencies.put(n, 0);
        }
        for (int i = 0; i < M; i++) {
            buffer = br.readLine().split(" ");
            A = Integer.parseInt(buffer[0]);
            B = Integer.parseInt(buffer[1]);
            graph.get(A).add(B);
            dependencies.put(B, dependencies.get(B) + 1);
        }
        Queue<Integer> queue = new PriorityQueue<>();
        StringBuilder answer = new StringBuilder();
        for (int n = 1; n <= N; n++) {
            if (dependencies.get(n) > 0) {
                continue;
            }
            queue.add(n);
        }
        while (!queue.isEmpty()) {
            int u = queue.poll();
            answer.append(u).append(" ");
            for (int v : graph.get(u)) {
                dependencies.put(v, dependencies.get(v) - 1);
                if (dependencies.get(v) == 0) {
                    queue.add(v);
                }
            }
        }
        System.out.println(answer);
    }
}
