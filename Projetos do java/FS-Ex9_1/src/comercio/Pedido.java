package comercio;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 *
 * @author supti
 */
public class Pedido {
    private static int contadorPedidos=0;
    private int idPedido;
    private Date data;
    private double valorDesconto;
    private List<ItemPedido> itens;

    public Pedido() {
        contadorPedidos++;
        this.idPedido = contadorPedidos;
        this.data = new Date();
        this.valorDesconto=0;
        this.itens = new ArrayList<>();
    }

    public int getIdPedido() {
        return idPedido;
    }

    public Date getData() {
        return data;
    }

    public double getValorDesconto() {
        return valorDesconto;
    }
    
    /**
     * insere um novo produto na lista de itens 
     * controlando automaticamente o ID
     * @param descricao
     * @param qtde
     * @param valor 
     */
    public void adicionarItem(String descricao, double qtde, double valor){
        ItemPedido i = new ItemPedido(this.itens.size()+1, descricao, qtde, valor);
        this.itens.add(i);
    } 
    
    /**
     * percorre a lista de itens, obtem o valor total e diminui o desconto.
     * @return o Total a pagar
     */
    public double totalizarPedido(){
        double total=0;
        for (int i = 0; i < itens.size(); i++) {
            total += itens.get(i).calcularSubTotal();
        }
        
        return total - this.valorDesconto;
    }
    
    @Override
    public String toString(){
        String ret = String.format("Pedido nº %d Dia %s\n", this.idPedido, this.data);
        ret += "---------------------------\n";
        for (int i = 0; i < itens.size(); i++) {
            ret += itens.get(i).toString() + "\n";            
        }
        ret += "---------------------------\n";
        ret += String.format("Desconto de R$ %.2f\n", this.valorDesconto);
        ret += "---------------------------\n";
        ret += String.format("Total a pagar R$ %.2f", this.totalizarPedido());
        return ret;
    }

    public void setValorDesconto(double valorDesconto) {
        this.valorDesconto = valorDesconto;
    }
    
}
