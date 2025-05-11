import java.util.Arrays;

public class example5 {
    public static void main(String[] args) {
        int[] numbers = new int[3] ;
        System.out.println(numbers);

        // to see the content of the array class 
        numbers[0] = 1;
        numbers[1] = 2;
        numbers[2] = 3;
        System.out.println(Arrays.toString(numbers));
    }
    
}
