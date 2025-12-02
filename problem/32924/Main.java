// 32924번: If I Could Turn Back Time

import java.io.*;
import java.util.*;

class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final int MAX_N = 100000;
    private static final int[] H = new int[MAX_N];
    private static final int[] P = new int[MAX_N];
    private static final Integer[] INDEX = new Integer[MAX_N];
    private static final Comparator<Integer> comparator = new Comparator<>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            if (H[o1] < H[o2]) {
                return -1;
            }
            if (H[o1] > H[o2]) {
                return 1;
            }
            if (P[o1] < P[o2]) {
                return -1;
            }
            if (P[o1] > P[o2]) {
                return 1;
            }
            return 0;
        }
    };

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
            System.out.println(solveTestCase(n));
        }
    }

    private static int solveTestCase(final int count) {
        int answer = 0;
        for (int i = 0; i < count; i++) {
            INDEX[i] = i;
        }
        Arrays.sort(INDEX, 0, count, comparator);
        for (int i = 0; i < count; i++) {
            if (i > 0 && P[INDEX[i-1]] > P[INDEX[i]]) {
                return -1;
            }
            answer = Math.max(answer, P[INDEX[i]] - H[INDEX[i]]);
        }
        return answer;
    }
}