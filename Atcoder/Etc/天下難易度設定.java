import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int ans = 0;
        for (int i = 0; i < n; i++){
            int tmp = 0;
            for (int j = 0; j < 5; j++){
                tmp += input.nextInt();
            }
            if (tmp < 20){
                ans += 1;
            }
        }
        System.out.println(ans);
    }
}