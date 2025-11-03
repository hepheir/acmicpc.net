// 28691번: 정보보호학부 동아리 소개

import java.io.*;
import java.util.HashMap;


class Main {
    private static final HashMap<Character, String> map = new HashMap<>();

    static {
        map.put('M', "MatKor");
        map.put('W', "WiCys");
        map.put('C', "CyKor");
        map.put('A', "AlKor");
        map.put('$', "$clear");
    }

    public static void main(String[] args) throws IOException {
        Reader reader = new InputStreamReader(System.in);
        char[] buffer = new char[2];
        reader.read(buffer);

        System.out.print(map.get(((Character) buffer[0])));
    }
}
