package Loja.computadores;

import java.util.Random;

public class App {
    public static void main(String[] args) throws Exception {

        Loja Lan_House = new Loja();
        Random rnd = new Random();

        for (int i = 0; i < 10; i++) {

            int opcao = rnd.nextInt(3);
            Computador c;
            switch (opcao) {
                case 0:
                    c = new Computador(16, 4.2, "PT-BR", 23);
                    break;
                case 1:
                    c = new Computador(8, 3.9, "EN", 27);
                    break;

                case 2:
                    c = new Computador(4, 3.6, "PT-PT", 21.5);
                    break;
                default:
                    c = new Computador(12, 3.2, "ES", 24);
            }

            Lan_House.adicionarComputador(c);
        }

        Lan_House.mostrarComputadores();

    }
}
