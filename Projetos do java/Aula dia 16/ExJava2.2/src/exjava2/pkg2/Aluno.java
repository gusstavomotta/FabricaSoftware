//Exercício do aluno Felipe Winkelmann Mueller ajustado 
//pelo Prof. Ivan para aula de encapuslamento
package exjava2.pkg2;

public class Aluno {
    
    public Aluno(int mat){
        
       matricula = mat;
       //inicializar os atributos
       n_p1 = 0;
       n_p2=0;
       n_trab=0;
       n_ex=0;
    }
    
    private int matricula;
    String nome;
    private float n_p1;
    private float n_p2;
    private float n_trab;
    private float n_ex;
    private float n_media;
    
    public void setMatricula(int mat){
        if(matricula>0 && matricula < 9999999)
            matricula = mat;
    }
    
    public float getMedia(){
        return n_media;
    }

    public void calcula_media(){
        n_media = (n_p1+n_p2+n_trab+n_ex)/4;        
    }

    public float getN_p1() {
        return n_p1;
    }

    public void setN_p1(float n_p1) {
        this.n_p1 = n_p1;
    }

    public float getN_p2() {
        return n_p2;
    }

    public void setN_p2(float n_p2) {
        this.n_p2 = n_p2;
    }

    public float getN_trab() {
        return n_trab;
    }

    public void setN_trab(float n_trab) {
        this.n_trab = n_trab;
    }

    public float getN_ex() {
        return n_ex;
    }

    public void setN_ex(float n_ex) {
        this.n_ex = n_ex;
    }
    public void mostra(){

        System.out.printf("Nome: ",nome);
    }
  
}   
