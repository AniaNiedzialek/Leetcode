package example6;

public class Main {
    public static void main(String[] args) {
        Array numbers = new Array(3);
        numbers.insert(1);
        numbers.insert(2);
        numbers.insert(3);
        numbers.insert(4); 
        numbers.insert(5);
        System.out.println(numbers.indexOf(1));
        System.out.println(numbers.indexOf(10));
        numbers.print();
    }
}
