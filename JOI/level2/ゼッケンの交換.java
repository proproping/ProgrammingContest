import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++){
            a[i] = input.nextInt();
        }
        for (int k = 1; k < m+1; k++){
            for (int i = 0; i < n-1; i++){
                if (a[i]%k > a[i+1]%k){
                    int tmp = a[i];
                    a[i] = a[i+1];
                    a[i+1] = tmp;
                }
            }
        }
        for (int i = 0; i < n; i++){
            System.out.println(a[i]);
        }
    }
}