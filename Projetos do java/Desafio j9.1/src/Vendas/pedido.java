package Vendas;
import java.util.Date;
import java.util.ArrayList;
import java.util.List;

public class pedido{

    private static int contadorPedidos = 0;
    private int idPedido;
    private Date data;
    private double valorDesconto;
    private List<itemPedido> itens;

    public pedido() {

        contadorPedidos++;
        this.idPedido = contadorPedidos;
        this.data = new Date();
        this.valorDesconto = 0;
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

    public void setValorDesconto(double valorDesconto) {
        this.valorDesconto = valorDesconto;
    }

    public void adicionarItem(String descricao, Double quantidade, Double valor){

        itemPedido i = new itemPedido(this.itens.size()+1, descricao, quantidade, valor);
        this.itens.add(i);

    }
    
    public double totalizarPedido(){

        double soma = 0;
        for ( int i = 0; i < itens.size(); i ++){
            soma += itens.get(i).calcularSubTotal();

        }
        return soma - this.valorDesconto;
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

    
}