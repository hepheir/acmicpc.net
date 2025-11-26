// 17484번: 진우의 달 여행 (Small)

import java.io.*;

class Main {
    private static final BufferedReader br;
    private static final int MAX_N = 6;
    private static final int MAX_M = 6;
    private static final int UNREACHABLE = Integer.MAX_VALUE;
    private static final int NOT_CACHED = Integer.MAX_VALUE;
    private static int N;
    private static int M;
    private static int[][] grid = new int[MAX_N][MAX_M];
    private static int[][][] getMinDistCache = new int[MAX_N][MAX_M][3];

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < MAX_N; i++) {
            for (int j = 0; j < MAX_M; j++) {
                for (int k = 0; k < 3; k++) {
                    getMinDistCache[i][j][k] = NOT_CACHED;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        String[] tokens = br.readLine().split(" ");
        N = Integer.parseInt(tokens[0]);
        M = Integer.parseInt(tokens[1]);
        for (int i = 0; i < N; i++) {
            tokens = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                grid[i][j] = Integer.parseInt(tokens[j]);
            }
        }
        System.out.println(getMinDist());
    }

    private static int getMinDist() {
        int minDist = UNREACHABLE;
        for (int c = 0; c < M; c++) {
            for (int dc = -1; dc <= 1; dc++) {
                minDist = Math.min(minDist, getMinDistNaive(0, c, dc));
            }
        }
        return minDist;
    }

    private static int getMinDistDP(int r, int c, int dc_in) {
        if (r == N) {
            return 0;
        }
        if (!validate(r, c)) {
            return UNREACHABLE;
        }
        int k = (dc_in + 3) % 3;
        if (getMinDistCache[r][c][k] == NOT_CACHED) {
            getMinDistCache[r][c][k] = getMinDistNaive(r, c, dc_in);
        }
        return getMinDistCache[r][c][k];
    }

    private static int getMinDistNaive(int r, int c, int dc_in) {
        if (r == N) {
            return 0;
        }
        if (!validate(r, c)) {
            return UNREACHABLE;
        }
        int minDist = UNREACHABLE;
        for (int dc_out = -1; dc_out <= 1; dc_out++) {
            if (dc_in == dc_out) {
                continue;
            }
            minDist = Math.min(minDist, getMinDistNaive(r + 1, c + dc_out, dc_out));
        }
        return minDist + grid[r][c];
    }

    private static boolean validate(int r, int c) {
        return 0 <= r && r < N && 0 <= c && c < M;
    }
}
