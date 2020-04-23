import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        int[] a = new int[m];
        int[][] b = new int[n][m];
        for (int i = 0; i < m; i++){
            a[i] = input.nextInt();
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                b[i][j] = input.nextInt();
            }
        }
    }
}