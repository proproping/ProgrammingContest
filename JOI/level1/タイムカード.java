import java.util.*;
import java.util.stream.*;
class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[][] info = new int[3][6];
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 6; j++){
                info[i][j] = input.nextInt();
            }
        }
        for (int i = 0; i < 3; i++){
            int h,m,s,sum;
            sum = (info[i][3] - info[i][0])*3600 + (info[i][4] - info[i][1])*60 + (info[i][5] - info[i][2]);
            s = sum%60;
            sum -= s;
            m = (sum/60)%60;
            h = sum/3600;
            System.out.printf("%d %d %d\n",h,m,s);
        }
    }
}