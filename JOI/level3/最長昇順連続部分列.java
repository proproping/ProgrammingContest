import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++){
            a[i] = input.nextInt();
        }
        int ans = 0;
        int tmp = 0;
        int before = 0;
        for (int i = 0; i < n; i++){
            if (before <= a[i]){
                tmp += 1;
            } else {
                ans = Math.max(ans,tmp);
                tmp = 1;
            }
            before = a[i];
            if (i == n-1){
                ans = Math.max(ans,tmp);
            }
        }
        System.out.println(ans);
    }
}