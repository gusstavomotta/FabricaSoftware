public class App {

    public static void main(String[] args) throws Exception {
        // criando um ar condicionado (a1) da classe arCondicionado
        arCondicionado a1 = new arCondicionado();

        //atribuindo características ao a1
        a1.marca = "Electrolux";
        a1.consumo = 8.5f;
        a1.btu = 9000;

        //chamando funções do ar condicionado
        a1.ligar();
        a1.aumentarTemperatura();
        a1.aumentarTemperatura();
        a1.aumentarTemperatura();
        a1.diminuirTemperatura();
        a1.diminuirTemperatura();
        a1.desligar();
    }
}