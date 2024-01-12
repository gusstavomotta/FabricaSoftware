public class App {
    public static void main(String[] args) throws Exception {

        // criando um PC da classe (computador)
        computador pc = new computador();

        // atribuindo características
        pc.processador = "Amd";
        pc.fonte = 550;
        pc.armazenamento = 200;
        pc.memoria = 6;

        // chamando as funções do computador
        pc.ligar();
        pc.abrirNavegador();
        pc.abrirNavegador();
        pc.abrirNavegador();
        pc.fecharNavegador();
        pc.baixar();
        pc.baixar();
        pc.baixar();
        pc.excluir();
        pc.desligar();

        System.out.printf("asa", pc.memoria);
    }
}