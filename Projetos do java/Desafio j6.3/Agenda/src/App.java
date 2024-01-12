import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        ListaTelefonica lista = new ListaTelefonica();
        int op = 0;

        while (op != 5) {

            System.out.println("\n~~~~~~~~~~ MENU ~~~~~~~~~~");
            System.out.println("1 - Adicionar contato. ");
            System.out.println("2 - Excluir contato.");
            System.out.println("3 - Mostrar todos os contatos.");
            System.out.println("4 - Alterar Contato");
            System.out.println("5 - Encerrar programa.");
            System.out.printf("\nQual opção você deseja realizar? ");
            Scanner sc = new Scanner(System.in);
            op = sc.nextInt();

            switch (op) {

                case 1:
                    lista.adicionarContato();
                    break;

                case 2:
                    lista.excluirContato();
                    break;

                case 3:
                    lista.mostrarTodosContatos();
                    break;

                case 4:
                    lista.alterarDadosContato();
                    break;

            }

        }

    }

}
