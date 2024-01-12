public class aluno {

    int matricula;
    String nome;
    float prova1= 0;
    float prova2 = 0;
    float trab1 = 0;
    float ex1 = 0;
    float mediaGeral = 0;

    void calculaMedia() {

        mediaGeral = (prova1 + prova2 + trab1 + ex1)/4;
        
    }
}