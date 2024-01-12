public class empresa{

    private funcionario[] funcionarios;
    private int totalFunc = 0;

    public empresa(){

        funcionarios = new funcionario[10];
    }
    public void contratar(String nome, float salario){

        funcionario f = new funcionario(nome,salario);
        funcionarios[totalFunc] = f;
        totalFunc++;
    }
}
