// 24309번: РАВЕНСТВО


import java.io.*;


class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine());
        int x = (b-c)/a;
        System.out.println(x);
    }
}
