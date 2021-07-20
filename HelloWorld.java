package IntroProg;

import java.util.Scanner;

class HelloWorld {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter your password");

        String password = in.nextLine();
        String confirm = in.nextLine();
        if (password == confirm)
            System.out.println("Welcome aboard");
        
    }
}