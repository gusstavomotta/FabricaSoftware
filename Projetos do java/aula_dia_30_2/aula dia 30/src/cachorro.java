public class cachorro extends animal{
    
    public void enterrar(){

        System.out.println("Enterrando osso...");
    }

    @Override
    public void fazerBarulho(){

        super.fazerBarulho();
        System.out.println("AU AU AU AU AU");
    }
}
