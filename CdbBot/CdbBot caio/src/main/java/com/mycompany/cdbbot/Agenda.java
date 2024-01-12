package com.mycompany.cdbbot;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

//classe agenda com seus atributos/ getters e setters
public class Agenda {

    private LocalDateTime dataHora;
    private String tipo;
    private String descricao;
    private List<Long> participantes;
    private List<String> recursos;

    public LocalDateTime getDataHora() {
        return dataHora;
    }

    public void setDataHora(LocalDateTime dataHora) {
        this.dataHora = dataHora;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public List<Long> getParticipantes() {
        return participantes;
    }

    public void setParticipantes(List<Long> participantes) {
        this.participantes = participantes;
    }

    public List<String> getRecursos() {
        return recursos;
    }

    public void setRecursos(List<String> recursos) {
        this.recursos = recursos;
    }

    public Agenda() {
    }

    // construtor
    public Agenda(LocalDateTime dataHora, String tipo, String descricao, List<Long> participantes,
            List<String> recursos) {
        this.dataHora = dataHora;
        this.tipo = tipo;
        this.descricao = descricao;
        this.participantes = participantes;
        this.recursos = recursos;
    }

    // método toString
    @Override
    public String toString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy - HH:mm");
        String ret = "\nData e hora: " + dataHora.format(formatter) + "\n";
        ret += "Tipo: " + tipo + "\n";
        ret += "Descrição: " + descricao + "\n";
        ret += "Participantes: " + participantes.toString().replaceAll("\\[|\\]", "") + "\n";
        ret += "Recursos: " + recursos.toString().replaceAll("\\[|\\]", "") + "\n";
        return ret;
    }

    // função para retirar caracteres indesejados
    private static List<Long> parseParticipantes(String participantesStr) {
        // essa função foi criada pois em python os participantes e recursos são salvos
        // em uma lista
        // por conta disso no csv esses atributos ficam salvos com colchetes
        // essa função é responsável por remover esses colchetes
        participantesStr = participantesStr.replaceAll("\\[|\\]", "");
        String[] participantesArr = participantesStr.split(",");

        List<Long> participantes = new ArrayList<>();
        for (String participante : participantesArr) {
            participantes.add(Long.parseLong(participante.trim()));
        }

        return participantes;
    }

    // função para retirar caracteres indesejados
    private static List<String> parseRecursos(String recursosStr) {
        // essa função foi criada pois em python os participantes e recursos são salvos
        // em uma lista
        // por conta disso no csv esses atributos ficam salvos com colchetes
        // essa função é responsável por remover esses colchetes
        recursosStr = recursosStr.replaceAll("\\[|\\]", "");
        String[] recursosArr = recursosStr.split(",");

        List<String> recursos = new ArrayList<>();
        for (String recurso : recursosArr) {
            recursos.add(recurso.trim());
        }

        return recursos;
    }

    // funçao para ler o csv das agendas, recebe o caminho do csv como argumento
    public static List<Agenda> retornar_agendas_do_csv(String arquivo) {
        List<Agenda> agendaList = new ArrayList<>();
        // cria uma lista e ignora o cabeçalho caso houver
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
                String[] data = line.split(",");
                String dataStr = data[0];
                String horaStr = data[1];
                String tipo = data[2];
                String descricao = data[3];
                String participantesStr = data[4];
                String recursosStr = data[5];
                // faz o format da data e realiza a "limpeza" dos atributos "participantes" e
                // "recursos"
                LocalDateTime dataHora = LocalDateTime.parse(dataStr + " " + horaStr,
                        DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm"));
                List<Long> participantes = parseParticipantes(participantesStr);
                List<String> recursos = parseRecursos(recursosStr);
                // cria o objeto com os atributos passados e add na lista de agendas
                Agenda agenda = new Agenda(dataHora, tipo, descricao, participantes, recursos);
                agendaList.add(agenda);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        // retorna a lista com as agendas
        return agendaList;
    }

    // carrega os dados das agendas, adiciona na lista e retorna lista com as
    // agendas
    public List<Agenda> carregar_dados_agendas() {
        String arquivo = "C:\\Users\\Gustavo Motta\\Desktop\\Python\\agendas.csv";
        // Ler as agendas do arquivo CSV
        List<Agenda> agendaList = Agenda.retornar_agendas_do_csv(arquivo);

        return agendaList;
    }

    // recebe a lista de agendas e o chat id do usuario que está interagindo
    // percorre a lista e separa todas as agendas que o usuário tem após a data
    // atual e add na lista
    public List<Agenda> buscar_agendas_por_id(List<Agenda> agendaList, Long chatId) {
        List<Agenda> agendasEncontradas = new ArrayList<>();
        LocalDateTime dataAtual = LocalDateTime.now();

        for (Agenda agenda : agendaList) {
            if (agenda.getParticipantes().contains(chatId) && agenda.getDataHora().isAfter(dataAtual)) {
                agendasEncontradas.add(agenda);
            }
        }
        // retorna a lista das agendas vpaldias
        return agendasEncontradas;
    }

    // recebe como parametro a lista de agendas do usuario, o chat id de quem está
    // interagindo e o intevalo de tempo que o usuario informou no cadastro
    public List<Agenda> separar_agendas_prox_x_horas(List<Agenda> agendaList, Long chatId,
            int intervalo) {
        // cria uma lista para os compromissos
        List<Agenda> compromissosProximasHoras = new ArrayList<>();
        // pega a data atual e seta uma data limite a partir da atual + o intervalo de
        // tempo do usuario
        LocalDateTime now = LocalDateTime.now();
        LocalDateTime limite = now.plusHours(intervalo);
        // percorre a lista de agendas do usuario verifica as datas de todas as agendas
        // caso for depois da data atual e antes da data limite o programa adiciona na
        // lista de compromisso nas proximas x horas
        for (Agenda agenda : agendaList) {
            if (agenda.getDataHora().isAfter(now) && agenda.getDataHora().isBefore(limite)) {
                compromissosProximasHoras.add(agenda);
            }
        }
        // retorna a lista com esses compromissos
        return compromissosProximasHoras;
    }

    // recebe como parametro uma lista de agendas
    // essa função realiza a separação dos lembretes que ja passaram da data
    public List<Agenda> obterLembretesExpirados(List<Agenda> agendaList) {
        LocalDateTime dataAtual = LocalDateTime.now();
        List<Agenda> lembretesExpirados = new ArrayList<>();
        // pega a data atual, cria uma lista, percorre essa lista e compara a hora atual
        // com a hora do lembrete
        for (Agenda agenda : agendaList) {
            LocalDateTime dataHora = agenda.getDataHora();
            // se a hora for menor ou igual a data atual a agenda é colcoada naa lsita
            if (dataHora.isBefore(dataAtual)) {
                lembretesExpirados.add(agenda);
            }
        }
        // retorna a lista das agendas expiradas
        return lembretesExpirados;
    }

}
