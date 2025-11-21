// 17244번: 아맞다우산

import java.io.*;
import java.util.*;

class Main {
    private static final BufferedReader br;

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    private static class Node {
        public int r;
        public int c;

        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    private static final int MAX_WIDTH = 50;
    private static final int MAX_HEIGHT = 50;
    private static final int MAX_TARGET_NODES = 5;
    private static final int[] DR = { 0, 0, -1, 1 };
    private static final int[] DC = { -1, 1, 0, 0 };
    private static final char[][] grid;
    private static final List<Node> targetNodes;
    private static int width;
    private static int height;
    private static Node startNode;
    private static Node endNode;

    static {
        grid = new char[MAX_HEIGHT][MAX_WIDTH];
        targetNodes = new ArrayList<>(MAX_TARGET_NODES);
    }

    public static void main(String[] args) throws IOException {
        String tokens[] = br.readLine().split(" ");
        width = Integer.parseInt(tokens[0]);
        height = Integer.parseInt(tokens[1]);
        for (int r = 0; r < height; r++) {
            String line = br.readLine();
            for (int c = 0; c < width; c++) {
                grid[r][c] = line.charAt(c);
                switch (grid[r][c]) {
                    case 'S':
                        startNode = new Node(r, c);
                        break;
                    case 'E':
                        endNode = new Node(r, c);
                        break;
                    case 'X':
                        targetNodes.add(new Node(r, c));
                        break;
                }
            }
        }

        System.out.println(findMinDist());
    }

    private static int findMinDist() {
        Map<Node, Integer[][]> dist = new HashMap<>();
        Map<Node, Boolean> visitable = new HashMap<>();
        dist.put(startNode, nodeShortestPath(startNode));
        visitable.put(startNode, true);
        dist.put(endNode, nodeShortestPath(endNode));
        visitable.put(endNode, true);
        for (Node node : targetNodes) {
            dist.put(node, nodeShortestPath(node));
            visitable.put(node, true);
        }
        visitable.put(startNode, false);
        return traverseTargetNodesBT(startNode, visitable, dist);
    }

    private static int traverseTargetNodesBT(Node node, Map<Node, Boolean> visitable, Map<Node, Integer[][]> dist) {
        int minDist = Integer.MAX_VALUE;
        for (Node otherNode : targetNodes) {
            if (!visitable.get(otherNode))
                continue;
            visitable.put(otherNode, false);
            minDist = Math.min(minDist,
                    traverseTargetNodesBT(otherNode, visitable, dist) + dist.get(node)[otherNode.r][otherNode.c]);
            visitable.put(otherNode, true);
        }
        if (minDist == Integer.MAX_VALUE) {
            // 모든 타깃 노드(챙길 물건)를 방문했으므로 출구로 간다.
            return dist.get(node)[endNode.r][endNode.c];
        }
        return minDist;
    }

    private static Integer[][] nodeShortestPath(Node node) {
        return gridShortestPath(node.r, node.c);
    }

    private static Integer[][] gridShortestPath(int srcR, int srcC) {
        // O(NM)
        Integer gridDist[][] = new Integer[MAX_HEIGHT][MAX_WIDTH];
        int r, c, nr, nc;
        Queue<Integer> queueR = new LinkedList<>();
        Queue<Integer> queueC = new LinkedList<>();
        for (r = 0; r < height; r++) {
            for (c = 0; c < width; c++)
                gridDist[r][c] = Integer.MAX_VALUE;
        }
        gridDist[srcR][srcC] = 0;
        queueR.add(srcR);
        queueC.add(srcC);
        while (!queueR.isEmpty()) {
            r = queueR.poll();
            c = queueC.poll();
            for (int d = 0; d < 4; d++) {
                nr = r + DR[d];
                nc = c + DC[d];
                if (nr < 0 || height <= nr || nc < 0 || width <= nc)
                    continue;
                if (grid[nr][nc] == '#')
                    continue;
                if (gridDist[nr][nc] > gridDist[r][c] + 1) {
                    gridDist[nr][nc] = gridDist[r][c] + 1;
                    queueR.add(nr);
                    queueC.add(nc);
                }
            }
        }
        return gridDist;
    }
}
