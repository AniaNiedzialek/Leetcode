public class example2 {
    public void log(int[] numbers) {
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // we could use a for each loop
        // for (int number : numbers) {
        //     System.out.println(number);
        // }
        
    }
}
// size of the input matters
// O(n) - linear time
// the time it takes to run the function is directly proportional to the size of the input
// the more numbers you have, the longer it takes to run
// cost of the algorithm grows lineraly with the size of the input!