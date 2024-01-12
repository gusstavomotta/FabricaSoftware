package Loja.computadores;

import java.util.List;

public class Computador implements iConstantes {

    private static int contar_computadores;

    private double gb_memoria;
    private double clock_processador;
    private String idioma_teclado;
    private double polegada_monitor;

    public Computador(double gb_memoria, double clock_processador, String idioma_teclado, double polegada_monitor) {

        contar_computadores++;
        this.gb_memoria = gb_memoria;
        this.clock_processador = clock_processador;
        this.idioma_teclado = idioma_teclado;
        this.polegada_monitor = polegada_monitor;
        tamanhoMemoria(gb_memoria);

    }

    public static int getContar_computadores() {
        return contar_computadores;
    }

    public double getMemoria() {
        return gb_memoria;
    }

    public void setMemoria(double gb_memoria) {
        this.gb_memoria = gb_memoria;
    }

    public double getProcessador() {
        return clock_processador;
    }

    public void setProcessador(double clock_processador) {
        this.clock_processador = clock_processador;
    }

    public String getTeclado() {
        return idioma_teclado;
    }

    public void setTeclado(String idioma_teclado) {
        this.idioma_teclado = idioma_teclado;
    }

    public double getMonitor() {
        return polegada_monitor;
    }

    public void setMonitor(double polegada_monitor) {
        this.polegada_monitor = polegada_monitor;
    }

    public double tamanhoMemoria(double gigas) {

        return gb_memoria = (TAMANHO_MEMORIA * gigas);
    }

    public String toString() {

        return "Memória RAM: " + this.gb_memoria + " | Clock do Processador: " + this.clock_processador + " Ghz"
                + " | Idioma do Teclado: " + this.idioma_teclado + " | Tamanho polegada_monitor: "
                + this.polegada_monitor + " polegadas.";
    }
}
