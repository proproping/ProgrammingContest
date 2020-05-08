import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        char[][] weather = new char[n][m];
        for (int i = 0; i < n; i++){
            String tmp = input.next();
            for (int j = 0; j < m; j++){
                weather[i][j] = tmp.charAt(j);
            }
        }
        int[][] ans = new int[n][m];
        for (int i = 0; i < n; i++){
            int now = m+1;
            for (int j = 0; j < m; j++){
                if (weather[i][j] == 'c'){
                    now = j;
                    ans[i][j] = 0;
                } else {
                    ans[i][j] = Math.max(-1,j-now);
                }
            }
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (j == m-1){
                    System.out.println(ans[i][j]);
                } else {
                    System.out.print(ans[i][j] + " ");
                }
            }
        }
    }
}