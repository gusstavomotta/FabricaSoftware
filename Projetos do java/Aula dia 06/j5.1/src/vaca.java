public class vaca extends animais {

    // ATRIBUTO UNICO DA CLASSE
    private String pelo;

    // GETTERS E SETTERS
    public String getPelo() {
        return pelo;
    }

    public void setPelo(String pelo) {
        this.pelo = pelo;
    }

    // SOBREESCRENDO METODOS GERAIS
    @Override
    public void comer() {

        System.out.println("A vaca está comendo grama!");
    }

    @Override
    public void fazerBarulhos() {

        System.out.println("A vaca está mugindo!");
    }
    // METODOS DA CLASSE

    // UTILIZADO DO METODO GET PARA ACESSSAR A VARIÁVEL DA CLASSE MÃE
    public void peso() {

        System.out.println("A vaca pesa " + getPeso() + " kg");
    }

    public void pelo() {

        System.out.println("A vaca tem o pelo da cor " + pelo + "!");
    }
}
