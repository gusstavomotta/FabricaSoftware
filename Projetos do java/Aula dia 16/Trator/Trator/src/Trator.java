import java.util.Scanner;

public class Trator {

    public Trator(String marca) {

        marcaTrator = marca;
        marcha = 0;
    }

    public String cor;
    private String marcaTrator;
    private int marcha;
    protected String revisado;
    protected boolean ligado = false;

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public String getMarcaTrator() {
        return marcaTrator;
    }

    public void setMarcaTrator(String marcaTrator) {
        this.marcaTrator = marcaTrator;
    }

    public int getMarcha() {
        if (ligado = true) {
            if (marcha > 0 && marcha <= 3)
                return marcha;
        }
        return marcha = 0;
    }

    public void setMarcha(int marcha) {
        this.marcha = marcha;
    }

    public String getRevisao() {
        return revisado;
    }

    public void ligar() {

        if (ligado == true) {
            System.out.println("\nO trator já está ligado!");
        } else {
            System.out.println("\nDando partida...");
            System.out.printf("Marcha atual: " + marcha + "\n");
            ligado = true;
        }
    }

    public void andar() {
        if (ligado != true) {
            System.out.println("\nO trator precisa ser ligado!\n");
        } else {
            System.out.println("Engatando primeira marcha...");
            System.out.println("\nTrator em movimento!");
            marcha = 1;
            System.out.printf("Marcha atual: " + getMarcha() + "\n");
        }
    }

    public void subirMarcha() {

        if (marcha == 3) {
            System.out.println("\nNão há mais marchas pra engatar!");
            System.out.printf("Marcha atual: " + getMarcha() + "\n");
            marcha = 3;
        } else if (marcha >= 0 || marcha <= 3) {
            System.out.println("\nSubindo marcha...");
            marcha += 1;
            System.out.printf("Marcha atual: " + getMarcha() + "\n");
        }
    }

    public void reduzirMarcha() {

        if (marcha == 0) {
            System.out.println("\nNão há como reduzir mais marchas!\n");
            marcha = 0;
        } else if (marcha >= 1 || marcha <= 3) {
            System.out.println("\nReduzindo a marcha...");
            marcha -= 1;
            System.out.printf("Marcha atual: " + getMarcha() + "\n");
        }
    }

    public void desligar() {

        if (ligado == false)
            System.out.println("\nO trator já está desligado");
        else {
            System.out.println("\nDesligando trator...\n");
            ligado = false;
        }
    }

    public void mostrarInfo() {

        System.out.println("~~~~~~~~INFORMAÇÕES GERAIS~~~~~~~~");
        System.out.println("Marca: " + marcaTrator);
        System.out.println("Cor: " + cor);
        System.out.println("Revisado: " + revisado);
    }

    public void entradaDados() {

        Scanner sc = new Scanner(System.in);

        boolean validacao = false;

        while (!validacao) {
            System.out.print("Informe a marca do trator: (Massey / Jhon Deere / Stara): ");
            marcaTrator = sc.nextLine();

            if (marcaTrator.equals("Massey") || marcaTrator.equals("Jhon Deere") || marcaTrator.equals("Stara"))
                validacao = true;
            else
                validacao = false;
        }
        boolean validacao2 = false;

        while (!validacao2) {

            System.out.print("Insira a cor: (Vermelho/ Verde/ Laranja): ");
            cor = sc.next();
            if (cor.equals("Vermelho") || cor.equals("Verde") || cor.equals("Laranja"))
                validacao2 = true;

            else
                validacao2 = false;

        }
        boolean validacao3 = false;

        while (!validacao3) {

            System.out.print("Foi realizada a revisão?: ");
            revisado = sc.next();

            if (revisado.equals("S") || revisado.equals("s") || revisado.equals("sim") || revisado.equals("Sim"))
                validacao3 = true;
            else if (revisado.equals("N") || revisado.equals("n") || revisado.equals("nao") || revisado.equals("não")|| revisado.equals("Não"))
                validacao3 = true;
            else
                validacao3 = false;
        }

    }
}