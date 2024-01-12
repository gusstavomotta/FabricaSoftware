//import java.util.ArrayList;
import java.util.LinkedList;

public class empresaList{
    
    //private ArrayList<funcionario> funcionarios;
    private LinkedList<funcionario> funcionarios;

    public empresaList(){
    
        funcionarios = new LinkedList<funcionario>();
    }
    public void contratar(String nome, float salario){
    
        funcionario f = new funcionario(nome,salario);
        funcionarios.add(f);
        
    }
    public void desligar(String nome){

    for(int i=0; i < funcionarios.size();i++){

        funcionario f = funcionarios.get(i);//obtendo objeto funcionario da posição i

        if( f.getNome() .equals(nome)){
            funcionarios.remove(i);
            break;
        }
        
    }
    }
    public void mostrarTodos(){

        for(int i = 0; i < funcionarios.size(); i++){
            System.out.println(funcionarios.get(i));
        }
    }
}

