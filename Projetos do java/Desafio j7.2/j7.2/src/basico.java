public class basico extends Funcionario implements vendedor {

    private String escola;

    public basico(String nome, int codigo, String escola) {

        super(nome, codigo);
        this.escola = escola;
        calcularSalario();
    }

    public String getEscola() {
        return escola;
    }

    public void setEscola(String escola) {
        this.escola = escola;
    }

    @Override
    public String toString() {

        return "Nome: " + getNome() + " | Comissão: " + adicional() + " | Salario: R$ " + getSalarioBase();
    }

    public double calcularSalario() {

        return salarioBase = salarioBase * 1.1 + adicional();
    }

    public double adicional() {
        return 850;
    }
}
