public class funcionario {
    
    private String nome;
    private float salario;

    public String getNome() {
        return nome;
    }

    public float getSalario() {
        return salario;
    }
 
    public funcionario(String nome, float salario){

        this.nome = nome;
        this.salario = salario;
    }
    public String toString(){

        return nome + " R$ " + salario;
    }
}
