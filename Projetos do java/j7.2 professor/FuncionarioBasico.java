package fs_ex_7_2;

/**
 *
 * @author supti
 */
public class FuncionarioBasico extends Funcionario {
    
    public FuncionarioBasico(IComissao tipoComissao){
        super(tipoComissao);
    }
    
    private String escola;

    public String getEscola() {
        return escola;
    }

    public void setEscola(String escola) {
        this.escola = escola;
    }
    
    
    @Override
    public float calcularSalario(){
        float sal = super.calcularSalario();//salário da classe mãe
        //return (sal * 10/100) + sal;
        return sal * 1.1f;//acrescido de 10%
    }
}
