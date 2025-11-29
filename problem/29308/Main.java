// 29308번: Закат


import java.io.*;


class Main {
    public static final String RUSSIA = "Russia";
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int highestSalary = 0;
        String highestSalaryLastName = "";
        for (int i = 0; i < n; i++) {
            String[] tokens = br.readLine().split(" ");
            int salary = Integer.parseInt(tokens[0]);
            String lastName = tokens[1];
            String citizenship = tokens[2];
            if (citizenship.equals(RUSSIA) && salary > highestSalary) {
                highestSalary = salary;
                highestSalaryLastName = lastName;
            }
        }
        System.out.println(highestSalaryLastName);
    }
}
