// 配点
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();
        int s = input.nextInt();
        int tmp = a + b + c - s;
        if (-3 <= tmp && tmp <= 0){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}