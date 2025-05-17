import java.io.*;
import java.util.*;


class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer[]> scores = new PriorityQueue<>(new Comparator<>() {
            @Override
            public int compare(Integer[] o1, Integer[] o2) {
                if (o1[1] < o2[1]) return 1;
                if (o1[1] > o2[1]) return -1;
                if (o1[0] < o2[0]) return 1;
                if (o1[0] > o2[0]) return -1;
                return 0;
            }
        });
        List<Integer> problems = new ArrayList<>();
        for (int i = 0; i < 8; i++) {
            Integer[] node = new Integer[2];
            node[0] = i+1;
            node[1] = Integer.parseInt(br.readLine());
            scores.add(node);
        }

        Integer score = 0;
        for (int i = 0; i < 5; i++) {
            Integer[] node = scores.remove();
            problems.add(node[0]);
            score += node[1];
        }
        problems.sort(null);
        System.out.println(score);
        for (Integer problem : problems) {
            System.out.printf("%d ", problem);
        }
        System.out.println();
    }
}
