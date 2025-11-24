// 23794번: 골뱅이 찍기 - 정사각형

import java.io.*;


class Main {
    private static final BufferedReader br;

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
    }
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int r = 0; r < N+2; r++) {
            if (r == 0 || r == N+1) {
                for (int c = 0; c < N+2; c++) {
                    sb.append("@");
                }
            }
            else {
                sb.append("@");
                for (int c = 0; c < N; c++) {
                    sb.append(" ");
                }
                sb.append("@");
            }
            sb.append("\n");
        }

        System.out.print(sb);
    }
}
