class Solution {
    public String[] solution(String[] expressions) {
        int min = 2;
        for (String exp : expressions) {
            for (char c : exp.toCharArray()) {
                if (c >= '0' && c <= '9') {
                    min = Math.max(min, c - '0' + 1);
                }
            }
        }
        
        boolean[] possible = new boolean[10];
        for (int i = min; i <= 9; i++) {
            possible[i] = true;
        }
        
        for (String exp : expressions) {
            if (exp.contains("X")) continue;
            
            String[] parts = exp.split(" ");
            int a = Integer.parseInt(parts[0]);
            String op = parts[1];
            int b = Integer.parseInt(parts[2]);
            int c = Integer.parseInt(parts[4]);
            
            for (int i = min; i <= 9; i++) {
                if (!possible[i]) continue;
                
                int aValue = toDecimal(a, i);
                int bValue = toDecimal(b, i);
                int cValue = toDecimal(c, i);
                
                int result = op.equals("+") ? aValue + bValue : aValue - bValue;
                
                if (result != cValue) {
                    possible[i] = false;
                }
            }
        }
        
        int answerCount = 0;
        for (String exp : expressions) {
            if (exp.contains("X")) answerCount++;
        }
        
        String[] answer = new String[answerCount];
        int idx = 0;
        
        for (String exp : expressions) {
            if (!exp.contains("X")) continue;
            
            String[] parts = exp.split(" ");
            int a = Integer.parseInt(parts[0]);
            String op = parts[1];
            int b = Integer.parseInt(parts[2]);
            
            String resultStr = null;
            boolean same = true;
            
            for (int i = min; i <= 9; i++) {
                if (!possible[i]) continue;
                
                int aValue = toDecimal(a, i);
                int bValue = toDecimal(b, i);
                int result = op.equals("+") ? aValue + bValue : aValue - bValue;
                
                String currentResult = fromDecimal(result, i);
                
                if (resultStr == null) {
                    resultStr = currentResult;
                } else if (!resultStr.equals(currentResult)) {
                    same = false;
                    break;
                }
            }
            
            if (same && resultStr != null) {
                answer[idx] = parts[0] + " " + op + " " + parts[2] + " = " + resultStr;
            } else {
                answer[idx] = parts[0] + " " + op + " " + parts[2] + " = ?";
            }
            idx++;
        }
        
        return answer;
    }
    
    private int toDecimal(int num, int n) {
        int result = 0;
        int multiplier = 1;
        while (num > 0) {
            result += (num % 10) * multiplier;
            multiplier *= n;
            num /= 10;
        }
        return result;
    }
    
    private String fromDecimal(int num, int n) {
        if (num == 0) return "0";
        
        StringBuilder sb = new StringBuilder();
        while (num > 0) {
            sb.append(num % n);
            num /= n;
        }
        return sb.reverse().toString();
    }
}