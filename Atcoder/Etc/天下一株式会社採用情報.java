import java.util.*;
public class Main {
    public static void main(String[] args) {
        long num = 42;
        while (num <= 130000000){
            num += num;
        }
        System.out.println(num);
    }
}

