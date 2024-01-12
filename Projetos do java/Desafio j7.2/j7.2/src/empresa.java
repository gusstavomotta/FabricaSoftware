import java.util.ArrayList;

public class empresa {

    private ArrayList<Funcionario> empresa = new ArrayList<>();

    public void contratar(Funcionario a) {

        empresa.add(a);
    }

    public void listaFuncionarios() {

        System.out.println("~~~~~~~~~~~~~~ Lista de Funcionários ~~~~~~~~~~~~~~");
        for (Funcionario a : empresa) {
            System.out.println(a);
        }
    }

    public void caclularCustoTotal() {

        double custoTotal = 0;

        for (Funcionario a : empresa) {
            custoTotal += a.getSalarioBase();
        }
        System.out.println("\nO custo total de todos os funcionarios é de: R$ " + custoTotal);
    }
}
