import java.util.*;
import java.util.stream.*;
class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String S = input.next();
        for (int i = 0; i < S.length(); i++){
            char c = S.charAt(i);
            if ((int)c < 68){
                c += 26;
            }
            c -= 3;
            System.out.printf("%s",c);
        }
        System.out.println();
    }
}