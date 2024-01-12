public class arCondicionado {

    // declarando as variáveis
    boolean ligado;
    int temperatura = 24;
    float consumo;
    String marca;
    int btu;

    // criando funções

    // função para ligar o ar condiconado
    void ligar() {
        ligado = true;
        System.out.println("\nAr ligando...");
        System.out.printf("Ar ligado em %dºC\n", temperatura);

    }

    // função para desligar o ar
    void desligar() {
        ligado = false;
        System.out.println("\nAr desligando...");
    }

    // função para aumentar a temperatura/ incrementa em 1 a temperatura
    void aumentarTemperatura() {

        temperatura += 1;

        if (temperatura >= 27) {
            System.out.println("\nAumentando a temperatura...");
            System.out.println("Temperatura máxima!\n");
            temperatura = 27;
        } else {
            System.out.println("\nAumentando temperatura");
            System.out.printf("Temperatura atual em %d°C\n", temperatura);

        }
    }

    // função para diminuir a temperatura / decrementa em 1 a temperatura
    void diminuirTemperatura() {

        temperatura -= 1;

        if (temperatura <= 18) {
            System.out.println("\nDiminuindo a temperatura...");
            System.out.println("Temperatura mínima!\n");
            temperatura = 18;

        } else {
            System.out.println("\nDiminuindo temperatura");
            System.out.printf("Temperatura atual em %d°C\n", temperatura);

        }
    }

}
