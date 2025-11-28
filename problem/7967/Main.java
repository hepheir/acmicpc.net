// 7967번: Balance

import java.io.*;
import java.util.*;


class Main{
    private static final int MAX_N = 10;
    private static final int[] a = new int[MAX_N];
    private static final boolean[] used = new boolean[MAX_N];
    private static int n;

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(solve());
    }

    private static int solve() {
        for (int i = 0; i < n; i++) {
            used[i] = false;
        }
        return solve(0, 0);
    }

    private static int solve(int left, int right) {
        int caseCount = 0;
        for (int i = 0; i < n; i++) {
            if (used[i]) {
                continue;
            }
            used[i] = true;
            if (left + a[i] <= right) {
                caseCount += solve(left + a[i], right);
            }
            caseCount += solve(left, right + a[i]);
            used[i] = false;
        }
        if (caseCount == 0) {
            // All weights have been used.
            return 1;
        }
        return caseCount;
    }
}
