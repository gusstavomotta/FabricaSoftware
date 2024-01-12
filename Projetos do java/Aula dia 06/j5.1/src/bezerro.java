public class bezerro extends vaca {

    // ATRIBUTOS UNICOS DA CLASSE
    private int meses;

    // GETTERS E SETTERS
    public int getMeses() {
        return meses;
    }

    public void setMeses(int meses) {
        this.meses = meses;
    }

    // SOBREESCREVENDO METODO GERAL
    @Override
    public void andar() {

        System.out.println("O bezerro nao sabe andar!");
    }

    // METODOS DA CLASSE
    public void mamar() {

        System.out.println("O bezerro está mamando!");
    }

    public void meses() {

        System.out.println("O bezerro tem " + meses + " meses!");
    }
}
