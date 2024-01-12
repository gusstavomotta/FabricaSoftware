public class coruja extends ave{
    
    @Override
    public void fazerBarulho(){

        super.fazerBarulho();
        System.out.println("UH UH UH UH");
    }
    @Override
    public void comer(){

        System.out.println("Coruja comendo " + comida);
    }
}
