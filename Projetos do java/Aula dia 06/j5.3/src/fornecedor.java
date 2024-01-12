public class fornecedor extends pessoa {

    // ATRIBUTOS UNICOS DE FORNECEDOR
    protected double valorCredito;
    protected double valorDivida;

    // GETTERS E SETTERS
    public double getValorCredito() {
        return valorCredito;
    }

    public void setValorCredito(double valorCredito) {
        this.valorCredito = valorCredito;
    }

    public double getValorDivida() {
        return valorDivida;
    }

    public void setValorDivida(double valorDivida) {
        this.valorDivida = valorDivida;
    }

    // CALCULA O SALDO
    public void obterSaldo() {

        double saldo = (valorCredito - valorDivida);
        System.out.println("Saldo: R$ " + saldo + ".");
    }
}
