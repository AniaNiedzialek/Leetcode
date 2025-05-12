package coding_examples;
import java.util.Scanner;
import java.util.Arrays;

public class Solution3 {
    public int[] sortedSquares(int[] nums) {
        int size = nums.length; 
        int[] dummy = new int[size];

        for (int i = 0; i < size; i++) {
            dummy[i] = nums[i] * nums[i];
        }
        Arrays.sort(dummy);
        return dummy;     
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int size = scanner.nextInt();

        int[] nums = new int[size];
        System.out.println("Enter the elements of the array separated by space:");
        for (int i = 0; i < size; i++) {
            nums[i] = scanner.nextInt();
        }
        
        Solution3 solution = new Solution3();
        int[] result = solution.sortedSquares(nums);
        System.out.println("The sorted array of squares: " + Arrays.toString(result)); // Use Arrays.toString()
        scanner.close();
    }
}
