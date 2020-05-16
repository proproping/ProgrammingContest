import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] ranking = new int[n];
        int[] point = new int[n];
        for (int i = 0; i < (n*(n-1)/2); i++){
            int a = input.nextInt();
            int b = input.nextInt();
            int c = input.nextInt();
            int d = input.nextInt();
            if (c > d){
                point[a-1] += 3;
            } else if (c < d){
                point[b-1] += 3;
            } else {
                point[a-1] += 1;
                point[b-1] += 1;
            }
        }
        for (int i = 0; i < n; i++){
            int tmp = 1;
            for (int j = 0; j < n; j++){
                if (point[i] < point[j]){
                    tmp += 1;
                }
            }
            ranking[i] = tmp;
        }
        for (int i = 0; i < n; i++){
            System.out.println(ranking[i]);
        }
    }
}