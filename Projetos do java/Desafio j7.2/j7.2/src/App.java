public class App {
    public static void main(String[] args) throws Exception {

        basico a1 = new basico("Gustavo", 10, "São pedro");
        basico a2 = new basico("Matheus", 20, "Marista");
        basico a3 = new basico("Leonardo", 30, "Barão");
        basico a4 = new basico("Pedro", 40, "Ulbra");
        Medio a5 = new Medio("Melissa", 50, "Totem");
        Medio a6 = new Medio("Carol", 60, "Imaculada");
        Medio a7 = new Medio("Pâmela", 70, "Diva");
        Medio a8 = new Medio("Eduarda", 80, "Borges");
        universidade a9 = new universidade("Caio", 90, "Unisc");
        universidade a10 = new universidade("Victor", 100, "Ufsm");

        empresa empresa = new empresa();
        empresa.contratar(a1);
        empresa.contratar(a2);
        empresa.contratar(a3);
        empresa.contratar(a4);
        empresa.contratar(a5);
        empresa.contratar(a6);
        empresa.contratar(a7);
        empresa.contratar(a8);
        empresa.contratar(a9);
        empresa.contratar(a10);
        empresa.listaFuncionarios();
        empresa.caclularCustoTotal();
    }
}
