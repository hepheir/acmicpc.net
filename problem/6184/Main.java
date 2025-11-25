// 6184번: Cow Cars

import java.io.*;
import java.util.*;


class Main {
    private static final int MAX_N = 50000;
    private static final BufferedReader br;
    private static int N;
    private static int M;
    private static int D;
    private static int L;
    private static final int[] S = new int[MAX_N];
    private static final int[] K = new int[MAX_N];

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    public static void main(String[] args) throws IOException {
        String[] tokens = br.readLine().split(" ");
        N = Integer.parseInt(tokens[0]);
        M = Integer.parseInt(tokens[1]);
        D = Integer.parseInt(tokens[2]);
        L = Integer.parseInt(tokens[3]);

        for (int i = 0; i < N; i++) {
            S[i] = Integer.parseInt(br.readLine());
            K[i] = maxPreceeders(S[i]);
        }
        Arrays.sort(K, 0, N);

        int cowOnAllHighwaysCount = 0;
        for (int i = 0; i < N; i++) {
            int minCowOnAHighwayCount = cowOnAllHighwaysCount / M;
            if (K[i] < minCowOnAHighwayCount) {
                continue;
            }
            cowOnAllHighwaysCount++;
        }

        System.out.println(cowOnAllHighwaysCount);
    }

    private static int maxPreceeders(int initialSpeed) {
        // 소가 최대로 허용할 수 있는 자신의 앞 차 대수.
        int answer = N-1;
        while (maxSpeed(initialSpeed, answer) < L) {
            answer--;
        }
        return answer;
    }

    private static int maxSpeed(int initialSpeed, int numberOfPreceeders) {
        return Math.max(initialSpeed - D * numberOfPreceeders, 0);
    }
}
