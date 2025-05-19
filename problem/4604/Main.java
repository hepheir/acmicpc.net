import java.io.*;
import java.util.*;


class Main {
    public static void main(String[] args) throws IOException {
        Map<Integer, String> map = new HashMap<>();
        map.put(0, " ");
        for (Character c = 'A'; c <= 'Z'; c++) {
            map.put(c + 1 - 'A', c.toString());
        }
        map.put(27, "\'");
        map.put(28, ",");
        map.put(29, "-");
        map.put(30, ".");
        map.put(31, "?");


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String rawLine;
        String decodedLine = new String();
        int bit = 0;
        int bitLength = 0;
        int spaceCount = 0;

        while (true) {
            rawLine = br.readLine();
            if (rawLine.charAt(0) == '*') {
                if (bitLength != 0) {
                    while (++bitLength <= 5) {
                        bit <<= 1;
                    }
                    decodedLine += map.get(bit);
                    bit = 0;
                    bitLength = 0;
                }
                System.out.println(decodedLine);
                decodedLine = new String();
                continue;
            }
            if (rawLine.charAt(0) == '#') {
                break;
            }
            for (int i = 0; i < rawLine.length(); i++) {
                if (rawLine.charAt(i) == ' ') {
                    spaceCount += 1;
                    continue;
                }
                if (spaceCount != 0) {
                    bit = bit << 1 | (1 - (spaceCount % 2));
                    if (++bitLength == 5) {
                        decodedLine += map.get(bit);
                        bit = 0;
                        bitLength = 0;
                    }
                    spaceCount = 0;
                }
            }
        }
    }
}