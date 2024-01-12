package modeloprova;

/**
 *
 * @author supti
 */
public class Kitinete extends Habitacao {

    public Kitinete() {
        super();
    }

    public Kitinete(float areaConstruida, int numQuartos, int numBanheiros, boolean garagem, EnumPiso tipoPiso) {
        super(areaConstruida, numQuartos, numBanheiros, garagem, tipoPiso);
    }

    @Override
    public float retornarBaseCalculo() {
        return 10;
    }

    /**
     * Sobrecarga na subclasse, para retornar seus dados aproveitando o
     * toString() da classe mãe.
     *
     * @return String com todos os dados da Kitinete (nesse caso é tudo da
     * classe Habitação)
     */
    @Override
    public String toString() {
        return super.toString();
    }
}
