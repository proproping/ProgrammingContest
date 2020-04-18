import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int X = input.nextInt();
        int L = input.nextInt();
        int R = input.nextInt();
        int[] ans = {L,Math.abs(X-L)};
        for (int i = L+1; i < R+1; i++){
            if (ans[1] > Math.abs(X-i)){
                ans[0] = i;
                ans[1] = Math.abs(X-i);
            }
        }
        System.out.println(ans[0]);
    }
}