//Exercício do aluno Felipe Winkelmann Mueller ajustado 
//pelo Prof. Ivan para aula de encapuslamento

package exjava2.pkg2;
import java.util.Scanner;

public class ExJ22 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner dadosAluno = new Scanner(System.in);
        
        Aluno student;//declaração
        student = new Aluno(888); //instanciação
        //construção pois chama o CONSTRUTOR
        
        
        System.out.printf("Digite a matricula do aluno: ");
        student.setMatricula(dadosAluno.nextInt());
        System.out.printf("Digite o nome do aluno: ");
        student.nome = dadosAluno.next();
        System.out.printf("Insira a nota da primeira prova: ");
        student.setN_p1(dadosAluno.nextFloat());
        System.out.printf("Insira a nota da segunda prova: ");
        student.setN_p2(dadosAluno.nextFloat());
        System.out.printf("Insira a nota do trabalho: ");
        student.setN_trab(dadosAluno.nextFloat());
        System.out.printf("Insira a nota do exercicio: ");
        student.setN_ex(dadosAluno.nextFloat());
        
        student.calcula_media();
        
        System.out.printf("A media do aluno e: " + student.getMedia());
        
        dadosAluno.close();
        
    }
    
}
