// EXERCÍCIOS JAVA / J4.1, J4.2 E J4.3
// GUSTAVO OLIVEIRA DA MOTTA
// DATA DE MODIFICAÇÃO: 30/03/2023


public class conversorUnidade {

    public static void main(String[] args){
        
        double milhas = CalculosUnidade.quilometroMilha(384400);
        System.out.println(milhas);
        
        double pes = CalculosUnidade.metrosPes(100);
        System.out.println(pes);

        double metrosPeses = CalculosUnidade.metroPe(100);
        System.out.println(metrosPeses);

        double pesesCentimetros = CalculosUnidade.peCentimetros(100);
        System.out.println(pesesCentimetros);

        double milhaAcres = CalculosUnidade.milhaAcre(100);
        System.out.println(milhaAcres);

        double acrePeses = CalculosUnidade.acrePes(100);
        System.out.println(acrePeses);
    }

}
