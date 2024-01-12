package Esporte;

import java.util.ArrayList;
import java.util.List;

public class Time {
    
    private String nomeTime;
    private String tecnico;
    private List<Atleta> elenco;

    public Time(String nomeTime, String tecnico) {
        this.nomeTime = nomeTime;
        this.tecnico = tecnico;
        this.elenco = new ArrayList<>();
    }
    
    public String getNomeTime() {
        return nomeTime;
    }
    public void setNomeTime(String nomeTime) {
        this.nomeTime = nomeTime;
    }
    public String getTecnico() {
        return tecnico;
    }
    public void setTecnico(String tecnico) {
        this.tecnico = tecnico;
    }

    public void adicionarAleta(Atleta a){
        this.elenco.add(a);
        
    }
    public void removerAtleta(Atleta a){
        this.elenco.remove(a);
    }

    public double calcularMediaIdade(){

        double soma = 0;
        for( int i = 0; i < elenco.size(); i++){
 
            soma += elenco.get(i).getIdade();
        }
        return soma / elenco.size();

    }

}
