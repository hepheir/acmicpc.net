// 26545번: Mathematics

import java.io.*;


class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int sum = 0;
        while (n-- > 0) {
            sum += Integer.parseInt(br.readLine());
        }
        System.out.println(sum);
    }
}
