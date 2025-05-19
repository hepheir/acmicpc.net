import java.io.*;
import java.util.*;

class Main {
    public static final int MAX_N = 20;
    private static int[][] grid = new int[MAX_N + 1][MAX_N + 1];

    private static class SeatScore implements Comparable<SeatScore> {
        public int favoriteStudentCount = 0;
        public int emptySeatCount = 0;
        public int r = 0;
        public int c = 0;

        @Override
        public int compareTo(SeatScore o) {
            if (favoriteStudentCount < o.favoriteStudentCount)
                return -1;
            if (favoriteStudentCount > o.favoriteStudentCount)
                return 1;
            if (emptySeatCount < o.emptySeatCount)
                return -1;
            if (emptySeatCount > o.emptySeatCount)
                return 1;
            if (r > o.r)
                return -1;
            if (r > o.r)
                return 1;
            return (c > o.c) ? -1 : 1;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int[][] students = new int[MAX_N * MAX_N][5];
        for (int i = 0; i < N * N; i++) {
            st = new StringTokenizer(br.readLine());
            students[i][0] = Integer.parseInt(st.nextToken());
            students[i][1] = Integer.parseInt(st.nextToken());
            students[i][2] = Integer.parseInt(st.nextToken());
            students[i][3] = Integer.parseInt(st.nextToken());
            students[i][4] = Integer.parseInt(st.nextToken());
        }
        int answer = solve(N, students);
        System.out.println(answer);
    }

    private static int solve(int N, int[][] students) {
        for (int i = 0; i < N * N; i++) {
            SeatScore maxSeatScore = getMaxSeatScore(N, students[i]);
            setStudentAtSeat(maxSeatScore.c, maxSeatScore.r, students[i][0]);
        }
        int satisfactionScore = 0;
        for (int i = 0; i < N * N; i++)
            satisfactionScore += getSatisfactionScore(N, students[i]);
        return satisfactionScore;
    }

    private static int getSatisfactionScore(int N, int[] student) {
        for (int x = 0; x < N; x++)
            for (int y = 0; y < N; y++)
                if (getStudentAtSeat(x, y) == student[0])
                    switch (calculateSeatScore(N, x, y, student).favoriteStudentCount) {
                        case 0:
                            return 0;
                        case 1:
                            return 1;
                        case 2:
                            return 10;
                        case 3:
                            return 100;
                        case 4:
                            return 1000;
                        default:
                            throw new AssertionError();
                    }
        throw new IllegalArgumentException();
    }

    private static SeatScore getMaxSeatScore(int N, int[] student) {
        List<SeatScore> scores = new ArrayList<>();
        for (int x = 0; x < N; x++)
            for (int y = 0; y < N; y++)
                if (isEmptySeat(x, y))
                    scores.add(calculateSeatScore(N, x, y, student));
        return scores.stream().max(SeatScore::compareTo).orElseThrow();
    }

    private static SeatScore calculateSeatScore(int N, int x, int y, int[] student) {
        SeatScore score = new SeatScore();
        score.c = x;
        score.r = y;
        if (0 <= x - 1)
            updateSeatScoreFor(score, x - 1, y, student);
        if (x + 1 < N)
            updateSeatScoreFor(score, x + 1, y, student);
        if (0 <= y - 1)
            updateSeatScoreFor(score, x, y - 1, student);
        if (y + 1 < N)
            updateSeatScoreFor(score, x, y + 1, student);
        return score;
    }

    private static void updateSeatScoreFor(SeatScore score, int x, int y, int[] student) {
        if (hasFavoriteStudent(x, y, student))
            score.favoriteStudentCount++;
        if (isEmptySeat(x, y))
            score.emptySeatCount++;
    }

    private static boolean hasFavoriteStudent(int x, int y, int[] student) {
        for (int i = 1; i < 5; i++)
            if (student[i] == grid[x][y])
                return true;
        return false;
    }

    private static boolean isEmptySeat(int x, int y) {
        return getStudentAtSeat(x, y) == 0;
    }

    private static int getStudentAtSeat(int x, int y) {
        return grid[x][y];
    }

    private static void setStudentAtSeat(int x, int y, int student) {
        grid[x][y] = student;
    }
}