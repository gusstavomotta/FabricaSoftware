
package fs.pkg10_1;

import java.util.Scanner;

/**
 *
 * @author supti
 */
public class FS10_1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Informe a temperatura em ºC: ");
        Scanner sc = new Scanner(System.in);
        float tempC = sc.nextFloat();
        
        ConversorTemperatura conv = new ConversorTemperatura(tempC);
        System.out.println("Para qual unidade você quer converter?");
        System.out.println("0: Célcius");
        System.out.println("1: Fahrenheit");
        System.out.println("2: Kelvin");
        //String escolha = sc.next();
        //float resultado = conv.converter(escolha);
        
        int opcao = sc.nextInt();
        float resultado = conv.converter(Escala.values()[opcao]);
        System.out.printf("O resultado é: %.2f\n", resultado);
    }
    
}
