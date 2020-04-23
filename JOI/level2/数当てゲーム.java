import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        int ans[] = new int[N];
        int num[][] = new int[N][3];
        for (int i = 0; i < N; i++){
            for (int j = 0; j < 3; j++){
                num[i][j] = input.nextInt();
            }
        }
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < N; j++){
                boolean flag = true;
                for (int k = 0; k < N; k++){
                    if (j == k){
                        continue;
                    }
                    if (num[j][i] == num[k][i]){
                        flag = false;
                        break;
                    }
                }
                if (flag){
                    ans[j] += num[j][i];
                }
            }
        }
        for (int i = 0; i < N; i++){
            System.out.println(ans[i]);
        }
    }
}