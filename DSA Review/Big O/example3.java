public class example3 {
    public void log(int[] numbers) {
        System.out.println(numbers[0]);
        
        
        for (int first: numbers) {
            for (int second: numbers) {
                System.out.println(first + " " + second);
            }
        }
    }
}


// for nested loops, we have to multiply the two inputs
// O(n) * O(m) = O(n*m)
// if we have two inputs of the same size, we can drop the m and just use n
// O(n*n) = O(n^2)
// the time complexity is O(n^2)
// the more numbers you have, the longer it takes to run
// the cost of the algorithm grows quadratically with the size of the input

// if there was a different loop outside the nested loop, we would add the two time complexities together
// O(n) + O(n^2) = O(n^2)
// the larger time complexity dominates the smaller one
// if we have a nested loop with a constant amount of time, we can drop the constant


// if there was another loop outside the nested loop (such that we have 3 nested loops total), we would multiply the two time complexities together
// O(n) * O(n^2) = O(n^3)