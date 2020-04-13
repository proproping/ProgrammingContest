import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[] W = new int[10];
        int[] K = new int[10];
        for (int i = 0; i < 20; i++){
            if (i < 10){
                W[i] = input.nextInt();
            } else {
                K[i-10] = input.nextInt();
            }
        }
        Arrays.sort(W);
        Arrays.sort(K);
        int w = W[7] + W[8] + W[9];
        int k = K[7] + K[8] + K[9];
        System.out.printf("%d %d\n",w,k);
    }
}