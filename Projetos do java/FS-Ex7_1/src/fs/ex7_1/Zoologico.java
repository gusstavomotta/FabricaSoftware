package fs.ex7_1;

import java.util.ArrayList;

/**
 *
 * @author supti
 */
public class Zoologico {
    private ArrayList<Animal> jaulas = new ArrayList<>();
    
    public void adicionarAnimal(Animal a){
        jaulas.add(a);
    }
    
    public void percorrerJaulas(){
        for (int i = 0; i < jaulas.size(); i++) {
            Animal a = jaulas.get(i);//'pegando' o animal da posição i
            a.emitirSom();
            
            /*if(a.getClass().equals(Cachorro.class)){
                 ((Cachorro) a).correr();
            }*/
            /*if(a instanceof Cachorro){
                ((Cachorro) a).correr();
            }
            else if(a instanceof Cavalo){
                Cavalo c = (Cavalo)a;
                c.correr();
            }*/
            
            if(a instanceof ICorredor){
                ICorredor corredor = (ICorredor)a;//CAST
                corredor.correr();
            }
        }
    }
}
