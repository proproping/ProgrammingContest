import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        String S = input.next();
        String ans = S.replaceAll("joi","JOI");
        System.out.println(ans);
    }
}