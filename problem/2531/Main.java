// 2531번: 회전 초밥

import java.io.*;
import java.util.*;


public class Main {
    static final int MAX_N = 30000;
    static final int MAX_D = 3000;
    static final int MAX_K = 3000;

    // 문제에서 제공되는 데이터
    static int N;
    static int d;
    static int k;
    static int c;
    static int[] belt;

    // 풀이를 위해 사용하는 데이터
    static int[] dishCount = new int[MAX_D+1]; // 초밥 종류 별 접시 수.
    static int uniqueDishCount = 0;
    static int maxUniqueDishCount = 0;
    static Queue<Integer> dishQueue = new ArrayDeque<>(MAX_K);

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        // I/O
        String[] tokens = br.readLine().split(" ");
        N = Integer.parseInt(tokens[0]);
        d = Integer.parseInt(tokens[1]);
        k = Integer.parseInt(tokens[2]);
        c = Integer.parseInt(tokens[3]);
        belt = new int[MAX_N];
        for (int i = 0; i < N; i++) {
            belt[i] = Integer.parseInt(br.readLine());
        }

        // 쿠폰으로 먹을 수 있는 초밥을 미리 세어둠.
        dishCount[c]++;
        uniqueDishCount++;

        // Queue 초기화
        for (int i = 0; i < k; i++) {
            int dishType = belt[i];
            if (dishCount[dishType] == 0)
                uniqueDishCount++;
            dishCount[dishType]++;
            dishQueue.offer(dishType);
        }

        // Queue를 rotate 하면서 최대 초밥 가짓수를 구하기.
        for (int i = k; i < k+N; i++) {
            int dishType;
            // 기존에 선택했던 접시를 제거
            dishType = dishQueue.poll();
            dishCount[dishType]--;
            if (dishCount[dishType] == 0)
                uniqueDishCount--;
            // 새로운 선택했던 접시를 추가
            dishType = belt[i % N];
            if (dishCount[dishType] == 0)
                uniqueDishCount++;
            dishCount[dishType]++;
            dishQueue.offer(dishType);
            // 최대 가짓 수 갱신
            maxUniqueDishCount = Math.max(maxUniqueDishCount, uniqueDishCount);
        }

        System.out.println(maxUniqueDishCount);
    }
}
