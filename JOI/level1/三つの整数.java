import java.util.*;
import java.util.stream.*;
class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int A,B,C;
        A = input.nextInt();
        B = input.nextInt();
        C = input.nextInt();
        Counter<Integer> c = new Counter<>();
        c.add(A);
        c.add(B);
        c.add(C);
        if (c.get(1) > c.get(2)){
            System.out.println(1);
        } else {
            System.out.println(2);
        }
    }
}
class Counter<T>{
    private Map<T,Integer> map = new HashMap<>();
    public void add(T key){
        int v = get(key);
        map.put(key, v + 1);
    }
    public int get(T key){
        return map.getOrDefault(key,0);
    }
    public Set<T> keySet(){
        return map.keySet();
    }
}