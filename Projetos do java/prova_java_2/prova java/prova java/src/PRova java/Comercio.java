public class Comercio extends Empresa{

    //definindo enumerador
    public enum EComercio {ATACADO, VAREJO}
    //declarando um atributo do tipo ( tipo comercio )
    private EComercio tipoComercio;
    
    public EComercio getTipoComercio() {
        return tipoComercio;
    }

    public Comercio(String cnpj, String nome, String endereco, Comercio.EComercio tipoComercio) {
        super(cnpj, nome, endereco);
        this.tipoComercio = tipoComercio;
    }

    @Override
    public String toString(){

        String ret = super.toString();
        ret += "Tipo do comércio: " + tipoComercio;
        return ret;
    }

}




/* 
 * public class Comercio extends Empresa{
    
    private tipoComercio comercio;

    public Comercio(String cnpj, String nome, String endereco, tipoComercio comercio) {
        super(cnpj, nome, endereco);
        this.comercio = comercio;
    }

    public tipoComercio getComercio() {
        return comercio;
    }

    public void setComercio(tipoComercio comercio) {
        this.comercio = comercio;
    }

    @Override
    public String toString(){

        String ret = super.toString();
        ret +=  "Tipo do comércio: " + comercio+ "\n";
        return ret;
    }

}
*/

