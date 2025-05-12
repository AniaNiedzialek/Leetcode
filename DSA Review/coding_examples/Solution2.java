package coding_examples;
import java.util.Scanner;

class Solution2 {
    public int findNumbers(int[] nums) {
        int size = nums.length; 
        int even = 0;

        for (int i = 0; i < size; i++) {
            String str = Integer.toString(nums[i]);
            int sizeString = str.length();
            if (sizeString % 2 == 0) {
                even++;
            }
        }
        return even;       
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int size = scanner.nextInt();

        int[] nums = new int[size];
        System.out.println("Enter the elements of the array separated by space:");
        for (int i = 0; i < size; i++) {
            nums[i] = scanner.nextInt();
        }
        
        Solution2 solution = new Solution2();
        int result = solution.findNumbers(nums);
        System.out.println("The number of integers with an even number of digits is: " + result);      
        scanner.close();
    }
}
