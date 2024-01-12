package fs_ex_7_2;

import java.util.ArrayList;

/**
 *
 * @author supti
 */
public class FS_Ex_7_2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        /*Funcionario f = new FuncionarioGraduacao();
        float sal = f.calcularSalario();
        System.out.println("Salário: " + sal);*/
        
        ArrayList<Funcionario> lst = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            lst.add(new FuncionarioBasico(null));
        }
        

        lst.add(new FuncionarioMedio(new ComissaoGerente()));
        lst.add(new FuncionarioMedio(new ComissaoVendedor()));
        lst.add(new FuncionarioMedio(new ComissaoVendedor()));
        lst.add(new FuncionarioMedio(new ComissaoVendedor()));
    
        
        lst.add(new FuncionarioGraduacao(new ComissaoSupervisor()));
        lst.add(new FuncionarioGraduacao(new ComissaoSupervisor()));
        
        //calculando os custos da empresa
        float custoGeral=0;
        float custoEscBasico=0;
        float custoEscMedio=0;
        float custoEscGraducao=0;
        for (int i = 0; i < lst.size(); i++) {
            Funcionario f = lst.get(i);
            custoGeral += f.calcularSalario();
            
            if(f instanceof FuncionarioBasico)
                custoEscBasico += f.calcularSalario();
            
            if(f instanceof FuncionarioMedio)
                custoEscMedio += f.calcularSalario();  
            
            if(f instanceof FuncionarioGraduacao)
                custoEscGraducao += f.calcularSalario(); 
            
            System.out.println(f.toString());
        }
        
        System.out.printf("Custo total R$ %.2f\n", custoGeral);
        System.out.printf("Custo Nível Básico R$ %.2f\n", custoEscBasico);
        System.out.printf("Custo Nível Médio R$ %.2f\n", custoEscMedio);
        System.out.printf("Custo Nível Graduação R$ %.2f\n", custoEscGraducao);
    }
    
}
