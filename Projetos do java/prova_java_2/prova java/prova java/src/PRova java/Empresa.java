public class Empresa implements ICMS{
    
    private String cnpj;
    private String nome;
    private String endereco;
    private double totalImpostos;
    private double totalVendas;


    public String getCnpj() {
        return cnpj;
    }

    public String getNome() {
        return nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public double getTotalImpostos() {
        return totalImpostos;
    }

    public double getTotalVendas() {
        return totalVendas;
    }

    public Empresa(String cnpj, String nome, String endereco) {
        this.cnpj = cnpj;
        this.nome = nome;
        this.endereco = endereco;
        
    }

    public void efetuarVenda(int Quantidade, double valorUnitario){

        double precoFinal = Quantidade * valorUnitario;
        totalVendas += precoFinal;

        if( this instanceof IPI )
            totalImpostos += ((IPI)this).calcularIPI(precoFinal);

        totalImpostos += calcularICMS(precoFinal);

    }

    @Override
    public double calcularICMS(double base) {
        
        return base * PERCENTUAL_ICMS/100;
    }

    @Override
    public String toString() {
        return "Empresa [cnpj=" + cnpj + ", nome=" + nome + ", endereco=" + endereco + ", totalImpostos="
                + totalImpostos + ", totalVendas=" + totalVendas + "]";
    }



    
}

/* public class Empresa implements ICMS{
    
    private String cnpj;
    private String nome;
    private String endereco;
    private static double totalImpostos;
    private static double totalVendas ;

    public Empresa(String cnpj, String nome, String endereco) {
        this.cnpj = cnpj;
        this.nome = nome;
        this.endereco = endereco;
        this.totalImpostos = 0;
        this.totalVendas = 0;
       
    }

    public String getCnpj() {
        return cnpj;
    }

    public void setCnpj(String cnpj) {
        this.cnpj = cnpj;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }


    public double getTotalImpostos() {
        return totalImpostos;
    }

    public double getTotalVendas() {
        return totalVendas;
    }

    public void efetuarVenda(int quantidade, double valorUnitario){

        
    }

    @Override
    public String toString() {
       
        String ret = "CNPJ: " + this.cnpj + "\n";
        ret += "Nome: " + this.nome + "\n";
        ret += "Endereco: " + this.endereco + "\n";
        return ret;
    }
    
    public double calcularICMS(double base){

        return base * PERCENTUAL_ICMS/100;
    }

}*/

