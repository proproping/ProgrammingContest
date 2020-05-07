import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        int d = input.nextInt();
        char[][] map = new char[n][m];
        for (int i = 0; i < n; i++){
            String chars = input.next();
            for (int j = 0; j < m; j++){
                map[i][j] = chars.charAt(j);
            }
        }
        List<Integer> nums = new ArrayList<>();
        for (int i = 0; i < n; i++){
            int tmp = 0;
            for (int j = 0; j < m; j++){
                if (map[i][j] == '.'){
                    tmp += 1;
                } else {
                    nums.add(tmp);
                    tmp = 0;
                }
                if (j == m-1){
                    nums.add(tmp);
                    tmp = 0;
                }
            }
        }
        for (int i = 0; i < m; i++){
            int tmp = 0;
            for (int j = 0; j < n; j++){
                if (map[j][i] == '.'){
                    tmp += 1;
                } else {
                    nums.add(tmp);
                    tmp = 0;
                }
                if (j == n-1){
                    nums.add(tmp);
                    tmp = 0;
                }
            }
        }
        int ans = 0;
        for (int i : nums){
            ans += Math.max(0,i-d+1);
        }
        System.out.println(ans);
    }
}