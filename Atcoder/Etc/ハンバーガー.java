import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();
        int n = input.nextInt();
        int A = 0;
        int B = 0;
        int C = 0;
        if (a < n){
            A = n - a;
        }
        if (b < 2*n){
            B = 2*n - b;
        }
        if (c < 3*n){
            C = 3*n - c;
        }
        System.out.printf("%d %d %d\n",A,B,C);
    }
}