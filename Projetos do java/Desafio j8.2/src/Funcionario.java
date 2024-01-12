
public abstract class Funcionario implements iConstantes {

    int diasTrabalhados;
    int valorHora = 50;
    double salarioLiquido;
    double salarioBruto;
    double salariosMinimos;

    public Funcionario(int diasTrabalhados) {
        this.diasTrabalhados = diasTrabalhados;
    }

    public double caclulaSalarioBruto() {

        return (valorHora * CARGA_HORARIA) * diasTrabalhados;
    }

    public String toString() {

        return String.format("Salário liquido: R$ %.2f | Salário bruto: R$ %.2f | Salários Mínimos: %.2f", this.salarioLiquido,this.caclulaSalarioBruto(), this.salariosMinimos);
    }

}