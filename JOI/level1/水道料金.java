import java.util.*;
import java.util.stream.*;
class Main {
    public static void main(String[] args) {
        int a,b,c,d,p;
        Scanner input = new Scanner(System.in);
        a = input.nextInt();
        b = input.nextInt();
        c = input.nextInt();
        d = input.nextInt();
        p = input.nextInt();
        int ans = Math.min(p*a,b+Math.max(0,p-c)*d);
        System.out.println(ans);
    }
}