import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        Trator trator1;
        trator1 = new Trator("Massey");

        trator1.entradaDados();

        Scanner sc = new Scanner(System.in);
        boolean menu = false;
        int escolha = 0;

        System.out.println("\nQuais operações você deseja realizar? ");
        System.out.println("\nVer informações gerais [1]");
        System.out.println("Ligar trator    [2]");
        System.out.println("Começar a andar [3]");
        System.out.println("Aumentar marcha [4]");
        System.out.println("Reduzir marcha  [5]");
        System.out.println("Desligar trator [6]");
        System.out.println("Sair do trator  [7]");

        while (!menu) {

            escolha = sc.nextInt();

            switch (escolha) {

                case 1:
                    trator1.mostrarInfo();
                    break;
                case 2:
                    trator1.ligar();
                    break;
                case 3:
                    trator1.andar();
                    break;
                case 4:
                    trator1.subirMarcha();
                    break;
                case 5:
                    trator1.reduzirMarcha();
                    break;
                case 6:
                    trator1.desligar();
                    break;
                case 7:
                    menu = true;
                    break;
                default:
                    System.out.println("Opção inválida! ");
                    break;
            }

        }

    }

}