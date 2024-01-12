//EXERCÍCIOS DE JAVA / J4.8, J4.9
//GUSTAVO OLIVEIRA DA MOTTA
//DATA DE MODIFICAÇÃO: 30/03/2023

public class App {
    public static void main(String[] args) throws Exception {

        // cria diferentes canetas usando os construtores
        caneta bic;
        //bic = new caneta();
        //bic = new caneta("BIC", "Vermelho");
        bic = new caneta("BIC", "Preto", 0.9);

        // executa as funções da caneta
        // bic.destampar();
        // bic.escrever();
        // bic.rabiscar();
        // bic.pintar();
        // bic.tampar();

        // modifica os atributos
        //bic.modificarAtributos("Laranja");
        bic.modificarAtributos("Verde", "Puc");
       // bic.modificarAtributos("Rosa", "Unisc", 0.20);

        // printa os atributos modificados
        System.out.println("\nAtributos Modificados: ");
        System.out.println("Modelo: " + bic.getModelo());
        System.out.println("Cor: " + bic.getCor());
        System.out.println("ponta: " + bic.getPonta());
    }

}
