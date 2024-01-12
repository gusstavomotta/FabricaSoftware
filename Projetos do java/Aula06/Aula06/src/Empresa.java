
/**
 *
 * @author supti
 */
public class Empresa {
    private final Funcionario[] funcionarios;
    private int totalFunc=0;
    
    public Empresa(){
        funcionarios = new Funcionario[10];
    }
    
    public void contratar(String nome, float salario){
        Funcionario f = new Funcionario(nome, salario);
        funcionarios[totalFunc] = f;
        totalFunc++;
    }
    
    public void desligar(String nome){
        for (int i = 0; i < funcionarios.length; i++) {
            Funcionario f = funcionarios[i];//obtendo o objeto funcionario da posição i
            if(f.getNome().equals(nome)){
                funcionarios[i]=null;
                return;
            }
        }
    }    
}
