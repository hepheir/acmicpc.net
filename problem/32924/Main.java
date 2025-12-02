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
            if (P[o1] < P[o2]) {
                return -1;
            }
            if (P[o1] > P[o2]) {
                return 1;
            }
            if (H[o1] < H[o2]) {
                return -1;
            }
            if (H[o1] > H[o2]) {
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

    private static int solveTestCase(final int n) {
        for (int i = 0; i < n; i++) {
            INDEX[i] = i;
        }
        // P가 작은 순, 같다면 H가 작은 순으로 정렬.
        Arrays.sort(INDEX, 0, n, comparator);
        int totalErosionCount = 0; // erode 된 횟수
        for (int i = 0; i < n; i++) {
            int requiredErosionCount = P[INDEX[i]] - H[INDEX[i]];
            if (requiredErosionCount < totalErosionCount) {
                return -1;
            }
            // 이번 건 내리면 안되는데, 다음 번 것이 동일 고도이지만 목표하는 고도가 다르면
            // 절대 불가능.
            if (i+1 < n && P[INDEX[i]] == P[INDEX[i+1]] && H[INDEX[i]] != H[INDEX[i + 1]]) {
                return -1;
            }
            totalErosionCount = Math.max(totalErosionCount, requiredErosionCount);
        }
        return totalErosionCount;
    }
}