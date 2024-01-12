package com.mycompany.cdbbot;

// IMPORTS QUE UTILIZAMOS NAS FUNÇÕES 
import java.text.SimpleDateFormat;
import java.util.Date;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import com.opencsv.CSVReader;
// IMPORTS DO TELEGRAMBOTS 
import org.telegram.telegrambots.meta.api.objects.Message;
import org.telegram.telegrambots.bots.TelegramLongPollingBot;
import org.telegram.telegrambots.meta.api.methods.send.SendMessage;
import org.telegram.telegrambots.meta.api.objects.Update;
import org.telegram.telegrambots.meta.exceptions.TelegramApiException;

public class CdbBotClass extends TelegramLongPollingBot {
    // seta o caminho do arquivo do faq
    // é utilizado na função lerArquivoCsv
    private static final String csv_arquivo = "C:\\Users\\Gustavo Motta\\Desktop\\CdbBot caio\\faq.csv";
    // criando dois objetos para chamar as funções de cada classe
    Usuarios u = new Usuarios();
    Agenda a = new Agenda();

    @Override
    public String getBotUsername() {
        return "Cdb BOT";
    }

    @Override
    public String getBotToken() {
        return "6108894788:AAGcKx9K7qiz_gBADuuUgYtb5QTmtU0dndY";
    }

    @Override
    public void onUpdateReceived(Update update) {
        if (update.hasMessage() && update.getMessage().hasText()) {
            SendMessage message = responder_mensagem(update);
            try {
                execute(message);
            } catch (TelegramApiException e) {
                e.printStackTrace();
            }
        }
    }

    public void enviarMensagem(Long chatId, String mensagem) {
        SendMessage sendMessage = new SendMessage();
        sendMessage.setChatId(String.valueOf(chatId));
        sendMessage.setText(mensagem);

        try {
            execute(sendMessage); // Chamada correta do método execute
        } catch (TelegramApiException e) {
            e.printStackTrace();
        }
    }

    // Função que gera uma reposta com base na pergunta do usuario
    private SendMessage responder_mensagem(Update update) {
        if (update.hasMessage()) {
            // recebe a mensagem, armazena o chat id, armazena o texto da mensagem e seta a
            // resposta vazia
            Message message = update.getMessage();
            Long chatId = message.getChatId();
            String pergunta = message.getText();
            String resposta = "";
            // A variavel resposta chama a função get resposta que recebe com oarqgumento a
            // pergunta o chat id do usuario
            resposta = retorna_resposta(pergunta, chatId);
            SendMessage sendMessage = new SendMessage();
            sendMessage.setChatId(String.valueOf(message.getChatId())); // Converte o chat id para string
            sendMessage.setText(resposta);
            System.out.println(chatId);
            // envia a mensagem
            return sendMessage;
        }

        return null;
    }

    // Get resposta retorna a resposta do que o usuário perguntar, recebe a pergunta
    // o id como parametro
    private String retorna_resposta(String pergunta, Long chatId) {
        String resposta = "";
        // recebe a pergunta e passa tudo para ,minúsculo
        pergunta = pergunta.toLowerCase();
        // a partir daqui são feitas verificações com base em palavras chaves
        // caso a mensagem conter algumas dessas strings a resposta adequada será
        // retornada
        // exemplo: se a pergunta conter /comandos a resposta será os comandos que o bot
        // consegue responder_mensagem
        if (pergunta.contains("/comandos")) {
            resposta = "Comandos disponíveis:\nMinhas agendas\n/Faq\nData\nHora";

        } else if (pergunta.contains("faq")) {
            resposta = menu_faq();

        } else if (pergunta.contains("data")) {
            resposta = getData();

        } else if (pergunta.contains("hora")) {
            resposta = getHora();

            // a partir daqui caso alguma pergunta conter essas Strings chave o programa
            // envia a pergunta para a função que retorna a resposta correspondete no faq
        } else if (pergunta.contains("pilares da") || pergunta.contains("da orientacao a ob")
                || pergunta.contains("da orientaçao a ob") || pergunta.contains("da orientação a ob")) {
            // o programa "arruma" a pergunta para se adequar às perguntas que estão no
            // faq.txt
            // depois passa como argumento para o get_resposta_faq e retorna a resposta
            // isso é feito para todas as perguntas do faq
            pergunta = "Quais são os pilares da orientação a objetos?";
            return get_resposta_faq(pergunta);

        } else if (pergunta.contains("quem sou eu") || pergunta.contains("quem sou") || pergunta.contains("sou eu")) {
            pergunta = "Quem sou eu?";
            return get_resposta_faq(pergunta);

        } else if (pergunta.contains("orientada a objetos") || pergunta.contains("o que e")
                || pergunta.contains("o que é")) {
            pergunta = "O que é programação orientada a objetos?";
            return get_resposta_faq(pergunta);

        } else if (pergunta.contains("heran") || pergunta.contains("a que serve")) {
            pergunta = "Para que serve herança?";
            return get_resposta_faq(pergunta);

        } else if (pergunta.contains("encapsulamento") || pergunta.contains("utilizar")
                || pergunta.contains("ar encapsulam")) {
            pergunta = "Por que utilizar encapsulamento?";
            return get_resposta_faq(pergunta);

        } else if (pergunta.contains("capital do brasil")) {
            pergunta = "Qual a capital do brasil?";
            return get_resposta_faq(pergunta);

            // caso o usuário quiser ver suas agendas o programa executa as seguintes
            // operações
        } else if (pergunta.contains("minhas agendas") || pergunta.contains("agendas")) {
            // Carrega os dados das agendas, os dados dos usuarios
            List<Agenda> agendas = a.carregar_dados_agendas();
            List<Usuarios> usuarios = u.carregar_dados_usuarios();
            // com base na lista de usuarios e o chatId de quem envia a mensagem o programa
            // pega o intervalo de tempo cadastrado
            int intervalo_tempo = u.get_intervalo_de_tempo(usuarios, chatId);
            // realiza a busca das agendas passando a lista de agendas e o chat id, todas
            // agendas com o chat id passado sao armazenadas e printadas
            List<Agenda> agendasDoUsuario = a.buscar_agendas_por_id(agendas, chatId);
            // realiza a busca nas agendas por usuario e retorna apenas as agendas que estão
            // dentro do intervalo de tempo especificado
            List<Agenda> compromissosXHoras = a.separar_agendas_prox_x_horas(agendasDoUsuario, chatId,
                    intervalo_tempo);
            // realiza os prints
            resposta = "Essa é toda sua programação:\n";
            for (Agenda agenda : agendasDoUsuario) {
                resposta += agenda.toString();
            }
            resposta += "\nEssa é sua programação para as próximas " + intervalo_tempo + " horas:" + "\n";
            for (Agenda agenda : compromissosXHoras) {
                resposta += agenda.toString();
            }
        } else {
            resposta = "Comando inválido, digite /comandos!";
        }

        return resposta;
    }

    private String get_resposta_faq(String pergunta) {
        // carrega os dados do faq em um map
        Map<String, String> data = carregar_dados_faq();
        // Retorna a resposta correspondente à pergunta, ou uma mensagem padrão caso não
        // haja resposta
        return data.getOrDefault(pergunta, "Desculpe, não tenho uma resposta para essa pergunta.");
    }

    private Map<String, String> carregar_dados_faq() {
        // Cria um Map para armazenar as perguntas e respostas
        Map<String, String> data = new HashMap<>();
        try (CSVReader reader = new CSVReader(new FileReader(csv_arquivo))) {
            String[] nextLine;
            // le as linhas do csv
            while ((nextLine = reader.readNext()) != null) {
                // verifica se a linha contém exatamente 2 elementos /pergunta e resposta
                if (nextLine.length == 2) {
                    String question = nextLine[0];
                    String answer = nextLine[1];
                    // Adiciona a pergunta e resposta ao Map

                    data.put(question, answer);
                }
            }
        } catch (IOException e) {

            e.printStackTrace();
        }

        // Retorna o Map com as informações
        return data;
    }

    // função pegar a data atual e retornar
    private String getData() {
        var formatter = new SimpleDateFormat("dd/MM/yyyy");
        return "A data atual é: " + formatter.format(new Date());
    }

    // função pegar a hora atual e retornar
    private String getHora() {
        var formatter = new SimpleDateFormat("HH:mm:ss");
        return "A hora atual é: " + formatter.format(new Date());
    }

    // menu com as opções do faq
    public static String menu_faq() {
        String ret = "O bot responde a essas opções:\n";
        ret += "O que é programação orientada a objetos?\n";
        ret += "Quais são os pilares da orientação a objetos?\n";
        ret += "Para que serve herança?\n";
        ret += "Por que utilizar encapsulamento?\n";
        ret += "Quem sou eu?\n";
        ret += "Qual é a capital do Brasil?\n";

        return ret;
    }

    // recebe a lista de lembretes expirados como argumento
    public void enviarLembretesExpirados(List<Agenda> agendaList) {
        // percorre essa lista, pega o chat id do participantes atrelado e add numa
        // lista de participantes
        for (Agenda agenda : agendaList) {
            List<Long> participantes = agenda.getParticipantes();
            // percorre a lista de participantes e envia a mensagem para o id do
            // participantes + a agenda q expirou
            for (Long participante : participantes) {
                String mensagem = "Agenda expirou:\n" + agenda.toString();
                enviarMensagem(participante, mensagem);
            }
        }
    }
}
