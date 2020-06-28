
// センター採点
// import java.util.*;
// public class Main {
//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
//         int n = input.nextInt();
//         String s = input.next();
//         int[] abcd = new int[4];
//         int a = 0;
//         int b = 0;
//         int c = 0;
//         int d = 0;
//         for (int i = 0; i < s.length(); i++){
//             char tmp = s.charAt(i);
//             if (tmp == '1'){
//                 a += 1;
//             } else if (tmp == '2'){
//                 b += 1;
//             } else if (tmp == '3'){
//                 c += 1;
//             } else {
//                 d += 1;
//             }
//         }
//         int max = Math.max(Math.max(Math.max(a,b),c),d);
//         int min = Math.min(Math.min(Math.min(a,b),c),d);
//         System.out.printf("%d %d\n",max,min);
//     }
// }

// 帰ってきた器物破損！高橋君
// import java.util.*;
// public class Main {
//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
//         String x = input.next();
//         String s = input.next();
//         s = s.replaceAll(x,"");
//         System.out.println(s);
//     }
// }

