// Leetcode Array prctice codes for Java
// This is a simple example of how to create an array of DVD objects in Java

public class DVDExample {

    public static void main(String[] args) {
        // creating an array that will store DVDs
        DVD[] dvdCollection = new DVD[15];

        // Adding a DVD to the collection
        dvdCollection[0] = new DVD("Inception", 2010, "Christopher Nolan");
        DVD avengersDVD = new DVD("The Avengers", 2012, "Joss Whedon");
        dvdCollection[7] = avengersDVD;
        DVD incrediblesDVD = new DVD("The Incredibles", 2004, "Brad Bird");
        DVD findingDoryDVD = new DVD("Finding Dory", 2016, "Andrew Stanton");
        DVD lionKingDVD = new DVD("The Lion King", 1994, "Roger Allers");
        DVD starWarsDVD = new DVD("Star Wars", 1977, "George Lucas");

        // put "The Incredibles" in the 4th place
        dvdCollection[3] = incrediblesDVD;
        // put "Finding Dory" in the 10th place
        dvdCollection[9] = findingDoryDVD;
        // put "The Lion King" in the 3rd place
        dvdCollection[2] = lionKingDVD;

        // testing
        dvdCollection[2] = starWarsDVD;




        // // Printing the added DVD
        // System.out.println("================");
        // System.out.println(dvdCollection[0]);
        // System.out.println(dvdCollection[7]);
        // System.out.println(dvdCollection[3]);
        // System.out.println(dvdCollection[9]);
        // System.out.println(dvdCollection[2]);
        // System.out.println("================");
        
        // Printing the entire collection
        System.out.println("===============");
        for (int i = 0; i < dvdCollection.length; i++) {
            if (dvdCollection[i] != null) {
                System.out.println("Index " + i + ": " + dvdCollection[i]);
            } else {
                System.out.println("Index " + i + ": Empty");
            }
        }
        System.out.println("===============");
    }


    // simple definition of the DVD class
    public static class DVD {
        public String name;
        public int releaseYear;
        public String director;

        public DVD(String name, int releaseYear, String director) {
            this.name = name;
            this.releaseYear = releaseYear;
            this.director = director;
        }

        public String toString() {
            return this.name + ", directed by " + this.director + ", released in " + this.releaseYear;
        }
    }
}