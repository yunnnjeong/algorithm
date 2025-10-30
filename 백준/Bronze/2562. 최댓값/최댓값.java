import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int[] nums = new int[9];
        for (int i = 0; i < 9; i++) {
            nums[i] = sc.nextInt();
        }
        
        int mx = nums[0];
        int idx = 1;
        
        for (int i = 1; i < 9; i++) {
            if (nums[i] > mx) {
                mx = nums[i];
                idx = i + 1;
            }
        }
        
        System.out.println(mx);
        System.out.println(idx);
        
        sc.close();
    }
}