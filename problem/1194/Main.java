// 1194번: 달이 차오른다, 가자.

import java.io.*;
import java.util.*;

public class Main {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static final int MAX_H = 50;
    static final int MAX_W = 50;
    static final int MAX_KEY_PAIRS = 6;
    static final int MAX_LOCK_STATE = (1 << Main.MAX_KEY_PAIRS) - 1;

    static final int[] DR = { -1, 0, 0, 1 };
    static final int[] DC = { 0, -1, 1, 0 };

    static int H;
    static int W;

    static char[][] grid = new char[MAX_H][MAX_W];

    public static void main(String[] args) throws IOException {
        String[] tokens = br.readLine().split(" ");

        H = Integer.parseInt(tokens[0]);
        W = Integer.parseInt(tokens[1]);

        for (int lockState = 0; lockState <= MAX_LOCK_STATE; lockState++)
            for (int r = 0; r < H; r++)
                for (int c = 0; c < W; c++)
                    Node.instances[lockState][r][c].visited = false;

        for (int r = 0; r < H; r++) {
            String line = br.readLine();
            for (int c = 0; c < W; c++)
                grid[r][c] = line.charAt(c);
        }

        System.out.println(solve());
    }

    static int solve() {
        Queue<Node> queue = new ArrayDeque<>();
        int dist = 0;

        for (int r = 0; r < H; r++)
            for (int c = 0; c < W; c++)
                if (isStart(r, c)) {
                    Node node = Node.instances[MAX_LOCK_STATE][r][c];
                    node.visited = true;
                    queue.offer(node);
                }

        while (queue.size() > 0) {
            for (int breadth = queue.size(); breadth > 0; breadth--) {
                Node node = queue.poll();

                if (isEnd(node.r, node.c))
                    return dist;

                for (int d = 0; d < 4; d++) {
                    int nr = node.r + DR[d];
                    int nc = node.c + DC[d];
                    int nState = tryOpenDoor(node.r, node.c, node.state);

                    if (isOutOfRange(nr, nc))
                        continue;

                    if (isWall(nr, nc))
                        continue;

                    if (isDoor(nr, nc) && hasKey(nr, nc, nState))
                        continue;

                    Node nextNode = Node.instances[nState][nr][nc];

                    if (nextNode.visited)
                        continue;

                    nextNode.visited = true;
                    queue.offer(nextNode);
                }
            }
            dist++;
        }
        return -1;
    }

    static int tryOpenDoor(int r, int c, int state) {
        if (isKey(r, c)) {
            return state & ~(1 << (grid[r][c] - 'a'));
        }
        return state;
    }

    static boolean hasKey(int r, int c, int state) {
        return (state & (1 << (grid[r][c] - 'A'))) > 0;
    }

    static boolean isOutOfRange(int r, int c) {
        return r < 0 || r >= H || c < 0 || c >= W;
    }

    static boolean isKey(int r, int c) {
        return 'a' <= grid[r][c] && grid[r][c] <= 'z';
    }

    static boolean isDoor(int r, int c) {
        return 'A' <= grid[r][c] && grid[r][c] <= 'Z';
    }

    static boolean isWall(int r, int c) {
        return grid[r][c] == '#';
    }

    static boolean isStart(int r, int c) {
    return grid[r][c] == '0';
    }

    static boolean isEnd(int r, int c) {
        return grid[r][c] == '1';
    }
}

class Node {
    static Node[][][] instances = new Node[Main.MAX_LOCK_STATE + 1][Main.MAX_H][Main.MAX_W];

    static {
        for (int state = 0; state <= Main.MAX_LOCK_STATE; state++) {
            for (int r = 0; r < Main.MAX_H; r++) {
                for (int c = 0; c < Main.MAX_W; c++) {
                    instances[state][r][c] = new Node(state, r, c);
                }
            }
        }
    }

    int state;
    int r;
    int c;
    boolean visited;

    Node(int state, int r, int c) {
        this.state = state;
        this.r = r;
        this.c = c;
    }
}
