import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        
        ArrayList <Habitacao> habitacoes = new ArrayList<>();

        Apartamento a1 = new Apartamento();
        Casa c1 = new Casa();
        kitinete k1=  new kitinete();

        Casa c2 = new Casa(105, 3, 2, false, enumPiso.LAMINADO, 10, "verde", true);
        Apartamento a2 = new Apartamento(105, 3, 2, false, enumPiso.GRANITO, 10, true, true);
        kitinete k2 = new kitinete(30, 2, 2, true, enumPiso.MARMORE);


        habitacoes.add(a1);
        habitacoes.add(c1);
        habitacoes.add(k1);
        habitacoes.add(a2);
        habitacoes.add(c2);
        habitacoes.add(k2);


        for (int i = 0; i < habitacoes.size(); i++){

            Habitacao c = habitacoes.get(i);
            System.out.println("~~~~~~~~ Informações Habitação ~~~~~~~~");
            
            System.out.println(c);

            float iptu = c.calcularIptu();
            System.out.println("Iptu: " + iptu + "\n");
        }   


    }
}
