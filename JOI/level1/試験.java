import java.util.*;
import java.util.stream.*;
class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[] points = new int[3];
        for (int i = 0; i < 3; i++){
            points[i] = input.nextInt();
        }
        Arrays.sort(points);
        System.out.println(points[1]+points[2]);
    }
}