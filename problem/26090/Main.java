// 26090번: 완전한 수열

import java.io.*;

class Main {
    private static final int MAX_N = 500;
    private static final int MAX_A_VALUE = 2000;
    private static final BufferedReader br;
    private static final boolean[] isPrime;
    private static final int[] sequence;
    private static final int[] prefixSum;

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
        isPrime = new boolean[MAX_A_VALUE * MAX_N + 1];
        sequence = new int[MAX_N];
        prefixSum = new int[MAX_N];
        initIsPrime(MAX_A_VALUE * MAX_N + 1);
    }

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        String[] rawA = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            sequence[i] = Integer.parseInt(rawA[i]);
        }
        initPrefixSum(N);
        int answer = 0;
        for (int s = 0; s < N; s++) {
            for (int e = s; e < N; e++) {
                if (isPerfectSequence(s, e)) {
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }

    private static Boolean isPerfectSequence(int s, int e) {
        int length = e - s + 1;
        int sum = getRangeSum(s, e);
        return isPrime[length] && isPrime[sum];
    }

    private static Integer getRangeSum(int s, int e) {
        if (s == 0) {
            return prefixSum[e];
        }
        return prefixSum[e] - prefixSum[s - 1];
    }

    private static void initIsPrime(int size) {
        for (int i = 0; i < 2 && i < size; i++) {
            isPrime[i] = false;
        }
        for (int i = 2; i < size; i++) {
            isPrime[i] = true;
        }
        for (int i = 2; i * i < size; i++) {
            if (!isPrime[i])
                continue;
            for (int j = i * i; j < size; j += i) {
                isPrime[j] = false;
            }
        }
    }

    private static void initPrefixSum(int size) {
        if (size > 0) {
            prefixSum[0] = sequence[0];
        }
        for (int i = 1; i < size; i++) {
            prefixSum[i] = prefixSum[i - 1] + sequence[i];
        }
    }
}
