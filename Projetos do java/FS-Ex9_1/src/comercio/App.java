package comercio;

/**
 *
 * @author supti
 */
public class App {
    public static void main(String arg[]){
        Pedido p1 = new Pedido();
        Pedido p2 = new Pedido();

        p2.adicionarItem("Coca-cola", 2, 6.5);
        p2.adicionarItem("Pão frances", 0.2, 10);
        p2.adicionarItem("Café", 1, 10);
        p2.setValorDesconto(1);
        
        System.out.println(p2);
        
    }
}
