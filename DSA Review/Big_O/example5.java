import java.util.Arrays;

public class example5 {
    public static void main(String[] args) {
        int[] numbers = new int[3] ;
        System.out.println(numbers);

        // to see the content of the array class 
        numbers[0] = 1;
        numbers[1] = 10;
        numbers[2] = 3;

        // another way is to do the following:
        int[] numbers2 = {1, 2, 3};
        
        System.out.println("numbers1 :" + Arrays.toString(numbers));
        System.out.println("numbers2: " + Arrays.toString(numbers2));

        System.out.println(numbers.length);
    }
    
}
