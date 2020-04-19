import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        int M = input.nextInt();
        int[][] AB = new int[M][2];
        for (int i = 0; i < M; i++){
            AB[i][0] = input.nextInt();
            AB[i][1] = input.nextInt();
        }
        Arrays.sort(AB, (a,b) -> Integer.compare(b[0],a[0]));
        int ans = 0;
        int hit = 0;
        for (int i = 0; i < M; i++){
            if (hit >= M-1){
                break;
            }
            if (AB[i][0] < N) {
                ans += (N - AB[i][0]);
            }
            hit += 1;
        }
        System.out.println(ans);
    }
}