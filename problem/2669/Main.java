import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] boxes = new int[4][4];
        for (int i = 0; i < 4; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                boxes[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int ans = solve(boxes);
        System.out.println(ans);
    }

    private static int solve(int[][] boxes) {
        int[] entireBox = new int[4];
        entireBox[0] = 0;
        entireBox[1] = 0;
        entireBox[2] = 100;
        entireBox[3] = 100;
        return solveUtil(boxes, 0, entireBox, 0);
    }

    private static int solveUtil(int[][] boxes, int i, int[] box, int depth) {
        int area = 0;
        int[] innerBox;
        while (i < boxes.length) {
            if (hasIntersection(box, boxes[i])) {
                innerBox = getIntersection(box, boxes[i]);
                if (depth % 2 == 0) {
                    area += calculateArea(innerBox);
                }
                else {
                    area -= calculateArea(innerBox);
                }
                area += solveUtil(boxes, i + 1, innerBox, depth + 1);
            }
            i++;
        }
        return area;
    }

    private static boolean hasIntersection(int[] box1, int[] box2) {
        return !((box1[2] < box2[0]) || (box2[2] < box1[0]) || (box1[3] < box2[1]) || (box2[3] < box1[1]));
    }

    private static int[] getIntersection(int[] box1, int[] box2) {
        int[] boxInner = new int[4];
        boxInner[0] = Math.max(box1[0], box2[0]);
        boxInner[1] = Math.max(box1[1], box2[1]);
        boxInner[2] = Math.min(box1[2], box2[2]);
        boxInner[3] = Math.min(box1[3], box2[3]);
        return boxInner;
    }

    private static int calculateArea(int[] box) {
        return Math.abs(box[0] - box[2]) * Math.abs(box[1] - box[3]);
    }
}