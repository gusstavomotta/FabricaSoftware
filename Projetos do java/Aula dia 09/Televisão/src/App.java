public class App {
    public static void main(String[] args) throws Exception {

        //criando tv1 da classe (televisao)
        televisao tv1 = new televisao();

        //atribuindo as características
        tv1.marca = "Samsung";
        tv1.polegadas = 65;
        tv1.volume = 20;
        tv1.consumoKwh = 35;
        tv1.canal = 3;
        
        //chamando as funções da televisao
        tv1.ligar();
        tv1.aumentarVolume();
        tv1.baixarVolume();
        tv1.trocarCanal();
        tv1.desligar();
    }
}