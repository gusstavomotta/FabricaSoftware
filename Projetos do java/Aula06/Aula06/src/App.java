/**
 *
 * @author supti
 */
public class App {
    public static void main(String[] args){
        EmpresaList unisc = new EmpresaList();
        unisc.contratar("Ivan", 99999);
        unisc.contratar("Bill", 1000);
        unisc.contratar("Bill", 2000);
        unisc.contratar("Paul", 2000);
        unisc.contratar("Zuke", 300);
        
        unisc.mostrarTodos();
    }
}
