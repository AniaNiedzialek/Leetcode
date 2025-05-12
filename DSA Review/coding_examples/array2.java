public class array2 {
    public static void main(String[] args) {
        // Create an instance of the square class
        square squareInstance = new square();

        

        // Display the square values
        System.out.println("Square values:");
        for (int value : squareInstance.squareNumbers) {
            System.out.println(value);
        }
    }

    public static class square {
        int[] squareNumbers = new int[10];

        // Constructor to initialize square numbers
        // public square() {
        //     for (int i = 0; i < squareNumbers.length; i++) {
        //         int square = (i + 1) * (i + 1);
        //         squareNumbers[i] = square;
        //     }
        // }
        
        // Way #2: Using a for loop to initialize square numbers
        public square() {
            for (int i = 0; i < squareNumbers.length; i++) {
                int square = (i + 1) * (i + 1);
                squareNumbers[i] = square;
            }
        }

       
    }
}

