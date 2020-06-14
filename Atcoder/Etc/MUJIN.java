import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String c = input.next();
        if (c.equals("O") || c.equals("P") || c.equals("K") || c.equals("L")){
            System.out.println("Right");
        } else {
            System.out.println("Left");
        }
    }
}