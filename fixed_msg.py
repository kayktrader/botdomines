import telebot

# Insira aqui o seu token do Telegram Bot
TOKEN = '5992692637:AAFNI31G_CnY06FPfsDpoT9oz5rfCiWRB8Y'
bot = telebot.TeleBot(TOKEN)

link = "<a href='https://shre.ink/QwD5'>CADASTRE-SE AQUI</a>"

# Mensagem que será enviada
mensagem = f'🆘🆘 ATENÇÃO 🆘🆘\n\n⚠️ NOSSOS SINAIS SÓ FUNCIONA NA GREEN BETS ⚠️\n\nTEM MUITAS PESSOAS QUE ESTÃO TOMANDO RED PORQUE ESTÃO JOGANDO EM OUTRA CASA!\n\n🚨 NOSSOS SINAIS SÓ FUNCIONAM NA GREEN BETS🚨\n\n ✍️ {link}\n\n CADASTRE-SE E COMECE A PEGAR OS GREEEENS'

# Cria o botão
botao = telebot.types.InlineKeyboardButton(text='R$ 500,00 🎁', url='https://shre.ink/QwD5')

# Cria o objeto de teclado inline e adiciona o botão
teclado_inline = telebot.types.InlineKeyboardMarkup()
teclado_inline.add(botao)

chat_id = '-1001909314682'
# Envia a mensagem com o botão
mensagem_enviada = bot.send_message(chat_id=chat_id, text=mensagem, reply_markup=teclado_inline, parse_mode='html')

# Fixa a mensagem no chat
bot.pin_chat_message(chat_id=chat_id, message_id=mensagem_enviada.message_id)
