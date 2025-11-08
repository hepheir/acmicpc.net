// 2665번: 미로만들기

import java.io.*;
import java.util.PriorityQueue;

class Main {
    public static final int MAX_N = 50;
    public static final int MAX_DIST = MAX_N * MAX_N + 1;
    public static final int[] DX = { 0, 0, 1, -1 };
    public static final int[] DY = { 1, -1, 0, 0 };
    private static int n;
    private static int[][] grid = new int[MAX_N][MAX_N];
    private static int[][] dist = new int[MAX_N][MAX_N];

    private static class Node implements Comparable<Node> {
        public int x;
        public int y;
        public int d;

        public Node(int x, int y, int d) {
            this.x = x;
            this.y = y;
            this.d = d;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.d, other.d);
        }
    }

    public static void main(String[] args) throws IOException {
        int x, y;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        for (y = 0; y < n; y++) {
            String line = br.readLine();
            for (x = 0; x < n; x++) {
                grid[y][x] = line.charAt(x) - '0';
                dist[y][x] = MAX_DIST;
            }
        }
        System.out.println(solve());
    }

    private static int solve() {
        int i;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        Node node, nextNode;
        node = new Node(0, 0, 0);
        dist[node.x][node.y] = node.d;
        pq.offer(node);
        while (!pq.isEmpty()) {
            node = pq.poll();
            if (node.x == n - 1 && node.y == n - 1) {
                pq.clear();
                return node.d;
            }
            for (i = 0; i < 4; i++) {
                if (!isVisitable(node.x+DX[i], node.y+DY[i])) {
                    continue;
                }
                nextNode = new Node(node.x+DX[i], node.y+DY[i], node.d);
                if (grid[nextNode.x][nextNode.y] == 0) {
                    nextNode.d++;
                }
                if (dist[nextNode.x][nextNode.y] > nextNode.d) {
                    dist[nextNode.x][nextNode.y] = nextNode.d;
                    pq.offer(nextNode);
                }
            }
        }
        throw new RuntimeException("도달 할 수 없는 경우.");
    }

    private static boolean isVisitable(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < n;
    }
}
