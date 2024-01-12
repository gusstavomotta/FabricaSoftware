package comercio;

/**
 *
 * @author supti
 */
public class ItemPedido {
    private int idItem;
    private String descricao;
    private double quantidade;
    private double valorUnitario;

    public ItemPedido(int idItem, String descricao, double quantidade, double valorUnitario) {
        this.idItem = idItem;
        this.descricao = descricao;
        this.quantidade = quantidade;
        this.valorUnitario = valorUnitario;
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

    public double getValorUnitario() {
        return valorUnitario;
    }
    
    /**
     * Multiplica a quantidade pelo preço unitário
     * @return o resultado
     */
    public double calcularSubTotal(){
        return this.quantidade * this.valorUnitario;
    }

    @Override
    public String toString() {
        String ret = String.format("%d: %s -> %.1f * R$%.2f = R$%.2f"
                , this.idItem, this.descricao, this.quantidade, this.valorUnitario, this.calcularSubTotal());
        
        return ret;
    }
    
    
}
