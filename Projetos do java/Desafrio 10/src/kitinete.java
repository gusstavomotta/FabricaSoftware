
public class kitinete extends Habitacao{
    
    public kitinete(){
        super();

    }
    public kitinete(float areaConstruida, int numQuartos, int numBanheiros, boolean garagem, enumPiso tipoPiso){

        super(areaConstruida, numQuartos, numBanheiros,garagem, tipoPiso);
    }

    @Override
    public float retornarBaseCalculo() {
        return 10;
    }

    @Override
    public String toString() {
        return super.toString();
    }
    
    
}
