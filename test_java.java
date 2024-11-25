public class ReadableExample {

    /**
     * Calculates the sum of all elements in an array of integers.
     *
     * @param numbers the array of integers
     * @return the sum of the elements
     */
    public int sumArray(int[] numbers) {
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        return sum;
    }

    /**
     * Shifts each character in a string by a given number of positions.
     *
     * @param input the input string
     * @param shift the number of positions to shift each character
     * @return the shifted string
     */
    public String shiftString(String input, int shift) {
        StringBuilder shiftedString = new StringBuilder();
        for (char character : input.toCharArray()) {
            char shiftedChar = (char) (character + shift);
            shiftedString.append(shiftedChar);
        }
        return shiftedString.toString();
    }

    public static void main(String[] args) {
        ReadableExample example = new ReadableExample();

        // Example usage of sumArray
        int[] numbers = {1, 2, 3, 4, 5};
        int sum = example.sumArray(numbers);
        System.out.println("Sum of array: " + sum);

        // Example usage of shiftString
        String originalString = "hello";
        int shiftAmount = 1;
        String shiftedString = example.shiftString(originalString, shiftAmount);
        System.out.println("Shifted string: " + shiftedString);
    }
}
