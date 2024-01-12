/**
 *
 * @author supti
 */
public class Funcionario {
    private String nome;
    private float salario;

    public Funcionario(String nome, float salario) {
        this.nome = nome;
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }

    public float getSalario() {
        return salario;
    }
    
    public String toString(){
        return nome + " R$ " + salario;
    }
    
}
