import java.nio.file.Files;
import java.nio.file.Paths;

public class Part1 {
    public static int pow(int a, int power) {
        int result = 1;
        for (int i = 0; i < power; i++) {
            result *= a;
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        String input = Files.readString(Paths.get("input"));
        String[] lines = input.split("\n");

        System.out.println("Line count: " + lines.length);

        int n = 2;
        int sum = 0;
        for (int i = 0; i < lines.length; i++) {
            String[] jolts = lines[i].split("");
            int[] nums = new int[n];
            int[] indexes = new int[n];
            for (int j = 0; j < n; j++) {

                int startIndex = 0;
                if (j > 0) {
                    startIndex = indexes[j - 1] + 1;
                }

                for (int k = startIndex; k < jolts.length - (n - j - 1); k++) {
                    int jolt = Integer.parseInt(jolts[k]);

                    if (jolt > nums[j]) {
                        nums[j] = jolt;
                        indexes[j] = k; 
                    }
                }
            }

            int num = 0;
            for (int j = 0; j < nums.length; j++) {
                num += nums[j] * pow(10, (nums.length - j - 1));
            }

            System.out.println(num);
            sum += num;
        }

        System.out.println("Sum: " + sum);
    }
}