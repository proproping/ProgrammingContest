import java.util.*;
import java.util.stream.*;
class Dice1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[] num = new int[6];
        for (int i = 0; i < 6; i++){
            num[i] = input.nextInt();
        }
        Dice dice = new Dice(num);
        String S;
        S = input.next();
        for (int i = 0; i < S.length(); i++){
            char c = S.charAt(i);
            dice.roll(c);
        }
        dice.disp_top();
    }
}

class Dice {
    private int N,E,W,S,T,B;
    private int[] dice_num;
    Dice(int[] num_array){
        dice_num = num_array;
        T = dice_num[0];
        S = dice_num[1];
        E = dice_num[2];
        W = dice_num[3];
        N = dice_num[4];
        B = dice_num[5];
    }
    public void roll(char direction){
        int tmp;
        if (direction == 'N'){
            tmp = T;
            T = S;
            S = B;
            B = N;
            N = tmp;
        } else if (direction == 'E'){
            tmp = T;
            T = W;
            W = B;
            B = E;
            E = tmp;
        } else if (direction == 'W'){
            tmp = T;
            T = E;
            E = B;
            B = W;
            W = tmp;
        } else {
            tmp = T;
            T = N;
            N = B;
            B = S;
            S = tmp;
        }
    }
    public void disp_top(){
        System.out.println(T);
    }
}