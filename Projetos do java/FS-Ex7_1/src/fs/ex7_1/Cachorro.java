package fs.ex7_1;

/**
 *
 * @author supti
 */
public class Cachorro extends Animal implements ICorredor {

    public void correr(){
        System.out.println("Cachorro correndo...");
    }
    
    @Override
    public void emitirSom() {
        System.out.println("Au, Au, Au");
    }
    
    
}
