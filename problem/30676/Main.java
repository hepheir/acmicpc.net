// 30676번: 이 별은 무슨 색일까

import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int lambda = Integer.parseInt(br.readLine());
        String color = getColor(lambda);
        System.out.println(color);
    }

    public static String getColor(int lambda) {
        if (lambda >= 620 && lambda <= 780) {
            return "Red";
        }
        if (lambda >= 590 && lambda < 620) {
            return "Orange";
        }
        if (lambda >= 570 && lambda < 590) {
            return "Yellow";
        }
        if (lambda >= 495 && lambda < 570) {
            return "Green";
        }
        if (lambda >= 450 && lambda < 495) {
            return "Blue";
        }
        if (lambda >= 425 && lambda < 450) {
            return "Indigo";
        }
        if (lambda >= 380 && lambda < 425) {
            return "Violet";
        }
        throw new IllegalArgumentException("lambda가 범위를 벗어남.");
    }
}
