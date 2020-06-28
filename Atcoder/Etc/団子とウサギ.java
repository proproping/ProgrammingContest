import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        long tmp = 0;
        for (int i = 1; i < n+1; i++){
            tmp += i * i;
        }
        System.out.println(tmp%m);
    }
}