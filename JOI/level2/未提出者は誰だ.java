import java.util.*;
import java.util.stream.*;
class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        boolean [] check = new boolean[30];
        for (int i = 0; i < 28; i++){
            int index = input.nextInt() - 1;
            check[index] = true;
        }
        for (int i = 0; i < 30; i++){
            if (!check[i]){
                System.out.println(i+1);
            }
        }
    }
}