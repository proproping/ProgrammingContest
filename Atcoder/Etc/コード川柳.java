// コード川柳
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String s = input.next();
        String t = input.next();
        String u = input.next();
        if (s.length() == 5 && t.length() == 7 && u.length() == 5){
            System.out.println("valid");
        } else {
            System.out.println("invalid");
        }
    }
}