import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        while (true){
            int n = input.nextInt();
            int k = input.nextInt();
            if (n == k && n == 0 && k == 0){
                break;
            }
            int[] tmp = new int[n];
            for (int i = 0; i < n; i++){
                tmp[i] = input.nextInt();
            }
            Arrays.sort(tmp);
            int ans = 0;
            for (int i = 0; i < k; i++){
                ans += tmp[i];
            }
            System.out.println(ans);
        }
    }
}