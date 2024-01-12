public class Apartamento extends Habitacao{
    
    private float areaSacada;
    private boolean elevador;
    private boolean churrasqueira;
    
    public Apartamento(float areaConstruida, int numQuartos, int numBanheiros, boolean garagem, enumPiso tipoPiso,
            float areaSacada, boolean elevador, boolean churrasqueira) {
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
    public String toString(){

        String ret = super.toString();
        ret += "Área de sacada: " + this.areaSacada + "\n";
        ret += "Possui elevador?: " + (elevador? "Sim\n" : "Não\n") ;
        ret += "Possui churrasqueira?: " + (churrasqueira? "Sim\n" : "Não\n");
        return ret;
    }

}
