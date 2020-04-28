import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        Counter<Integer> c = new Counter<>();
        for (int i = 0; i < n; i++){
            c.add(input.nextInt());
        }
        int ans = 0;
        for (Integer i : c.keySet()){
            ans = Math.max(ans,c.get(i));
        }
        System.out.println(ans);
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