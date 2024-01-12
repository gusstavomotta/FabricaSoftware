import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
       
        int n = sc.nextInt();

        for ( int i = 1; i < 11; i++){
            int resultado = i * n;
            System.out.println(String.format("%d x %d = %d", i,n,resultado));
        }
    }
}
