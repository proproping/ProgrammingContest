import java.util.*;
import java.util.stream.*;
class PrintARectangle {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int H,W;
        while(true){
            H = input.nextInt();
            W = input.nextInt();
            if (H == 0 && W == 0){
                break;
            } else {
                for (int i = 0; i < H; i++){
                    for (int j = 0; j < W; j++){
                        System.out.printf("#");
                    }
                    System.out.printf("\n");
                }
                System.out.printf("\n");
            }
        }
    }
}