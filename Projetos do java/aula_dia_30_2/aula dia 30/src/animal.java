public class animal {
    
    private double peso;
    protected String comida;

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }
    
    public String getComida() {
        return comida;
    }

    public void setComida(String comida) {
        this.comida = comida;
    }

    public void comer(){

        System.out.println("Animal comendo " + comida);
    }   

    public void dormir(){
        
        System.out.println("Animal dormindo!");
    }

    public void movimentar(){
        
        System.out.println("Animal andando!");
    }

    public void fazerBarulho(){
        
        System.out.println("Animal fazendo barulho...");
    }
}

