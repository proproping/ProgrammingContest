import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String x = input.next();
        String s = input.next();
        s = s.replaceAll(x,"");
        System.out.println(s);
    }
}
