package coding_examples;
import java.util.Scanner;

class Solution1 {
    public int findMaxConsecutiveOnes(int[] nums) {
        int size = nums.length;
        int maxCount = 0;
        int count = 0;

        for (int i = 0; i < size; i++) {
            if (nums[i] == 1){
                count++;
                if (count > maxCount) {
                    maxCount = count;
                }
            } else {
                count = 0;
            }
        }
        return maxCount;   
    }
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int size = scanner.nextInt();

        int[] nums = new int[size];
        System.out.println("Enter the elements of the array (0 or 1):");
        for (int i = 0; i < size; i++) {
            nums[i] = scanner.nextInt();
        }
        
        Solution1 solution = new Solution1();
        int result = solution.findMaxConsecutiveOnes(nums);
        System.out.println("The maximum number of consecutive 1's is: " + result);
        scanner.close();
    }
}
