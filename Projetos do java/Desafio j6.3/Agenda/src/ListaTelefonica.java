
import java.util.ArrayList;
import java.util.Scanner;

// CLASSE DA LISTA TELEFONICA COM OS MÉTODOS E INICIALIZAÇÃO DA LISTA
public class ListaTelefonica {

    // CRIAÇÃO DE UMA ARRAYLIST DOI TIPO CONTATO QUE ARMAZENA OS ATRIBUTOS DE UM
    // CONTATO
    private ArrayList<Contato> listaTelefonica;
    Scanner sc = new Scanner(System.in);

    // CONSTRUTOR
    public ListaTelefonica() {

        listaTelefonica = new ArrayList<Contato>();
    }

    // ADICIONA UM CONTATO NA LISTA TELEFONICA
    public void adicionarContato() {

        String nome;
        String endereço;
        String email;
        int telefone;

        Scanner sc = new Scanner(System.in);
        System.out.print("\nInsira o nome: ");
        nome = sc.nextLine();

        System.out.print("Insira o endereço: ");
        endereço = sc.nextLine();

        System.out.print("Insira o email: ");
        email = sc.nextLine();
        
        System.out.print("Insira o telefone: ");
        telefone = sc.nextInt();

        Contato contato = new Contato(nome, endereço, email, telefone);
        listaTelefonica.add(contato);
        System.out.println("\nContato adicionado com sucesso!");

    }

    // PRINTA TODOS OS CONTATOS NA LISTA TELEFONICA
    public void mostrarTodosContatos() {

        for (int i = 0; i < listaTelefonica.size(); i++) {
            System.out.println(listaTelefonica.get(i));
        }
    }

    // EXCLUI CONTATO DA LISTA TELEFONICA PELO NOME
    public void excluirContato() {

        System.out.print("\nInforme o nome do contato: ");
        String excluiNome = sc.nextLine();

        for (int i = 0; i < listaTelefonica.size(); i++) {

            Contato c = listaTelefonica.get(i);
            if (c.getNome().equals(excluiNome)) {
                listaTelefonica.remove(i);
                System.out.println("\nContato excluído com sucesso!");
                break;
            }
        }
    }

    // ALTERA DADOS DE UM CONTATO PELO NOME
    public void alterarDadosContato() {

        System.out.print("\nInforme o nome do contato você deseja alterar: ");
        String modificaContato = sc.next();

        // PERCORRE A LISTA
        for (int i = 0; i < listaTelefonica.size(); i++) {

            Contato c = listaTelefonica.get(i);
            // VERIFICA SE O NOME QUE ESTÁ NA LISTA (I) É IGUAL AO INSERIDO, CASO VERDADEIRO
            // RELIZA AS OUTRAS OPERAÇÕES
            if (c.getNome().equals(modificaContato)) {

                System.out.printf("Informe o atributo que você deseja alterar: ");
                String atributoContato = sc.next();

                switch (atributoContato) {

                    case "nome":
                        System.out.print("Informe o novo nome: ");
                        String alteraNome = sc.next();
                        c.setNome(alteraNome);
                        break;

                    case "endereço":
                        System.out.print("Informe o novo endereço: ");
                        String alteraEndereco = sc.next();
                        c.setEndereço(alteraEndereco);
                        break;

                    case "email":
                        System.out.print("Informe o novo email: ");
                        String alteraEmail = sc.next();
                        c.setEmail(alteraEmail);
                        break;

                    case "telefone":
                        System.out.print("Informe o novo telefone: ");
                        int alteraTelefone = sc.nextInt();
                        c.setTelefone(alteraTelefone);
                        break;

                }
            }
        }
    }
}
