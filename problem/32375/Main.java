// 32375번: 불꽃놀이

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

class Main {
    public static final int MAX_N = 200000;
    public static final int MAX_K = 1000000000;
    public static final List<Integer> A = new ArrayList<>(MAX_N);

    private static final BufferedReader br;

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st;
        int N;
        int K;
        int answer;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        A.clear();
        for (int i = 0; i < N; i++) {
            A.add(Integer.valueOf(st.nextToken()));
        }

        answer = countMaxFireworks(A, K);
        if (answer == 0) {
            System.out.printf("-1\n");
            return;
        }
        System.out.printf("%d\n", answer);
    }

    private static int countMaxFireworks(List<Integer> levels, int requiredLevel) {
        List<Integer> combinableLevels = levels.stream()
                .filter(lv -> lv < requiredLevel)
                .sorted()
                .collect(Collectors.toList());
        int count = levels.size() - combinableLevels.size();
        int i = 0;
        int j = combinableLevels.size() - 1;
        while (i < j) {
            if (combinableLevels.get(i) + combinableLevels.get(j) >= requiredLevel) {
                count++;
                i++;
                j--;
                continue;
            }
            i++;
        }
        return count;
    }
}
