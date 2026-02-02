// 32335 부자가 될 거야!

import java.io.*;

public class Main {
	static final int MAX_N = 200_000;
	static final int MAX_M = 1_000_000;

	static int N;
	static int M;
	static String S;

	static int[] digits = new int[MAX_N];

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		// I/O (Read)
		String[] tokens = br.readLine().split(" ");
		N = Integer.parseInt(tokens[0]);
		M = Integer.parseInt(tokens[1]);
		S = br.readLine();

		for (int i = 0; i < N; i++) {
			digits[i] = S.charAt(i) - '0';
		}

		// Greedy 하게 접근해보자.
		// 앞 자리 수가 작을 수록 작은 수임.
		// -> 큰 자릿 수부터 순차 조작으로 정답을 만들어 보자.
		int remainingMoveCount = M;

		for (int i = 0; i < N; i++) {
			if (remainingMoveCount >= (10 - digits[i]) && digits[i] > 0) {
				// 돌렸을 때, 이득이면 돌리자. (안 돌릴 수 있으면 돌리기 횟수 아끼기.)
				remainingMoveCount -= (10 - digits[i]);
				digits[i] = 0;
			}
		}

		// 이동 횟수가 남았다면 일단 한 바퀴 돌릴 수 있는 만큼 돌리기.
		// (10번씩 돌리면 제자리니까.)
		remainingMoveCount %= 10;

		// 그래도 남았다면 최대한 낮은 자릿 수를 돌려준다.
		digits[N-1] = (digits[N-1] + remainingMoveCount) % 10;

		// I/O (Write)
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < N; i++) {
			sb.append(digits[i]);
		}

		System.out.println(sb.toString());
	}
}
