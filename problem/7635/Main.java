// 7635번: Hidden Code

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            int N = Integer.parseInt(br.readLine());
            if (N == 0)
                break;

            String[] P = new String[N];
            String[] C = new String[N];

            for (int i = 0; i < N; i++) {
                String[] input = br.readLine().split(" ");
                P[i] = input[0];
                C[i] = input[1];
            }

            Testcase tc = new Testcase(N, P, C);
            String answer = tc.solve();
            System.out.println(answer);
        }
    }

    private static class Testcase {
        Integer N;
        String[] P;
        String[] C;

        public Testcase(Integer N, String[] P, String[] C) {
            this.N = N;
            this.P = P;
            this.C = C;
        }

        public String solve() {
            StringBuilder key = new StringBuilder();
            if (!constructKey(key))
                return "Impossible";
            return key.toString();
        }

        private Boolean constructKey(StringBuilder key) {
            if (key.length() > 0 && validateKey(key))
                return true;
            for (int i = 0; i < 26; i++) {
                char candidateChar = (char) ('A' + i);
                key.append(candidateChar);
                if (validateKeyAt(key, key.length() - 1) && constructKey(key))
                    return true;
                key.deleteCharAt(key.length() - 1);
            }
            return false;
        }

        private Boolean validateKey(StringBuilder key) {
            int maxLength = 0;
            for (int i = 0; i < N; i++) {
                if (P[i].length() > maxLength)
                    maxLength = P[i].length();
            }
            for (int i = 0; i < maxLength; i++) {
                if (!validateKeyAt(key, i))
                    return false;
            }
            return true;
        }

        private Boolean validateKeyAt(StringBuilder key, Integer charIndex) {
            for (int i = 0; i < N; i++) {
                if (charIndex >= P[i].length())
                    continue;
                if (charIndex >= key.length()) {
                    if (C[i].charAt(charIndex) != ascii_add(P[i].charAt(charIndex),
                            C[i].charAt(charIndex - key.length())))
                        return false;
                } else {
                    if (C[i].charAt(charIndex) != ascii_add(P[i].charAt(charIndex), key.charAt(charIndex)))
                        return false;
                }
            }
            return true;
        }

        private char ascii_add(char c1, char c2) {
            return (char) ((c1 - 'A' + c2 - 'A') % ('Z' - 'A' + 1) + 'A');
        }
    }
}
