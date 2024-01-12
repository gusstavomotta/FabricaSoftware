package modeloprova;

/**
 *
 * @author supti
 */
public class Apartamento extends Habitacao {

    private float areaSacada;
    private boolean elevador;
    private boolean churrasqueira;

    public Apartamento(float areaSacada, boolean elevador, boolean churrasqueira, float areaConstruida, int numQuartos, int numBanheiros, boolean garagem, EnumPiso tipoPiso) {
        super(areaConstruida, numQuartos, numBanheiros, garagem, tipoPiso);
        this.areaSacada = areaSacada;
        this.elevador = elevador;
        this.churrasqueira = churrasqueira;
    }

    public Apartamento() {
        super();
        this.areaSacada = 0;
        this.elevador = false;
        this.churrasqueira = false;
    }

    public float getAreaSacada() {
        return areaSacada;
    }

    public void setAreaSacada(float areaSacada) {
        this.areaSacada = areaSacada;
    }

    public boolean isElevador() {
        return elevador;
    }

    public void setElevador(boolean elevador) {
        this.elevador = elevador;
    }

    public boolean isChurrasqueira() {
        return churrasqueira;
    }

    public void setChurrasqueira(boolean churrasqueira) {
        this.churrasqueira = churrasqueira;
    }

    @Override
    public float retornarBaseCalculo() {
        return 20;
    }

    /**
     * Sobrecarga na subclasse, para retornar seus dados aproveitando o toString() da classe mãe.
     * @return String com todos os dados do apartamento
     */    
    @Override
    public String toString() {
        String ret = super.toString() + "\n";//reaproveitando o método da classe mãe
        
        //adicionando as características próprias do apartamento
        ret += String.format("Área de Sacada: %.2f m2\n", areaSacada);
        ret += "Com Elevador: " + (elevador ? "Sim\n" : "Não\n");
        ret += "Com Churrasqueira: " + (churrasqueira ? "Sim" : "Não");
        
        return ret;
    }

}
