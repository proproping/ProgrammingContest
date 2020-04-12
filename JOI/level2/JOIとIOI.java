import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String S = input.next();
        int joi = 0;
        int ioi = 0;
        for (int i = 0; i < S.length()-2; i++){
            String tmp = S.substring(i,i+3);
            if (tmp.equals("JOI")){
                joi += 1;
            } else if (tmp.equals("IOI")){
                ioi += 1;
            }
        }
        System.out.printf("%d\n%d\n",joi,ioi);
    }
}
