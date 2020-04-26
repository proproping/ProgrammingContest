import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        int[] a = new int[m];
        int[][] b = new int[m][n];
        for (int i = 0; i < m; i++){
            a[i] = input.nextInt();
        }
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                b[i][j] = input.nextInt();
            }
        }
        int[] ans = new int[n];
        for (int i = 0; i < m; i++){
            int bonus = n;
            for (int j = 0; j < n; j++){
                if (a[i] == b[i][j]) {
                    ans[j] += 1;
                    bonus -= 1;
                }
            }
            ans[a[i]-1] += bonus;
        }
        for (int i = 0; i < n; i++){
            System.out.println(ans[i]);
        }
    }
}