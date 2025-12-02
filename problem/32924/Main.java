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

    private static int solveTestCase(final int n) {
        int answer = 0;
        for (int i = 0; i < n; i++) {
            INDEX[i] = i;
        }
        // H가 작은 순, 같다면 P가 작은 순으로 정렬.
        Arrays.sort(INDEX, 0, n, comparator);
        for (int i = 0; i < n; i++) {
            // 뭘 해도 p -> h를 못 만드는 경우
            if (P[INDEX[i]] < H[INDEX[i]]) {
                return -1;
            }
            // 정렬된 INDEX 기준, 먼저 조회할 p가 더 낮은 h로 가야하는데
            // 먼저 조회한 p가 직후의 p보다 높다면,
            // INDEX가 h에 대해 오름차순으로 정렬되어 있으므로,
            // 앞의 p를 내리면 뒤에 있는 p들도 내려와야 한다는 전제를 만족 못함.
            if ((i+1 < n) && (P[INDEX[i]] > P[INDEX[i+1]])) {
                return -1;
            }
            // p가 같으면 무조건 같이 erode 할 수 밖에 없는데, 목표해야할 h가 다른경우
            // -> 절대 도달 못함.
            if ((i+1 < n) && (P[INDEX[i]] == P[INDEX[i+1]]) && (H[INDEX[i]] != H[INDEX[i + 1]])) {
                return -1;
            }
            answer = Math.max(answer, P[INDEX[i]] - H[INDEX[i]]);
        }
        return answer;
    }
}