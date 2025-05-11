import java.util.LinkedList;

public class example7 {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<>();
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);  
        list.addLast(4);
        list.removeFirst();
        list.addLast(30);
        list.indexOf(2);      
    }  
}
