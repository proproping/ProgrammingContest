// 天下一プログラマーゲーム
import java.util.*;
public class Main {
    public static void main(String[] args) {
        int ans = 0;
        for (int i = 1; i < 101; i++){
            if (!(i%3 == 0 || i%5 == 0)){
                ans += i;
            }
        }
        System.out.println(ans);
    }
}