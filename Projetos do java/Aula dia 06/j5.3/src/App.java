public class App {
    public static void main(String[] args) throws Exception {

        // CHAMANDO OS CONSTRUTORES
        fornecedor fornecedor = new fornecedor();
        empregado empregado = new empregado();
        administrador adm = new administrador();
        operario operario = new operario();
        vendedor vendedor = new vendedor();

        // REALIZANDO OS TESTES E OS CÁLCULOS
        adm.setAjudaDeCusto(10000);
        adm.calcularSalario();

        operario.setValorProducao(20000);
        operario.setComissao(10);
        operario.calcularSalario();

        fornecedor.setValorCredito(10000);
        fornecedor.setValorDivida(5000);
        fornecedor.obterSaldo();

        empregado.setCodigoSetor(10);
        empregado.setSalarioBase(3000);
        empregado.setImposto(10);
        empregado.calcularSalario();

        vendedor.setComissao(10);
        vendedor.setCpf(0422);
        vendedor.setNome("Gustavo");
        vendedor.setSalarioBase(5000);
        vendedor.setValorVendas(5000);
        vendedor.calcularSalario();
                                    
    }
}
