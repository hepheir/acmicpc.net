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

    private static int solveTestCase(final int count, final int[] height, final int[] pastHeight) {
        if (!validateShape(count, height, pastHeight) || !validateErode(count, height, pastHeight)) {
            return -1;
        }
        int answer = 0;
        for (int i = 0; i < count; i++) {
            answer = Math.max(answer, pastHeight[i] - height[i]);
        }
        return answer;
    }

    private static boolean validateShape(final int count, final int[] height, final int[] pastHeight) {
        // 등고저차가 유지되었거나 평평한지 검사.
        for (int i = 1; i < count; i++) {
            // 등락이 역전되면 불가능한 케이스이다.
            if (sign(pastHeight[i] - pastHeight[i - 1]) * sign(height[i] - height[i - 1]) == -1) {
                return false;
            }
        }
        return true;
    }

    private static boolean validateErode(final int count, final int[] height, final int[] pastHeight) {
        // 유지되었거나 깎여나간건지 검사.
        for (int i = 0; i < count; i++) {
            if (pastHeight[i] < height[i]) {
                return false;
            }
        }
        return true;
    }

    private static int sign(int x) {
        if (x == 0) {
            return 0;
        }
        return (x < 0) ? -1 : 1;
    }
}