import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        int[] post = new int[n];
        int[] cost = new int[n];
        int[] level = new int[m];
        for (int i = 0; i < n; i++){
            cost[i] = input.nextInt();
        }
        for (int i = 0; i < m; i++){
            level[i] = input.nextInt();
        }
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (cost[j] <= level[i]){
                    post[j] += 1;
                    break;
                }
            }
        }
        int ans = 0;
        int howMuch = 0;
        for (int i = 0; i < n; i++){
            if (howMuch < post[i]){
                howMuch = post[i];
                ans = i+1;
            }
        }
        System.out.println(ans);
    }
}