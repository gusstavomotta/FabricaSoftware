public class Casa extends Habitacao{
    
    private float areaPatio;
    private String cor;
    private boolean piscina;

    
    public Casa(float areaConstruida, int numQuartos, int numBanheiros, boolean garagem, enumPiso tipoPiso,
            float areaPatio, String cor, boolean piscina) {
        super(areaConstruida, numQuartos, numBanheiros, garagem, tipoPiso);
        this.areaPatio = areaPatio;
        this.cor = cor;
        this.piscina = piscina;
    }
    public Casa(){

        this.areaPatio = 0;
        this.cor = "";
        this.piscina = false;

    }

    public boolean isPiscina() {
        return piscina;
    }
    public void setPiscina(boolean piscina) {
        this.piscina = piscina;
    }
    public float getAreaPatio() {
        return areaPatio;
    }
    public void setAreaPatio(float areaPatio) {
        this.areaPatio = areaPatio;
    }
    public String getCor() {
        return cor;
    }
    public void setCor(String cor) {
        this.cor = cor;
    }
    
    @Override
    public String toString(){
    String ret = super.toString();
    ret += "Área do pátio: " + this.areaPatio + "\n";
    ret += "Cor da casa: " + this.cor + "\n";
    ret += "Possui piscina?: " + (piscina ? "Sim\n" : "Não\n") ;
    return ret;
}
    @Override
    public float retornarBaseCalculo(){

        return 30;
    }
    
}
