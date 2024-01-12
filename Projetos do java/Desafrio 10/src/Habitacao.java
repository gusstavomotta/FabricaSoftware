public abstract class Habitacao implements IPTU{
    
    private float areaConstruida;
    private int numQuartos;
    private int numBanheiros;
    private boolean garagem;
    private enumPiso tipoPiso;
    
    public Habitacao(float areaConstruida, int numQuartos, int numBanheiros, boolean garagem, enumPiso tipoPiso) {
        this.areaConstruida = areaConstruida;
        this.numQuartos = numQuartos;
        this.numBanheiros = numBanheiros;
        this.garagem = garagem;
        this.tipoPiso = tipoPiso;
    }

    public Habitacao() {
        this.areaConstruida = 0;
        this.numQuartos = 0;
        this.numBanheiros = 0;
        this.garagem = false;
        this.tipoPiso = enumPiso.CERAMICO;

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
    public void setNumBanheiros(int numBanheiros) {
        this.numBanheiros = numBanheiros;
    }
    public boolean isGaragem() {
        return garagem;
    }
    public void setGaragem(boolean garagem) {
        this.garagem = garagem;
    }
    public enumPiso getTipoPiso() {
        return tipoPiso;
    }
    public void setTipoPiso(enumPiso tipoPiso) {
        this.tipoPiso = tipoPiso;
    }

    public float calcularIptu(){

        return this.areaConstruida * retornarBaseCalculo();
    }
    public String toString(){

        String ret = "Área construída: " + this.areaConstruida + "\n";
        ret += "Número de quartos: " + this.numQuartos + "\n";
        ret += "Número de banheiros: " + this.numBanheiros + "\n";
        ret += "Possui garagem?: " + (garagem ? "Sim\n" : "Não\n");
        ret += "Tipo do piso: " + this.tipoPiso.toString() + "\n";
        return  ret;
    }

}
