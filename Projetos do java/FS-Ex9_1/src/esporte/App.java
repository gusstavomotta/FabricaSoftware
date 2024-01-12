package esporte;

/**
 *
 * @author supti
 */
public class App {
    public static void main(String arg[]){
        Time t = new Time("Internacional","Mano Menezes");
        t.adicionarAtleta(new Atleta("Kaneman",25,"Zagueiro" ));
        t.adicionarAtleta(new Atleta("...",30,"Goleiro" ));
        double idadeMedia = t.calcularIdadeMedia();
        System.out.println("Idade média é " + idadeMedia);
    }
}
