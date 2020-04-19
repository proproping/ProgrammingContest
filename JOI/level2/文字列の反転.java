import java.util.*;
public class Main {
    public static void main(String[] args) {
        int N, A, B;
        String S;
        Scanner input = new Scanner(System.in);
        N = input.nextInt();
        A = input.nextInt();
        B = input.nextInt();
        S = input.next();
        StringBuffer str = new StringBuffer(S.substring(A-1,B));
        String revS = str.reverse().toString();
        String ans = S.substring(0,A-1) + revS + S.substring(B);
        System.out.println(ans);
    }
}