// 7562번: 나이트의 이동

import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

class Main {
    private static final BufferedReader br;
    public static final int[] DR = { -2, -2, -1, -1, 1, 1, 2, 2 };
    public static final int[] DC = { -1, 1, -2, 2, -2, 2, -1, 1 };
    public static final int MAX_L = 300;
    public static final int INF = 0;

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    public static void main(String[] args) throws IOException {
        int T;
        int l;
        int sr, sc;
        int er, ec;
        String[] tokens;
        T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            l = Integer.parseInt(br.readLine());
            tokens = br.readLine().split(" ");
            sr = Integer.parseInt(tokens[0]);
            sc = Integer.parseInt(tokens[1]);
            tokens = br.readLine().split(" ");
            er = Integer.parseInt(tokens[0]);
            ec = Integer.parseInt(tokens[1]);
            System.out.println(solveTestcase(l, sr, sc, er, ec));
        }
    }

    private static int solveTestcase(final int l, final int sr, final int sc, final int er, final int ec) {
        int r, c, nr, nc, d;
        int moves;
        boolean[][] visited = new boolean[MAX_L][MAX_L];
        Queue<Integer> queueR = new LinkedList<>();
        Queue<Integer> queueC = new LinkedList<>();
        int queueWidth;
        for (r = 0; r < l; r++) {
            for (c = 0; c < l; c++) {
                visited[r][c] = false;
            }
        }
        visited[sr][sc] = true;
        queueR.add(sr);
        queueC.add(sc);
        moves = 0;
        while (!queueR.isEmpty() && !queueC.isEmpty()) {
            for (queueWidth = queueR.size(); queueWidth > 0; queueWidth--) {
                r = queueR.poll();
                c = queueC.poll();
                if (r == er && c == ec) {
                    return moves;
                }
                for (d = 0; d < DR.length; d++) {
                    nr = r + DR[d];
                    nc = c + DC[d];
                    if (nr < 0 || nr >= l || nc < 0 || nc >= l) {
                        continue;
                    }
                    if (visited[nr][nc]) {
                        continue;
                    }
                    visited[nr][nc] = true;
                    queueR.add(nr);
                    queueC.add(nc);
                }
            }
            moves++;
        }
        return -1;
    }
}
