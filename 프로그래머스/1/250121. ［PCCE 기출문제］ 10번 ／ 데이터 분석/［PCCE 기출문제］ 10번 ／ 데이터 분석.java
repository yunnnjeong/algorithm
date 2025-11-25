import java.util.*;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        int e = getIndex(ext);
        int s = getIndex(sort_by);
        
        List<int[]> list = new ArrayList<>();
        for (int[] row : data) {
            if (row[e] < val_ext) {
                list.add(row);
            }
        }
        
        list.sort((a, b) -> Integer.compare(a[s], b[s]));
        
        int[][] answer = new int[list.size()][];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
    
    private int getIndex(String col) {
        switch (col) {
            case "code": return 0;
            case "date": return 1;
            case "maximum": return 2;
            case "remain": return 3;
            default: return -1;
        }
    }
}