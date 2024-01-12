package fs_ex_7_2;

/**
 *
 * @author supti
 */
public class Funcionario {
    private int codigoFuncional;
    private String nome;
    private IComissao tipoComissao;
    
    public Funcionario(IComissao tipoComissao){
        this.tipoComissao = tipoComissao;
    }

    public int getCodigoFuncional() {
        return codigoFuncional;
    }

    public void setCodigoFuncional(int codigoFuncional) {
        this.codigoFuncional = codigoFuncional;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public float calcularSalario(){
        return 1000 + calcularComissao();
    }
    
    public float calcularComissao(){
        if(tipoComissao == null)
            return 0;
        else
            return tipoComissao.calcular();
    }
    
    @Override
    public String toString(){
        String ret = "Funcionario " + this.getNome();
        ret += String.format(" Comissão R$ %.2f", this.calcularComissao());
        ret += String.format(" Salário Total R$: %.2f", this.calcularSalario());
        
        return ret;
    }
}
