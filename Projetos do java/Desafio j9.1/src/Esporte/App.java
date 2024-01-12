package Esporte;
public class App {
    public static void main(String[] args) throws Exception {
        
        Time t1 = new Time("Internacional", "Mano");
        
        t1.adicionarAleta(new Atleta("Dourado", 30, "Lateral"));
        t1.adicionarAleta(new Atleta("Geromessi", 22, "Zagueiro"));
        t1.adicionarAleta(new Atleta("Dale", 39, "Meio campo"));
        
        double idadeMedia = t1.calcularMediaIdade();
        System.out.printf("Idade média: %.2f", idadeMedia);
    }
}
