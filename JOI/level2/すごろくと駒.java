import java.util.*;
public class Main {
    public static void main(String[] args) {
        boolean[] map = new boolean[2019];
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] x = new int[n];
        for (int i = 0; i < n; i++){
            x[i] = input.nextInt();
            map[x[i]-1] = true;
        }
        int m = input.nextInt();
        int[] a = new int[m];
        for (int i = 0; i < m; i++){
            a[i] = input.nextInt();
        }
        for (int i = 0; i < m; i++){
            int ai = a[i]-1;
            if (x[ai] == 2019){
                continue;
            } else if (map[x[ai]]){
                continue;
            } else {
                map[x[ai]-1] = false;
                map[x[ai]] = true;
                x[ai] += 1;
            }
        }
        for (int i : x){
            System.out.println(i);
        }
    }
}