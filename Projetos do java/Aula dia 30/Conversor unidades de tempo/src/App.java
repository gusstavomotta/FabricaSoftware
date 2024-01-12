//EXERCÍCIOS DE JAVA / J4.4, J4.5
//GUSTAVO OLIVEIRA DA MOTTA
//DATA DE MODIFICAÇÃO: 29/03/2023

public class App {
    public static void main(String[] args) throws Exception {

     
        double diasEmAnos = conversorTempo.anoss(365);
        System.out.println("Anos: " + diasEmAnos);

        double diasEmMeses = conversorTempo.mesess(365);
        System.out.println("Meses: " + diasEmMeses);

        double diasEmSemanas = conversorTempo.semanass(365);
        System.out.println("Semanas: " + diasEmSemanas);

        double diasReais = conversorTempo.diass(365);
        System.out.println("Dias: " + diasReais);

        double diasEmHoras = conversorTempo.horas(365);
        System.out.println("Horas: " + diasEmHoras);

        double diasEmMinutos = conversorTempo.minutos(365);
        System.out.println("Minutos: " + diasEmMinutos);

        double diasEmSegundos = conversorTempo.segundos(365);
        System.out.println("Segundos: " + diasEmSegundos);

    }
}
