class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        
        int t = bandage[0];
        int x = bandage[1];
        int y = bandage[2];
        
        int hp = health;
        int success = 0;
        int idx = 0;
        
        int end = attacks[attacks.length - 1][0];
        
        for(int time = 1; time <= end; time++) {
            if(idx < attacks.length && attacks[idx][0] == time) {
                hp -= attacks[idx][1];
                success = 0;
                idx++;
                
                if(hp <= 0) {
                    return -1;
                }
            } else {
                hp += x;
                success++;
                
                if(success == t) {
                    hp += y;
                    success = 0;
                }
                
                if(hp > health) {
                    hp = health;
                }
            }
        }
        
        answer = hp;
        return answer;
    }
}