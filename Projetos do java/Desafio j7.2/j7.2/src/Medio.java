public class Medio extends Funcionario implements supervisor {

    private String escola;

    public Medio(String nome, int codigo, String escola) {

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

        return salarioBase = salarioBase * 1.5 + adicional();
    }

    public double adicional() {
        return 1800;
    }
}
