import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String s = input.next();
        int n = input.nextInt();
        String[] rings = new String[n];
        for (int i = 0; i < n; i++){
            rings[i] = input.next();
        }
        int ans = 0;
        for(int i = 0; i < n; i++){
            String tmp = rings[i] + rings[i];
            String tmprp = tmp.replaceAll(s,"");
            if (tmp.length() != tmprp.length()){
                ans += 1;
            }
        }
        System.out.println(ans);
    }
}