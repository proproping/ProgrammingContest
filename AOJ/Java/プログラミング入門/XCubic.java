import java.util.*;
import java.util.stream.*;
class XCubic {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        int ans = (int)Math.pow(x,3);
        System.out.println(ans);
    }
}