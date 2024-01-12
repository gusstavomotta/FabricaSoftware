package modeloprova;

/**
 *
 * @author supti
 */
public abstract class Habitacao implements IPTU {

    private float areaConstruida;
    private int numQuartos;
    private int numBanheiros;
    private boolean garagem;
    private EnumPiso tipoPiso;

    //Construtor com argumentos
    public Habitacao(float areaConstruida, int numQuartos, int numBanheiros, boolean garagem, EnumPiso tipoPiso) {
        this.areaConstruida = areaConstruida;
        this.numQuartos = numQuartos;
        this.numBanheiros = numBanheiros;
        this.garagem = garagem;
        this.tipoPiso = tipoPiso;
    }

    /**
     * Construtor sem argumentos
     */
    public Habitacao() {
        this.areaConstruida = 0;
        this.numQuartos = 0;
        this.numBanheiros = 0;
        this.garagem = false;
        this.tipoPiso = EnumPiso.CERAMICO;
    }

    public float getAreaConstruida() {
        return areaConstruida;
    }

    public void setAreaConstruida(float areaConstruida) {
        this.areaConstruida = areaConstruida;
    }

    public int getNumQuartos() {
        return numQuartos;
    }

    public void setNumQuartos(int numQuartos) {
        this.numQuartos = numQuartos;
    }

    public int getNumBanheiros() {
        return numBanheiros;
    }

    public EnumPiso getTipoPiso() {
        return tipoPiso;
    }

    public void setTipoPiso(EnumPiso tipoPiso) {
        this.tipoPiso = tipoPiso;
    }

    public void setNumBanheiros(int numBanheiros) {
        this.numBanheiros = numBanheiros;
    }

    public boolean isGaragem() {
        return garagem;
    }

    public void setGaragem(boolean garagem) {
        this.garagem = garagem;
    }

    @Override
    public String toString() {
        String ret = String.format("Área Construida: %.2f m2\n", areaConstruida);
        ret += String.format("Nº Quartos: %d\n", numQuartos);
        ret += String.format("Nº Banheiros: %d\n", numBanheiros);
        ret += "Com Garagem: " + (garagem ? "Sim\n" : "Não\n");
        ret += "Tipo de Piso: " + tipoPiso.toString();

        return ret;
    }
    
    public float calcularIPTU(){
        return this.areaConstruida * retornarBaseCalculo();
    }

}
