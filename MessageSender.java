import java.util.Scanner;

public class MessageSender {

    public static void main(String[] args) {
        // Create a Scanner object to read input from the console
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter their message
        System.out.print("Enter your message: ");
        String message = scanner.nextLine();

        // Send the message
        sendMessage(message);

        // Close the scanner
        scanner.close();
    }

    /**
     * Sends the message by printing it to the console.
     *
     * @param message The message to be sent.
     */
    public static void sendMessage(String message) {
        // Print the message to the console
        System.out.println("Message sent: " + message);
    }
}
