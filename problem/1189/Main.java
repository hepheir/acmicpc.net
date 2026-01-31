// 1189번: 컴백홈

import java.io.*;

class Main {
    static final int MAX_R = 5;
    static final int MAX_C = 5;
    static final int[] DY = { -1, 0, 1, 0 };
    static final int[] DX = { 0, 1, 0, -1 };

    static int R;
    static int C;
    static int K;

    static final boolean[][] isWall = new boolean[MAX_R][MAX_C];
    static boolean[][] visited = new boolean[MAX_R][MAX_C];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tokens = br.readLine().split(" ");

        R = Integer.parseInt(tokens[0]);
        C = Integer.parseInt(tokens[1]);
        K = Integer.parseInt(tokens[2]);

        for (int y = 0; y < R; y++) {
            String line = br.readLine();
            for (int x = 0; x < C; x++) {
                isWall[y][x] = (line.charAt(x) == 'T');
            }
        }

        System.out.println(solveBT(R - 1, 0, 1));
    }

    static int solveBT(int y, int x, int depth) {
        // 더 이상 유효하지 않은 경로 걸러내기.
        if (!isBound(y, x)) // 경계 밖인 경우.
            return 0;
        if (depth > K) // K번 초과로 움직였을 경우
            return 0;
        if (visited[y][x]) // 왔던 길을 반복하는 경우
            return 0;
        if (isWall[y][x]) // 갈 수 없는 길인 경우
            return 0;
        if (y == 0 && x == C - 1)
            return (depth == K) ? 1 : 0;

        // 백트래킹을 하는 부분.
        visited[y][x] = true;
        int retval = 0;
        for (int dir = 0; dir < 4; dir++)
            retval += solveBT(y + DY[dir], x + DX[dir], depth + 1);
        visited[y][x] = false;
        return retval;
    }

    static boolean isBound(int y, int x) {
        return (0 <= y && y < R && 0 <= x && x < C);
    }
}
