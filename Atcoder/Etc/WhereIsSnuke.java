import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int h = input.nextInt();
        int w = input.nextInt();
        String[][] map = new String[h][w];
        for (int i = 0; i < h; i++){
            for (int j = 0; j < w; j++){
                map[i][j] = input.next();
            }
        }
        int height = 1;
        char width = 'A';
        for (int i = 0; i < h; i++){
            for (int j = 0; j < w; j++){
                if (map[i][j].equals("snuke")){
                    width = (char)(((int)'A')+j);
                    height += i;
                }
            }
        }
        System.out.printf("%s%d\n",width,height);
    }
}


// import java.util.*;
// public class Main {
//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
//         String s = input.next();
//         int ans = 0;
//         String codefestival2016 = "CODEFESTIVAL2016";
//         for (int i = 0; i < s.length(); i++){
//             if (s.charAt(i) != codefestival2016.charAt(i)){
//                 ans += 1;
//             }
//         }
//         System.out.println(ans);
//     }
// }