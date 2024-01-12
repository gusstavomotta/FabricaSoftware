
public class App {
    public static void main(String[] args) throws Exception {

        Professor evandro = new Professor(30);
        Professor ivan = new Professor(29);
        MotoristaTaxi matheus = new MotoristaTaxi(29);
        MotoristaTaxi victor = new MotoristaTaxi(31);

        /*
         * System.out.println(evandro.caclulaSalarioBruto());
         * System.out.println(evandro.getQtdSalMinimos());
         * System.out.println(evandro.getSalarioLiquido());
         */

        System.out.println(evandro);
        System.out.println(ivan);
        System.out.println(matheus);
        System.out.println(victor);

    }
}
