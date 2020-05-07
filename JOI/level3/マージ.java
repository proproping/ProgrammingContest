import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        int[] ans = new int[n+m];
        for (int i = 0; i < (n+m); i++){
            ans[i] = input.nextInt();
        }
        Arrays.sort(ans);
        for (int i = 0; i < (n+m); i++){
            System.out.println(ans[i]);
        }
    }
}