//EXERCÍCIOS DE JAVA / J4.8, J4.9
//GUSTAVO OLIVEIRA DA MOTTA
//DATA DE MODIFICAÇÃO: 30/03/2023


public class caneta {

    // cria o primeiro construtor sem argumentos
    public caneta() {

        System.out.println("Construindo caneta padrão!");
        cor = "Azul";
        tampado = true;
        ponta = 0.5;

        System.out.println("Cor: " + cor);
        System.out.println("Tampado: " + tampado);
    }

    // cria o segundo construtor, passando o modelo e a cor como argumentos
    public caneta(String modelo, String cor) {

        System.out.println("\nConstruindo caneta, cor e modelo!");
        this.cor = cor;
        this.modelo = modelo;

        System.out.println("Cor: " + cor);
        System.out.println("Modelo: " + modelo);
    }

    // cria o terceiro construtor, passando modelo, cor e ponta como argumentos
    public caneta(String modelo, String cor, double ponta) {

        System.out.println("\nConstruindo caneta completa!");

        this.modelo = modelo;
        this.cor = cor;
        this.ponta = ponta;

        System.out.println("Modelo: " + modelo);
        System.out.println("Cor: " + cor);
        System.out.println("Ponta: " + ponta);
    }

    // variáveis com diferentes visibilidades
    public boolean tampado = true;
    private String modelo;
    private String cor;
    private double ponta;

    // getters e setters para acessar os valores
    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public double getPonta() {
        return ponta;
    }

    public void setPonta(double ponta) {
        this.ponta = ponta;
    }

    // verifica se a caneta está tampada, se não estiver escreve
    void escrever() {

        if (tampado == true) {
            System.out.println("\nA caneta está tampada!");

        } else {
            System.out.println("Escrevendo...");
        }
    }

    // verifica se a caneta está tampada, se não estiver rabisca
    void rabiscar() {

        if (tampado == true) {
            System.out.println("\nA caneta está tampada!");

        } else {
            System.out.println("Rasbicando...");
        }
    }

    // verifica se a caneta está tampada, se não estiver pinta
    void pintar() {

        if (tampado == true) {
            System.out.println("\nA caneta está tampada!");

        } else {
            System.out.println("Rabiscando...");
        }
    }

    // verifica se a caneta já está destampada, se não destampa
    void destampar() {

        if (tampado == false) {
            System.out.println("\nA caneta ja está sem a tampa! ");

        } else {
            System.out.println("Destampando...");
            tampado = false;
        }
    }

    // verifiv se já esta tampado, se não tampa
    void tampar() {

        if (tampado == true) {
            System.out.println("\nA caneta já está com a tampa!");
        } else {

            System.out.println("\nTampando caneta...");
            tampado = true;
        }
    }

    // modifica os atributos passando como argumento a cor
    void modificarAtributos(String cor) {
        this.cor = cor;
    }

    // modifica os atributos passando como argumento a cor e o modelo
    void modificarAtributos(String cor, String modelo) {
        this.cor = cor;
        this.modelo = modelo;
    }

    // modifica os atributos passando como argumento a cor. modelo e a ponta
    void modificarAtributos(String cor, String modelo, double ponta) {
        this.cor = cor;
        this.modelo = modelo;
        this.ponta = ponta;
    }
}
