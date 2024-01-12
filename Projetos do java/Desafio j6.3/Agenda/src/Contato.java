
// CLASSE COM OS ATRIBUTOS DE UM CONTATO
public class Contato {

    private String nome;
    private String endereço;
    private String email;
    private int telefone;

    // CONSTRUTOR
    public Contato(String nome, String endereço, String email, int telefone) {

        this.nome = nome;
        this.endereço = endereço;
        this.email = email;
        this.telefone = telefone;

    }

    // GETTERS E SETTERS
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEndereço() {
        return endereço;
    }

    public void setEndereço(String endereço) {
        this.endereço = endereço;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getTelefone() {
        return telefone;
    }

    public void setTelefone(int telefone) {
        this.telefone = telefone;
    }

    // MÉTODO TO STRING
    public String toString() {

        return "Nome: " + nome + " /Endereço: " + endereço + " /Email: " + email + " /Telefone: " + telefone;
    }
}