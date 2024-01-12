public class vendedor extends empregado {

    // ATRIBUTOS UNICOS DE VENDEDOR
    protected double valorVendas;
    protected double comissao;

    // GETTERS E SETTERS
    public double getValorVendas() {
        return valorVendas;
    }

    public void setValorVendas(double valorVendas) {
        this.valorVendas = valorVendas;
    }

    public double getComissao() {
        return comissao;
    }

    public void setComissao(double comissao) {
        this.comissao = comissao;
    }

    // SOBREESCREVE O METODO CALCULA SALARIO COM OS ATRIBUTOS DO VENDEDOR
    @Override
    public void calcularSalario() {

        double salario = (valorVendas * comissao / 100) + (super.salarioBase);
        System.out.println("O Salário é: R$ " + salario + ".");
    }
}
