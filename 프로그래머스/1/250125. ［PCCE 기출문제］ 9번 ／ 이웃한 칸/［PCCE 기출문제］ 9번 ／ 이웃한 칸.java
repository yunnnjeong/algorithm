class Solution {
    public int solution(String[][] board, int h, int w) {
        int n = board.length;
        int answer = 0;
        
        int[] dh = {0, 1, -1, 0};
        int[] dw = {1, 0, 0, -1};
        
        for(int i = 0; i < 4; i++) {
            int height = h + dh[i];
            int width = w + dw[i];
            
            if(height >= 0 && height < n && width >= 0 && width < n) {
                if(board[h][w].equals(board[height][width])) {
                    answer++;
                }
            }
        }
        
        return answer;
    }
}