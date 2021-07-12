import java.util.Scanner;

class HelloWorld {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter your password");

        String password = in.nextLine();
        if (password == password)
            System.out.println("Welcome aboard");
        
    }
}