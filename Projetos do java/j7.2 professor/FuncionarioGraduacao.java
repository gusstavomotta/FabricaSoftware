package fs_ex_7_2;

/**
 *
 * @author supti
 */
public class FuncionarioGraduacao extends FuncionarioMedio {
    
    public FuncionarioGraduacao(IComissao tipoComissao){
        super(tipoComissao);
    }       
    
    private String universidade;

    public String getUniversidade() {
        return universidade;
    }

    public void setUniversidade(String universidade) {
        this.universidade = universidade;
    }

    @Override
    public float calcularSalario() {
        return super.calcularSalario() * 2;//salário do nível médio acrescido de 100%
    }
    
    
}
