import java.util.Arrays;

class Solution {
    public int solution(int[] m, String[][] park) {
        Arrays.sort(m);
        
        int h = park.length;
        int w = park[0].length;
        
        for (int i = m.length - 1; i >= 0; i--) {
            int size = m[i];
            
            for (int r = 0; r <= h - size; r++) {
                for (int c = 0; c <= w - size; c++) {
                    if (check(park, r, c, size)) {
                        return size;
                    }
                }
            }
        }
        
        return -1;
    }
    
    private boolean check(String[][] park, int row, int col, int size) {
        for (int r = row; r < row + size; r++) {
            for (int c = col; c < col + size; c++) {
                if (!park[r][c].equals("-1")) {
                    return false;
                }
            }
        }
        return true;
    }
}