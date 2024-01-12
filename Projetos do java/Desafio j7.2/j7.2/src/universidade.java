
public class universidade extends Funcionario implements gerente {

    private String universidade;

    public universidade(String nome, int codigo, String universidade) {

        super(nome, codigo);
        this.universidade = universidade;
        calcularSalario();
    }

    public String getUniversidade() {
        return universidade;
    }

    public void setUniversidade(String universidade) {
        this.universidade = universidade;
    }

    @Override
    public String toString() {

        return "Nome: " + getNome() + " | Comissão: " + adicional() + " | Salario: R$ " + getSalarioBase();
    }

    public double calcularSalario() {

        return salarioBase = salarioBase * 2 + adicional();
    }

    public double adicional() {

        return 5000;
    }
}
