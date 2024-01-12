
import java.util.*;

/**
 *
 * @author supti
 */
public class EmpresaList {
    //private ArrayList<Funcionario> funcionarios = new ArrayList<>();
    //private LinkedList<Funcionario> funcionarios = new LinkedList<>();
    private Vector<Funcionario> funcionarios = new Vector<>();
    
    public EmpresaList(){
    }
    
    public void contratar(String nome, float salario){
        Funcionario f = new Funcionario(nome, salario);
        funcionarios.add(f);        
    }   
    
    public void desligar(String nome){        
        Iterator<Funcionario> iter1 = funcionarios.iterator();
        while(iter1.hasNext()){
            Funcionario f = iter1.next();
            if(f.getNome().equals(nome))
                iter1.remove();
        }           
    }
    
    public void mostrarTodos(){
        for (int i = 0; i < funcionarios.size(); i++) {
            System.out.println(funcionarios.get(i));
        }
    }
}
