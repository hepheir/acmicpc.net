// 27598번: Beppa and SwerChat

import java.io.*;
import java.util.*;


class Main {
    private static final int MAX_N = 100000;
    private static final BufferedReader br;
    private static final int[] a;
    private static final int[] b;
    private static final int[] valueToIndex;

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
        a = new int[MAX_N];
        b = new int[MAX_N];
        valueToIndex = new int[MAX_N + 1];
    }

    public static void main(String[] args) throws IOException {
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            StringTokenizer st;
            int n = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                b[i] = Integer.parseInt(st.nextToken());
            }
            System.out.println(solve(n));
        }
    }

    private static int solve(int n) {
        for (int i = 0; i < n; i++) {
            valueToIndex[a[i]] = i;
        }
        // LIS (Longest Increasing Subsequence)로 치환
        int lisLength = 1;
        for (int i = n-2; i >= 0; i--) {
            if (valueToIndex[b[i]] < valueToIndex[b[i+1]]) {
                lisLength++;
            } else {
                break;
            }
        }
        return n - lisLength;
    }
}
