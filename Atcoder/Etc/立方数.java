// 立方数
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        String ans = "NO";
        for (int i = 0; i < 101; i++){
            if (i*i*i == a){
                ans = "YES";
            }
        }
        System.out.println(ans);
    }
}
