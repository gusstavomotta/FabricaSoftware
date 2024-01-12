public class administrador extends empregado {

    // ATRIBUTOS UNICOS DE AMD
    protected double ajudaDeCusto;

    // GETTERS E SETTERS
    public double getAjudaDeCusto() {
        return ajudaDeCusto;
    }

    public void setAjudaDeCusto(double ajudaDeCusto) {
        this.ajudaDeCusto = ajudaDeCusto;
    }

    // SOBREESCREVE O CALCULA SALARIO DA CLASSE MEPREGADO COM OS ATRIBUTOS DO ADM
    @Override
    public void calcularSalario() {

        double salario = (super.salarioBase + ajudaDeCusto);
        System.out.println("O Salário é: R$ " + salario + ".");
    }

}
