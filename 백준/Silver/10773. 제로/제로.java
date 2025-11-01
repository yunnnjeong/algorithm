import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int k = sc.nextInt();
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int i = 0; i < k; i++) {
            int n = sc.nextInt();
            if (n == 0) {
                list.remove(list.size() - 1);
            } else {
                list.add(n);
            }
        }
        
        int sum = 0;
        for (int num : list) {
            sum += num;
        }
        
        System.out.println(sum);
        sc.close();
    }
}