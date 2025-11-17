// 26574번: Copier


import java.io.*;


class Main {
    private static final BufferedReader br;

    static {
        br = new BufferedReader(new InputStreamReader(System.in));
    }
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            int x = Integer.parseInt(br.readLine());
            System.out.printf("%d %d\n", x, x);
        }
    }
}
