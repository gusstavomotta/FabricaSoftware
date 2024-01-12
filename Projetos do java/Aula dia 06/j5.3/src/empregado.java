public class empregado extends pessoa {

    // ATRIBUTOS ESPECÍFICOS DE EMPREGADO
    protected int codigoSetor;
    protected double imposto;
    protected double salarioBase = 10000;

    // GETTERS E SETTERS
    public int getCodigoSetor() {
        return codigoSetor;
    }

    public void setCodigoSetor(int codigoSetor) {
        this.codigoSetor = codigoSetor;
    }

    public double getSalarioBase() {
        return salarioBase;
    }

    public void setSalarioBase(double salarioBase) {
        this.salarioBase = salarioBase;
    }

    public double getImposto() {
        return imposto;
    }

    public void setImposto(double imposto) {
        this.imposto = imposto;
    }

    // MÉTODO PARA CALCULAR O SALARIO
    public void calcularSalario() {

        double descontos = (salarioBase) * (imposto / 100);
        double salario = (salarioBase - descontos);
        System.out.println("O Salário é de: R$ " + salario + ".");
    }
}
