import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String s = input.next();
        String t = input.next();
        if (s.equals(t)){
            System.out.println("same");
        } else if (s.toUpperCase().equals(t.toUpperCase())){
            System.out.println("case-insensitive");
        } else {
            Sysstem.out.println("different");
        }
    }
}