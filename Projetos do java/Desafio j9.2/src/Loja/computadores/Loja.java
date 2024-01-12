package Loja.computadores;

public class Loja {

    Computador[] computadores = new Computador[10];

    public void adicionarComputador(Computador a) {
        for (int i = 0; i < computadores.length; i++) {
            if (computadores[i] == null) {
                computadores[i] = a;
                break;
            }
        }
    }

    public void mostrarComputadores() {
        for (int i = 0; i < computadores.length; i++) {
            Computador c = computadores[i];
            System.out.println(c);
        }
    }

}
