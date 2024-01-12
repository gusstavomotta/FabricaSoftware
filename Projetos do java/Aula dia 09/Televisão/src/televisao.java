
public class televisao {

    //declarando as variáveis
    boolean ligado;
    int volume;
    int canal;
    int polegadas;
    int consumoKwh;;
    String marca;

    // função para ligar a tv
    void ligar() {

        ligado = true;
        System.out.printf("\nTelevisão ligando...");
        System.out.printf("\nCanal %d\n", canal);
    }

    // função para desligar a tv
    void desligar() {

        ligado = false;
        System.out.printf("\nTv desligando...");
    }

    // função para aumentar o volume e calcular o volume atual / com limite máximo
    void aumentarVolume() {

        volume += 3;
        System.out.printf("\nAumentando o volume...");

        if (volume >= 50) {
            System.out.println("Volume máximo!");
            volume = 50;
        } else {
            System.out.printf("\nvolume atual : %d\n", volume);
        }
    }
    // função para baixar o volume e calcular o volume total / com limite mínimo
    void baixarVolume() {
        volume -= 3;

        System.out.println("\nBaixando volume...");

        if (volume <= 0) {
            System.out.println("Volume mínimo!");
            volume = 0;
        } else {
            System.out.printf("Volume atual: %d\n", volume);
        }
    }
    // função para trocar de canal
    void trocarCanal() {
        canal += 3;
        System.out.println("\nMudando de canal...");
        System.out.printf("Canal atual: %d\n", canal);

    }
}