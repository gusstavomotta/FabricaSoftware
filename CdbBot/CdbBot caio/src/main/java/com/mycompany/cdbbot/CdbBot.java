/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.cdbbot;

import java.util.List;

import org.telegram.telegrambots.meta.TelegramBotsApi;
import org.telegram.telegrambots.meta.exceptions.TelegramApiException;
import org.telegram.telegrambots.updatesreceivers.DefaultBotSession;

/**
 *
 * @author Gustavo Motta
 */
public class CdbBot {

    public static void main(String[] args) {
        // Main para executar o bot
        try {
            // Cria dois objetos sem argumentos apenas para chamar as funções
            CdbBotClass cdbBot = new CdbBotClass();
            Agenda a = new Agenda();
            // carrega as agendas
            List<Agenda> agendas = a.carregar_dados_agendas(); // Obtenha as agendas
            // filtra as agendas q ja passaram do prazo
            List<Agenda> expirados = a.obterLembretesExpirados(agendas);
            // envia essas agendas para os respectivos usuários com o aviso
            cdbBot.enviarLembretesExpirados(expirados);

            // Registra o bot
            TelegramBotsApi telegramBotsApi = new TelegramBotsApi(DefaultBotSession.class);
            telegramBotsApi.registerBot(new CdbBotClass());
        } catch (TelegramApiException e) {
            e.printStackTrace();
        }
    }

}
