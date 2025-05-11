package example6;
public class Array {
    private int[] items;
    private int count;

    public Array(int length) {
        items = new int[length];   
    }

    public void insert(int item) {
        // if the array is full, we need to resize it
        if (items.length == count) {
            // create a new array with double the size
            int[] newItems = new int[count * 2];
            // copy all the exisitng items to the new array
            for (int i = 0; i < count; i++) {
                newItems[i] = items[i];
            }
            // set the items to the new array
            items = newItems;
        }

        // add the new item at the end of the array
        items[count++] = item;
    }
    public int indexOf(int item) {
        for (int i = 0; i < count; i++) {
            if (items[i] == item) {
                return i;
            }
        }
        return -1;
    }
   
    public void removeAt(int index){
        // validate the index
        if (index < 0 || index >= count) {
            throw new IllegalArgumentException();
        }
        // shift the items to the left
        for (int i = index; i < count; i++) {
            items[i] = items[i + 1];
        }
        // decrement the count
        count--;
        // set the last item to 0
        items[count] = 0;
        // or we can set it to null if we are using an object array
        // items[count] = null;

    }
    public void print() {
        for (int i = 0; i < count; i++) {
            System.out.println(items[i]);
        }
    }
} 