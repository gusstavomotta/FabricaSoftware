package Vendas;

public class app {
    
    public static void main (String [] args){

        pedido p1 = new pedido();
        pedido p2 = new pedido();
        pedido p3 = new pedido();

        /* 
        System.out.println(p1.getIdPedido());
        System.out.println(p2.getIdPedido());
        System.out.println(p3.getIdPedido());
        */
        p2.adicionarItem("Coca cola", 2.0, 5.50);
        p2.adicionarItem("pao", 0.2, 1.0);
        p2.adicionarItem("queijo", 2.0, 3.0);
        p2.setValorDesconto(5);
        System.out.println(p2);
        
    }
}
