package fs_ex_7_2;

/**
 *
 * @author supti
 */
public class FuncionarioMedio extends FuncionarioBasico {
    
    public FuncionarioMedio(IComissao tipoComissao){
        super(tipoComissao);
    }    

    @Override
    public float calcularSalario() {
        return super.calcularSalario() * 1.5f;//salário da classe inferior acrescido de 50%
    }
    
}
