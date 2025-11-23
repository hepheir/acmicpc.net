// 26090번: 완전한 수열

import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    private static final int MAX_N = 500;
    private static final int MAX_A_VALUE = 2000;
    private static final BufferedReader br;
    private static final boolean[] isPrime;

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
        isPrime = new boolean[MAX_A_VALUE * MAX_N + 1];
        initIsPrime();
    }

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        List<Integer> a = Arrays.stream(br.readLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        List<Integer> prefixSum = getPrefixSum(a);
        int answer = 0;
        for (int length = 1; length < N; length++) {
            if (!isPrime[length]) {
                continue;
            }
            for (int offset = 0; offset + length - 1 < N; offset++) {
                if (isPrime[getRangeSum(prefixSum, offset, offset + length - 1)]) {
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }

    private static void initIsPrime() {
        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i < isPrime.length; i++) {
            isPrime[i] = true;
        }
        for (int i = 2; i * i < isPrime.length; i++) {
            if (!isPrime[i])
                continue;
            for (int j = i * i; j < isPrime.length; j += i) {
                isPrime[j] = false;
            }
        }
    }

    private static Integer getRangeSum(List<Integer> prefixSum, int s, int e) {
        if (s == 0) {
            return prefixSum.get(e);
        }
        return prefixSum.get(e) - prefixSum.get(s - 1);
    }

    private static List<Integer> getPrefixSum(List<Integer> a) {
        List<Integer> prefixSum = new ArrayList<>();
        int sum = 0;
        for (int i = 0; i < a.size(); i++) {
            sum += a.get(i);
            prefixSum.add(sum);
        }
        return prefixSum;
    }
}
