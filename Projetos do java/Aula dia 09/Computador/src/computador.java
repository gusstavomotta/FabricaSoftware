public class computador {

    //declarando as varáveis
    boolean ligado;
    boolean navegador;
    boolean download;
    int memoria;
    int armazenamento;
    String processador;
    int fonte;

    //criando as funções do computador
    void ligar() {

        ligado = true;
        System.out.println("\nComputador ligando...");
        System.out.println("Bem vindo ao windows! ");

    }
    // função para ligar o pc
    void desligar() {

        ligado = false;
        System.out.println("\nComputador desligando...\n");

    }
    // função para abrir o navegador  e calcular o uso de memoria
    void abrirNavegador() {

        navegador = true;
        memoria += 2;

        if (memoria >= 16) {
            System.out.println("\nAbrindo navegador...");
            System.out.println("Utilizando toda a memória RAM, não é possivel abrir o navegador.\n");
            memoria = 8;
        } else {

            System.out.println("\nAbrindo navegador...");
            System.out.printf("Uso de memória: %d GB\n", memoria);
        }

    }
    // função para fechar o navegador e calcular o uso de memoria
    void fecharNavegador() {

        navegador = false;
        memoria -= 2;

        if(memoria <= 0){
            System.out.println("Todas as abas ja foram fechadas");
            memoria = 2;
        }
        System.out.println("\nFechando o navegador...");
        System.out.printf("Uso de memória: %d GB\n", memoria);

    }
    // função para fazer um download e calcular o uso de armazenamento
    void baixar() {

        download = true;
        armazenamento += 25;
        
        if (armazenamento >= 250) {
            System.out.println("\nFazendo Download...");
            System.out.println("Armazenamento cheio!\n");
            armazenamento = 250;
        } else {
            System.out.println("\nFazendo download...");
            System.out.printf("Uso de armazenamento %d GB\n", armazenamento);
        }
    }
    // função para excluir algo e calcular o uso do armazenamento
    void excluir() {

        download = false;
        armazenamento -= 25;
        
        if (armazenamento <= 0) {
            System.out.println("\nExcluindo...");
            System.out.println("O armazenamento está vazio!\n ");
            armazenamento = 0;
        } else {
            System.out.println("\nExluindo...");
            System.out.printf("Uso de armazenamento %d GB\n", armazenamento);
        }
    }

}