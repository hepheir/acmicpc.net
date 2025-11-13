// 18409번: 母音を数える (Counting Vowels)

import java.io.*;

class Main {
    private static BufferedReader br;

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    public static void main(String[] args) throws IOException {
        int answer = 0;
        br.readLine();
        for (char c : br.readLine().toCharArray()) {
            if (c == 'a' || c == 'i' || c == 'u' || c == 'e' || c == 'o') {
                answer++;
            }
        }
        System.out.println(answer);
    }
}
