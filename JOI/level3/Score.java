import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[][] score = new int[n][2];
        for (int i = 0; i < n; i++){
            score[i][0] = input.nextInt();
            score[i][1] = i + 1;
        }
        Arrays.sort(score, (a,b) -> Integer.compare(a[0],b[0]));
        int rnk = 1;
        int point = 0;
        int tmp = 1;
        for (int i = n-1; i > -1; i--){
            if (i == n-1){
                point = score[i][0];
                score[i][0] = rnk;
            } else {
                if (score[i][0] == point){
                    score[i][0] = rnk;
                    tmp++;
                } else {
                    point = score[i][0];
                    rnk += tmp;
                    tmp = 1;
                    score[i][0] = rnk;
                }
            }
        }
        Arrays.sort(score, (a,b) -> Integer.compare(a[1],b[1]));
        for (int i = 0; i < n; i++){
            System.out.println(score[i][0]);
        }
    }
}