import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int A = input.nextInt();
        int B = input.nextInt();
        int C = input.nextInt();
        long ans = 0;
        long counter = 0;
        for (int i = 1; i < Math.pow(10,6)+1; i++){
            if (counter >= C){
                break;
            }
            ans ++;
            counter += A;
            if (i%7 == 0){
                counter += B;
            }
        }
        System.out.println(ans);
    }
}