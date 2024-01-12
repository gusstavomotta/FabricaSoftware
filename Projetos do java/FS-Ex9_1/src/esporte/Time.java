package esporte;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 *
 * @author supti
 */
public class Time {
    private String nomeTime;
    private String tecnico;
    private List<Atleta> elenco;

    public Time(String nomeTime, String tecnico) {
        this.nomeTime = nomeTime;
        this.tecnico = tecnico;
        this.elenco = new LinkedList<>();
    }

    public String getNomeTime() {
        return nomeTime;
    }

    public String getTecnico() {
        return tecnico;
    }
    
    public void adicionarAtleta(Atleta a){
        this.elenco.add(a);
    }
    
    public void removerAtleta(Atleta a){
        this.elenco.remove(a);
    }
    
    public double calcularIdadeMedia(){
        double soma=0;
        for (int i = 0; i < elenco.size(); i++) {
            soma += elenco.get(i).getIdade();
        }
        
        return soma / elenco.size();
    }
}
