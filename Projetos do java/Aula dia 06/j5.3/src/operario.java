public class operario extends empregado {

    // ATRIBUTOS UNICOS DE OPERARIO
    protected double valorProducao;
    protected double comissao;

    // GETTERS E SETTERS
    public double getValorProducao() {
        return valorProducao;
    }

    public void setValorProducao(double valorProducao) {
        this.valorProducao = valorProducao;
    }

    public double getComissao() {
        return comissao;
    }

    public void setComissao(double comissao) {
        this.comissao = comissao;
    }

    // SOBREESCREVE O METODO CALCULAR SALARIO DO EMPREGADO COM OS ATRIBUTOS DO
    // OPERARIO
    @Override
    public void calcularSalario() {

        double salario = (valorProducao * comissao / 100) + salarioBase;
        System.out.println("O Salário é: R$ " + salario + ".");
    }
}
