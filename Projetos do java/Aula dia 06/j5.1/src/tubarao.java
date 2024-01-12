public class tubarao extends peixe {

    // ATRIBUTOS UNICOS DA CLASSE
    private int dentes;

    // GETTERS E SETTERS
    public int getDentes() {
        return dentes;
    }

    public void setDentes(int dentes) {
        this.dentes = dentes;
    }

    // SOBREESCREVENDO METODOS GERAIS
    @Override
    public void comer() {

        System.out.println("O tutu está comendo peixes!");
    }
    // PRINTANDO A VARIÁVEL / METODOS DA CLASSE

    public void dentes() {

        System.out.println("O tutu tem " + dentes + " dentes!");
    }

}
