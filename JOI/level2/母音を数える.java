import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        String S = input.next();
        int ans = 0;
        for (int i = 0; i < S.length(); i++){
            char c = S.charAt(i);
            if (c == 'a' || c == 'i' || c == 'u' || c == 'e' || c == 'o'){
                ans += 1;
            }
        }
        System.out.println(ans);
    }
}