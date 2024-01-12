import java.util.Scanner;

public class media {

    aluno a1 = new aluno();

    public static void main(String[] args) {

        aluno a1 = new aluno();

        Scanner scanner = new Scanner(System.in);
        System.out.printf("Digite a matrícula do aluno: ");
        a1.matricula = scanner.nextInt();
        System.out.printf("Digite o nome do aluno: ");
        a1.nome = scanner.next();
        System.out.printf("Insira as notas do aluno: ");
        a1.prova1 = scanner.nextFloat();
        a1.prova2 = scanner.nextFloat();
        a1.trab1 = scanner.nextFloat();
        a1.ex1 = scanner.nextFloat();

        scanner.close();

        a1.calculaMedia();
        System.out.println("Média geral do aluno " + a1.nome + " foi: " + a1.mediaGeral + " pontos.");
    }

}