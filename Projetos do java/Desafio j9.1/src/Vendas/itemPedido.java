package Vendas;

public class itemPedido {
    
    private int idItem;
    private String descricao;
    private double quantidade;
    private double valor;
    
    public itemPedido(int idItem, String descricao, double quantidade, double valor) {
        this.idItem = idItem;
        this.descricao = descricao;
        this.quantidade = quantidade;
        this.valor = valor;
    }
    public int getIdItem() {
        return idItem;
    }

    public String getDescricao() {
        return descricao;
    }

    public double getQuantidade() {
        return quantidade;
    }

    public double getValor() {
        return valor;
    }

    public double calcularSubTotal(){

        return this.valor * this.quantidade;
    }
    @Override
    public String toString() {
        String ret = String.format("%d: %s -> %.1f * R$%.2f = R$%.2f"
                , this.idItem, this.descricao, this.quantidade, this.valor, this.calcularSubTotal());
        
        return ret;
    }
}
