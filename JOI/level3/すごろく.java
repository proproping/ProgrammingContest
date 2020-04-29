import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        int[] inst = new int[n];
        int[] dice = new int[m];
        for (int i = 0; i < n; i++){
            inst[i] = input.nextInt();
        }
        for (int i = 0; i < m; i++){
            dice[i] = input.nextInt();
        }
        int now = 0;
        int ans = 0;
        for (int i = 0; i < m; i++){
            ans += 1;
            now += dice[i];
            if (now >= n-1){
                break;
            }
            now = Math.min(Math.max(0,(now+inst[now])),n-1);
            if (now >= n-1){
                break;
            }
        }
        System.out.println(ans);
    }
}