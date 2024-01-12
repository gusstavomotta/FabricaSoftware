public abstract class Funcionario {

    private String nome;
    private int codigo;
    protected double salarioBase;

    public Funcionario(String nome, int codigo) {

        this.nome = nome;
        this.codigo = codigo;
        this.salarioBase = 1000;
    }

    public double getSalarioBase() {
        return salarioBase;
    }

    public void setSalarioBase(double salarioBase) {
        this.salarioBase = salarioBase;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;

    }

    public String toString() {

        return "Nome: " + nome + " | Código: " + codigo + " | Salário: R$ " + salarioBase;
    }

    public abstract double calcularSalario();
}
