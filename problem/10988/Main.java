import java.io.*;


class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int i = 0;
        int j = s.length()-1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                System.out.println(0);
                return;
            }
            i++;
            j--;
        }
        System.out.println(1);
    }
}