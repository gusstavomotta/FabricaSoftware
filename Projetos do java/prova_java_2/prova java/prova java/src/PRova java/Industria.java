public class Industria extends Empresa implements IPI{

    //criando enumerador
    public enum EIndustria { PRODUCAO, INTERMEDIARIA, CONSUMO}
    // criando atributo do tipo eindustria
    private EIndustria tipoIndustria;
    
    public EIndustria getTipoIndustria() {
        return tipoIndustria;
    }

    public Industria(String cnpj, String nome, String endereco, Industria.EIndustria tipoIndustria) {
        super(cnpj, nome, endereco);
        this.tipoIndustria = tipoIndustria;
    }

    @Override
    public double calcularIPI(double base) {
       
        return base * PERCENTUAL_IPI/100;
    }

    @Override
    public String toString(){

        
        String ret = super.toString();
        ret += "Tipo do comércio: " + tipoIndustria;
        return ret;
        
    }
    
}


/*
 * public class Industria extends Empresa implements IPI{
    
    private tipoIndustria industria;

    public Industria(String cnpj, String nome, String endereco, tipoIndustria industria) {
        super(cnpj, nome, endereco);
        this.industria = industria;
    }

    public tipoIndustria getIndustria() {
        return industria;
    }

    public void setIndustria(tipoIndustria industria) {
        this.industria = industria;
    }
    
    public String toString(){

        String ret = super.toString();
        ret +=  "Tipo da industria: " + industria+ "\n";
        return ret;

    }
 
    @Override
    public double calcularIPI(double base){

        return base * PERCENTUAL_IPI/100;
    }
    
}

 * 
 */
