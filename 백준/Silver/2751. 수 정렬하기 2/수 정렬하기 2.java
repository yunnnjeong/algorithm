import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        
        ArrayList<Integer> numbers = new ArrayList<>();
        
        for (int i = 0; i < N; i++) {
            numbers.add(Integer.parseInt(br.readLine()));
        }
        
        Collections.sort(numbers);
        
        StringBuilder sb = new StringBuilder();
        for (int num : numbers) {
            sb.append(num).append('\n');
        }
        
        System.out.print(sb);
        
        br.close();
    }
}