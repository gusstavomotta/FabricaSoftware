package modeloprova;

/**
 *
 * @author supti
 */
public class Casa extends Habitacao {

    private float areaPatio;
    private String cor;
    private boolean piscina;

    public Casa(float areaPatio, String cor, boolean piscina, float areaConstruida, int numQuartos, int numBanheiros, boolean garagem, EnumPiso tipoPiso) {
        super(areaConstruida, numQuartos, numBanheiros, garagem, tipoPiso);
        this.areaPatio = areaPatio;
        this.cor = cor;
        this.piscina = piscina;
    }

    public Casa() {
        super();
        this.areaPatio = 0;
        this.cor = "";
        this.piscina = false;
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

    public boolean isPiscina() {
        return piscina;
    }

    public void setPiscina(boolean piscina) {
        this.piscina = piscina;
    }


    /**
     * Sobrecarga na subclasse, para retornar seus dados aproveitando o
     * toString() da classe mãe.
     *
     * @return String com todos os dados da casa
     */
    @Override
    public String toString() {
        String ret = super.toString() + "\n";//reaproveitando o método da classe mãe

        //adicionando as características próprias da casa
        ret += String.format("Área de Pátio: %.2f m2\n", areaPatio);
        ret += "Cor: " + cor + "\n";
        ret += "Com Piscina: " + (piscina ? "Sim" : "Não");

        return ret;
    }

    @Override
    public float retornarBaseCalculo() {
        return 30;
    }

}
