public class App {
    public static void main(String[] args) {

        empresaList c= new empresaList();
        c.contratar("Gustavo", 10000);
        c.contratar("Caio", 12000);
        c.contratar("Matheus", 11000);

        c.mostrarTodos();
    }
}
