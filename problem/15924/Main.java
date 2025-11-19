// 15924번: 욱제는 사과팬이야!!

import java.io.*;

class Main {
    public static final int MAX_N = 3000;
    public static final int MAX_M = 3000;
    public static final int MOD = 1000000009;
    private static final BufferedReader br;
    private static final char[][] grid = new char[MAX_N][MAX_M];
    private static final int[][] dp = new int[MAX_N][MAX_M];

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < MAX_N; i++) {
            for (int j = 0; j < MAX_M; j++) {
                dp[i][j] = -1;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        String line = br.readLine();
        int N = Integer.parseInt(line.split(" ")[0]);
        int M = Integer.parseInt(line.split(" ")[1]);
        for (int i = 0; i < N; i++) {
            line = br.readLine();
            for (int j = 0; j < M; j++) {
                grid[i][j] = line.charAt(j);
            }
        }
        int answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                answer = (answer + countCase(i, j)) % MOD;
            }
        }
        System.out.println(answer);
    }

    private static int countCase(int i, int j) {
        if (dp[i][j] == -1) {
            switch (grid[i][j]) {
                case 'E':
                    dp[i][j] = countCase(i, j + 1);
                    break;
                case 'S':
                    dp[i][j] = countCase(i + 1, j);
                    break;
                case 'B':
                    dp[i][j] = (countCase(i, j + 1) + countCase(i + 1, j)) % MOD;
                    break;
                case 'X':
                    dp[i][j] = 1;
                    break;
                default:
                    throw new AssertionError();
            }
        }
        return dp[i][j];
    }
}
