package fs.ex7_1;

import java.util.ArrayList;
import java.util.Random;

/**
 *
 * @author supti
 */
public class FSEx7_1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Cachorro c = new Cachorro();
        Preguica p = new Preguica();
        Cavalo cav = new Cavalo();      
        Animal a = new Cavalo();//polimorfismo de referência
        
        ArrayList<Animal> lst = new ArrayList<>();
        lst.add(c);
        lst.add(p);
        lst.add(cav);
        Veterinario v = new Veterinario();
        for (int i = 0; i < lst.size(); i++) {
            //lst.get(i).emitirSom();
            //v.examinar(lst.get(i));
        }
        
        
        //letra d;
        Zoologico zoo = new Zoologico();
        Random rnd = new Random();
        for (int i = 0; i < 10; i++) {
            int opcao = rnd.nextInt(3);//sorear um valor entre 0 e 2
            Animal animal;
            switch (opcao) {
                case 0:
                    animal = new Cachorro();
                    break;
                case 1:
                    animal = new Preguica();
                    break;
                default:
                    animal = new Cavalo();
            }
            
            zoo.adicionarAnimal(animal);//adicionar na 'jaula'
        }
        
        zoo.percorrerJaulas();
    }
    
}
