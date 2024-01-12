package modeloprova;

import java.util.ArrayList;

/**
 *
 * @author Prof. Ivan L. Süptitz
 */
public class App {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        ArrayList<Habitacao> lstHab = new ArrayList<>();

        //testando os construtores SEM parâmetros
        Casa c1 = new Casa();
        Apartamento a1 = new Apartamento();
        Kitinete k1 = new Kitinete();

        //testando os construtores COM parâmetros
        Casa c2 = new Casa(105, "Azul-marinho", true, 85, 3, 2, true, EnumPiso.CERAMICO);
        Apartamento a2 = new Apartamento(9.5f, false, true, 70.5f, 2, 1, true, EnumPiso.PORCELANATO);
        Kitinete k2 = new Kitinete(60, 1, 1, false, EnumPiso.LAMINADO);

        //adicionando todos os objetos na lista
        lstHab.add(c1);
        lstHab.add(a1);
        lstHab.add(k1);
        lstHab.add(c2);
        lstHab.add(a2);
        lstHab.add(k2);

        //iterando sobre a lista para testar os métodos
        for (int i = 0; i < lstHab.size(); i++) {
            Habitacao h = lstHab.get(i);//obtendo o elemento atual da lista

            System.out.println("\n---------------------------\n");
            System.out.printf("%dª habitação:\n", i + 1);

            float iptu = h.calcularIPTU();
            System.out.printf("IPTU: R$ %.2f\n", iptu);

            System.out.println(h.toString());
        }
    }

}
