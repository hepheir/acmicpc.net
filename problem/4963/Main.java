// 4963번: 섬의 개수

import java.io.*;
import java.util.*;

class Main {
    private static final int LAND = 1;
    private static final int MAX_W = 50;
    private static final int MAX_H = 50;

    private static final boolean[][] isVisitable = new boolean[MAX_H][MAX_W];

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int w, h;
        int x, y;
        int islandCount;
        while (true) {
            st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());
            if (w == 0 && h == 0) {
                break;
            }
            for (y = 0; y < h; y++) {
                st = new StringTokenizer(br.readLine());
                for (x = 0; x < w; x++) {
                    setIsVisitable(x, y, (Integer.parseInt(st.nextToken()) == LAND));
                }
            }
            islandCount = 0;
            for (y = 0; y < h; y++) {
                for (x = 0; x < w; x++) {
                    if (isVisitable(x, y)) {
                        visitLandAt(x, y);
                        islandCount++;
                    }
                }
            }
            System.out.println(islandCount);
        }
    }

    private static void visitLandAt(int x, int y) {
        int dx, dy;
        Stack<Integer> stackX = new Stack<>();
        Stack<Integer> stackY = new Stack<>();
        stackX.push(x);
        stackY.push(y);
        while (!stackX.isEmpty() && !stackY.isEmpty()) {
            x = stackX.pop();
            y = stackY.pop();
            if (!isVisitable(x, y)) {
                continue;
            }
            setIsVisitable(x, y, false);
            for (dx = -1; dx <= 1; dx++) {
                for (dy = -1; dy <= 1; dy++) {
                    stackX.push(x + dx);
                    stackY.push(y + dy);
                }
            }
        }
    }

    private static boolean isVisitable(int x, int y) {
        if (x < 0 || x >= MAX_W || y < 0 || y >= MAX_H)
            return false;
        return isVisitable[y][x];
    }

    private static void setIsVisitable(int x, int y, boolean value) {
        isVisitable[y][x] = value;
    }
}