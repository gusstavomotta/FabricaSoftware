public class peixe extends animais {

    // ATRIBUTOS UNICOS DA CLASSE
    private double tamanho;

    // GETTERS E SETTERS
    public double getamanho() {
        return tamanho;
    }

    public void setamanho(double tamanho) {
        this.tamanho = tamanho;
    }

    // MÉTODOS DA CLASSE
    public void tamanho() {

        System.out.println("O peixe mede: " + tamanho + " cm!");
    }

    // SOBREESCREVENDO METODOS GERAIS
    @Override
    public void andar() {

        System.out.println("Peixe nadando!");
    }

    @Override
    public void comer() {

        System.out.println("O peixe está comendo minhoca!");
    }

    @Override
    public void dormir() {

        System.out.println("Peixe não dorme!");
    }
}
