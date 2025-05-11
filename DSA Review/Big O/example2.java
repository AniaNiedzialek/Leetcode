public class example2 {
    public void log(int[] numbers) {
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // we could use a for each loop
        // for (int number : numbers) {
        //     System.out.println(number);
        // }
        // we could use a while loop or do while loop
        
    }
}
// size of the input matters
// O(n) - linear time
// the time it takes to run the function is directly proportional to the size of the input
// the more numbers you have, the longer it takes to run
// cost of the algorithm grows lineraly with the size of the input!

// with print statement that adds a constant amount of time
// O(n) + O(1) = O(n+1), the 1 does not really matter so it can be dropped
// therefore the time complexity is O(n)


// for loop with two/multiple inputs, we have to distinguish between the two inputs
// for example:
// public void log(int[] numbers1, int[] numbers2) {
//     for (int i = 0; i < numbers1.length; i++) {
//         System.out.println(numbers1[i]);
//     }
//     for (int j = 0; j < numbers2.length; j++) {
//         System.out.println(numbers2[j]);
//     }
// }
// O(n) + O(m) = O(n+m)
// which we can drop to O(n) if n is the largest input, and in this case the runtime is linear
