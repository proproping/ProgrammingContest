import java.util.*;
import java.util.stream.*;
class Main {
    public static void main(String[] args) {
        int a,b,c,d,e;
        Scanner input = new Scanner(System.in);
        a = input.nextInt();
        b = input.nextInt();
        c = input.nextInt();
        d = input.nextInt();
        e = input.nextInt();
        int ans;
        if (a*b < 0){
            ans = (0-a)*c + d + (b-0)*e;
        } else if (a*b > 0){
            ans = (b-a)*e;
        } else if (a < 0 || b < 0){
            ans = Math.abs(a-b)*c;
        } else {
            ans = Math.abs(a-b)*e;
        }
        System.out.println(ans);
    }
}