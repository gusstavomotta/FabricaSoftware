//EXERCÍCIOS DE JAVA / J4.4, J4.5
//GUSTAVO OLIVEIRA DA MOTTA
//DATA DE MODIFICAÇÃO: 29/03/2023

public class conversorTempo {

    public static int anoss(int dias) {
        return dias / 365;
    }

    public static int mesess(int dias) {
        return dias / 30;
    }

    public static int semanass(int dias) {
        return dias / 7;
    }

    public static int diass(int dias) {
        return dias;
    }

    public static int horas(int dias) {
        return dias * 24;
    }

    public static int minutos(int dias) {
        return dias * 24 * 60;
    }

    public static int segundos(int dias) {
        return dias * 24 * 60 * 60;
    }

}
