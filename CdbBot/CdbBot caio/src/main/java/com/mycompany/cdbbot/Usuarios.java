package com.mycompany.cdbbot;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

//classe usuarios com seus atributos/ getters e setters
public class Usuarios {

    private String nome;
    private Long chatId;
    private int intervalo_tempo;

    public Usuarios() {
    }

    // construtor
    public Usuarios(String nome, Long chatId, int intervalo_tempo) {
        this.nome = nome;
        this.chatId = chatId;
        this.intervalo_tempo = intervalo_tempo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Long getChatId() {
        return chatId;
    }

    public void setChatId(Long chatId) {
        this.chatId = chatId;
    }

    public int getIntervalo_tempo() {
        return intervalo_tempo;
    }

    public void setIntervalo_tempo(int intervalo_tempo) {
        this.intervalo_tempo = intervalo_tempo;
    }

    // método to string
    @Override
    public String toString() {
        String ret = "\nNome: " + nome + "\n";
        ret += "Chat ID: " + chatId + "\n";
        ret += "Intervalo de tempo para mostrar as notificações" + intervalo_tempo + "\n";

        return ret;
    }

    // função responsável por ler o arquivo csv de usuarios
    // recebe como parâmetro o caminho do arquivo
    public static List<Usuarios> readUsuariosFromCSV(String arquivo) {
        List<Usuarios> usuariosList = new ArrayList<>();
        // cria uma lista e ignora o cabeçalho caso tiver
        try (BufferedReader br = new BufferedReader(new FileReader(arquivo))) {
            String line;
            boolean headerSkipped = false;

            while ((line = br.readLine()) != null) {
                if (!headerSkipped) {
                    // Ignorar o cabeçalho
                    headerSkipped = true;
                    continue;
                }
                // faz a separação dos atributos lidos e associa a variáveis
                String[] linha = line.split(",");
                String nome = linha[0];
                Long chatId = Long.parseLong(linha[1]);
                int intervaloTempo = Integer.parseInt(linha[2]);
                // passa essas variáveis como parametro para criar o objeto usuario e add na
                // lista de usuarios
                Usuarios usuario = new Usuarios(nome, chatId, intervaloTempo);
                usuariosList.add(usuario);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        // retorna a lista de usuarios
        return usuariosList;
    }

    // carrega os dados dos usuarios, adiciona numa lista e retorna a lista de
    // usuarios
    public List<Usuarios> carregar_dados_usuarios() {
        String arquivo = "C:\\Users\\Gustavo Motta\\Desktop\\Python\\usuarios.csv";
        // Ler as agendas do arquivo CSV
        List<Usuarios> usuariosList = Usuarios.readUsuariosFromCSV(arquivo);

        return usuariosList;
    }

    // recebe a lista de usuarios e o chat id de quem está interagindo com o bot
    // percorre a lista comparando os chat ids da lista com o inserido e retorna o
    // intervalo de tempo respectivo do usuario
    public int get_intervalo_de_tempo(List<Usuarios> usuariosList, Long chatId) {
        for (Usuarios usuario : usuariosList) {
            if (usuario.getChatId().equals(chatId)) {
                return usuario.getIntervalo_tempo();
            }
        }

        return -1; // Valor padrão caso não seja encontrado
    }

}
