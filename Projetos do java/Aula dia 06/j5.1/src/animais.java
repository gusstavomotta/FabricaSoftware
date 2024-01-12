//NOME DA CLASSE
public class animais {

    // ATRIBUTOS
    protected String comida;
    private double peso;

    // GETTERS E SETTERS
    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public String getComida() {
        return comida;
    }

    public void setComida(String comida) {
        this.comida = comida;
    }

    // MÉTODOS GERAIS
    public void andar() {

        System.out.println("O animal está andando!");
    }

    public void dormir() {
        System.out.println("O animal está dormindo!");
    }

    public void comer() {

        System.out.println("O animal está comendo " + comida);
    }

    public void fazerBarulhos() {

        System.out.println("O animal está fazendo barulho!");
    }

}
