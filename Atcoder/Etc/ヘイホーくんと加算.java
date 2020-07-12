// ヘイホー君と加算
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double n = input.nextDouble();
        int ans = 0;
        while (true){
            if (Math.pow(Math.floor(Math.sqrt(n)),2) == n){
                break;
            }
            n += 1;
            ans += 1;
        }
        System.out.println(ans);
    }
}