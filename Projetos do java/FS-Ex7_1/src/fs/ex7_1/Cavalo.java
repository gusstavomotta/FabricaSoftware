package fs.ex7_1;

/**
 *
 * @author supti
 */
public class Cavalo extends Animal implements ICorredor {
    public void correr(){
        System.out.println("Cavalo correndo...");
    }
    
    @Override
    public void emitirSom(){
        System.out.println("Pocotó!");
    }
}
