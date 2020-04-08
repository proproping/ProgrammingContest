import java.util.*;
import java.util.stream.*;
class 鉛筆 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double N,A,B,C,D;
        N = input.nextDouble();
        A = input.nextDouble();
        B = input.nextDouble();
        C = input.nextDouble();
        D = input.nextDouble();
        double setA,setB;
        setA = Math.ceil(N/A);
        setB = Math.ceil(N/C);
        int ans;
        ans = (int)Math.min(setA*B,setB*D);
        System.out.println(ans);
    }
}