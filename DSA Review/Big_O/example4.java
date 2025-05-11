

public class example4 {
    public void log(String[] names) {

        for (int i = 0; i < names.length; i++) {
            System.out.println("Hi" + names[i]);
        }
    }
}

// since we have a loop variable that is independent of the size of the input, the method
// will only allocate a constant amount of time
// O(1) - space complexity
// the space complexity is O(1) because we are not using any extra space

// now, if we had a specifically defined length of the array, we would have to use that length
// for example:
// public class example4 {
//     public void log(String[] names) {
//         String[] copy = new String[names.length];
//         for (int i = 0; i < names.length; i++) {
//             System.out.println("Hi" + names[i]);
//         }
// now space complexity is O(n)
//         // we are using an array of size n, so the space complexity is O(n)