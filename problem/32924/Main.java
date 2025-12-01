// 32924번: If I Could Turn Back Time

import java.io.*;
import java.util.*;

class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final int MAX_N = 100000;
    private static final int[] H = new int[MAX_N];
    private static final int[] P = new int[MAX_N];

    public static void main(String[] args) throws IOException {
        int nTestCases = Integer.parseInt(br.readLine());
        for (int testCaseNo = 0; testCaseNo < nTestCases; testCaseNo++) {
            int n = Integer.parseInt(br.readLine());
            StringTokenizer tokenizerForH = new StringTokenizer(br.readLine());
            StringTokenizer tokenizerForP = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                H[i] = Integer.parseInt(tokenizerForH.nextToken());
                P[i] = Integer.parseInt(tokenizerForP.nextToken());
            }
            System.out.println(solveTestCase(n, H, P));
        }
    }

    private static int solveTestCase(int n, int[] h, int[] p) {
        int answer = 0;
        while (!isEqual(n, h, p)) {
            int x = determineX(n, h, p);
            if (!validateX(n, h, p, x)) {
                return -1;
            }
            for (int i = 0; i < n; i++) {
                if (x <= p[i]) {
                    p[i]--;
                }
            }
            answer++;
        }
        return answer;
    }

    private static boolean isEqual(final int n, final int[] h, int[] p) {
        for (int i = 0; i < n; i++) {
            if (h[i] != p[i]) {
                return false;
            }
        }
        return true;
    }

    private static int determineX(final int n, final int[] h, int[] p) {
        // h가 p에 가까워지기 위한 가장 작은 x 찾기.
        int x = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (h[i] < p[i]) {
                x = Math.min(x, p[i]);
            }
        }
        return x;
    }

    private static boolean validateX(final int n, final int[] h, int[] p, final int x) {
        for (int i = 0; i < n; i++) {
            boolean willErode = x <= p[i];
            boolean shouldErode = h[i] < p[i];
            if (willErode != shouldErode) {
                return false;
            }
        }
        return true;
    }
}