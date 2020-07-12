// // 173 a
// import java.util.*;
// public class Main {
//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
//         int n = input.nextInt();
//         System.out.println(n%1000);
//     }
// }

// // 173 b
// import java.util.*;
// public class Main {
//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
//         int ac = 0;
//         int wa = 0;
//         int tle = 0;
//         int re = 0;
//         int n = input.nextInt();
//         for (int i = 0; i < n; i++){
//             String s = input.next();
//             if(s.equals("AC")){
//                 ac += 1;
//             } else if (s.equals("WA")){
//                 wa += 1;
//             } else if (s.equals("TLE")){
//                 tle += 1;
//             } else {
//                 re += 1;
//             }
//         }
//         System.out.printf("AC x %d\nWA x %d\nTLE x %d\nRE x %d\n",ac,wa,tle,re);
//     }
// }

// // コード川柳
// import java.util.*;
// public class Main {
//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
//         String s = input.next();
//         String t = input.next();
//         String u = input.next();
//         if (s.length() == 5 && t.length() == 7 && u.length() == 5){
//             System.out.println("valid");
//         } else {
//             System.out.println("invalid");
//         }
//     }
// }