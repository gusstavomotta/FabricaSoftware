// EXERCÍCIOS JAVA / J4.1, J4.2 E J4.3
// GUSTAVO OLIVEIRA DA MOTTA
// DATA DE MODIFICAÇÃO: 30/03/2023


public class campoFutebol {
    
    public static void main (String[] args){

        double campoEmPes = CalculosUnidade.metrosPes(8250);
        System.out.println(campoEmPes);

        double campoEmAcres = CalculosUnidade.metrosAcres(8250);
        System.out.println(campoEmAcres);

        double campoEmCentimetros = CalculosUnidade.centimetroParaMetro(8250);
        System.out.println(campoEmCentimetros);
    }
}
