import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int h = input.nextInt();
        int w = input.nextInt();
        int[][] a = new int[h][w];
        double ans = 1e9;
        for (int i = 0; i < h; i++){
            for (int j = 0; j < w; j++){
                a[i][j] = input.nextInt();
            }
        }
        for (int i = 0; i < h; i++){
            for (int j = 0; j < w; j++){
                int tmp = 0;
                for (int k = 0; k < h; k++){
                    for (int l = 0; l < w; l++){
                        tmp += Math.min(Math.abs(i-k),Math.abs(j-l))*a[k][l];
                    }
                }
                ans = Math.min(ans,tmp);
            }
        }
        System.out.println((int)ans);
    }
}