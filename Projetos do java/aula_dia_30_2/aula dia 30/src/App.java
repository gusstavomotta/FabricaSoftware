public class App {
    public static void main(String[] args) throws Exception {
        
        cachorro cao = new cachorro();
        coruja coruja = new coruja();
        ave galinha = new ave();

        cao.fazerBarulho();
        galinha.fazerBarulho();
        coruja.fazerBarulho();
        coruja.setComida("insetos");
        coruja.comer();
    }
}
