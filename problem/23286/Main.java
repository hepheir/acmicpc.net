import java.io.*;

public class Main {
    public static final int MAX_N = 300;
    public static final int MAX_H = 1000000;
    public static final int INF = MAX_H * MAX_N + 100; // not ovf.

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final int[][] dist = new int[MAX_N + 1][MAX_N + 1];

    static {
        for (int u = 1; u <= MAX_N; u++) {
            for (int v = 1; v <= MAX_N; v++) {
                dist[u][v] = INF;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        String[] tokens;

        tokens = br.readLine().split(" ");

        final int N = Integer.parseInt(tokens[0]);
        final int M = Integer.parseInt(tokens[1]);
        final int T = Integer.parseInt(tokens[2]);

        for (int i = 0; i < M; i++) {
            tokens = br.readLine().split(" ");
            int u = Integer.parseInt(tokens[0]);
            int v = Integer.parseInt(tokens[1]);
            int h = Integer.parseInt(tokens[2]);
            dist[u][v] = h;
        }

        // Floyd-Warshall
        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    if (dist[i][j] > Math.max(dist[i][k], dist[k][j])) {
                        dist[i][j] = Math.max(dist[i][k], dist[k][j]);
                    }
                }
            }
        }

        for (int i = 0; i < T; i++) {
            tokens = br.readLine().split(" ");
            int s = Integer.parseInt(tokens[0]);
            int e = Integer.parseInt(tokens[1]);
            int minDist = (dist[s][e] < INF) ? dist[s][e] : -1;
            System.out.println(minDist);
        }
    }
}
