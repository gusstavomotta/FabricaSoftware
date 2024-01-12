public class MotoristaTaxi extends Funcionario implements iSalario {

    public MotoristaTaxi(int diasTrabalhados) {
        super(diasTrabalhados);
        getQtdSalMinimos();
        getSalarioLiquido();

    }

    @Override
    public double getQtdSalMinimos() {

        double salarioLiquido = getSalarioLiquido();
        salariosMinimos = salarioLiquido / SAL_MINIMO;
        return salariosMinimos;
    }

    @Override
    public double getSalarioLiquido() {

        double salarioBruto = caclulaSalarioBruto();
        return salarioLiquido = (salarioBruto) - (salarioBruto * 0.15);
    }

}