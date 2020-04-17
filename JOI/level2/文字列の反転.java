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
        StringBuffer str = new StringBuffer(S);
        String revS = str.reverse().toString();
        System.out.println(S.substring(0,A-1)+revS.substring(A,B-1)+S.substring(B,S.length()));
    }
}