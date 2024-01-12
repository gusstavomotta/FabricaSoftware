
public class App {
    public static void main(String[] args) throws Exception {

        //construtores
        peixe traira = new peixe();
        vaca mococa = new vaca();
        bezerro mocoquinha = new bezerro();
        tubarao tutu = new tubarao();

        //CHAMANDO MÉTODOS E SETANDO ALGUNS VALORES

         traira.andar();
         traira.comer();
         traira.dormir();
         traira.setamanho(30.5);
         tutu.setDentes(300);
         traira.tamanho();
         tutu.dentes();
         tutu.comer();

         mococa.andar();
         mococa.comer();
         mococa.dormir();
         mococa.setPeso(500);
         mococa.peso();
         mococa.setPelo("Marrom");
         mococa.pelo();
         mocoquinha.setMeses(5);
         mocoquinha.andar();
         mocoquinha.mamar();
         mocoquinha.meses();
    }
}
