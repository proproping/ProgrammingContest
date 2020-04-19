import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++){
            A[i] = input.nextInt();
        }
        int counter = 0;
        int tmp = 0;
        boolean flag = false;
        for (int i = 0; i < N; i++){
            if (flag){
                if (A[i] == 1){
                    tmp += 1;
                } else {
                    flag = false;
                    counter = Math.max(counter,tmp);
                    tmp = 0;
                }
            } else if (A[i] == 1){
                flag = true;
                tmp += 1;
            }
        }
        counter = Math.max(counter,tmp);
        System.out.println(counter+1);
    }
}