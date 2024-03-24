import telebot
from telebot import types

bot = telebot.TeleBot('7063169730:AAFByWs8LY-judRFN-u5s4MiObFyVdxkLRY')

def vibor_cs_go (message):
    bot.send_message(message.chat.id, "это вызывается функция для cs_go (будут кнопки, старосты и т д)")
def vibor_Dota2 (message):
    bot.send_message(message.chat.id, "это вызывается функция для Dota2 (будут кнопки, старосты и т д)")
    start(message)
def vibor_LOL (message):
    bot.send_message(message.chat.id, "это вызывается функция для LOL'a (будут кнопки, старосты и т д)")
    start(message)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, новичок! ВСТУПИТЕЛЬНАЯ ИНФА ТУТ + КАРТИНКИ")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Sections")
    item2 = types.KeyboardButton("FAQ")
    item3 = types.KeyboardButton("Список админов")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Что тебя интересует?", reply_markup=markup)



#Command /start
@bot.message_handler(commands=['main'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Sections")
    item2 = types.KeyboardButton("FAQ")
    item3 = types.KeyboardButton("Список админов")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Привет!", reply_markup=markup)

#Bottom 1
@bot.message_handler(func=lambda message: message.text == "FAQ")
def FAQ(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("В главное меню")
    markup.add(item1)
    bot.send_message(message.chat.id, "Вот основная инфа про CyberCluBBB RSMU", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "В главное меню")
def returning_to_main(message):
    main(message)


@bot.message_handler(func=lambda message: message.text == "Список админов")
def admins(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("В главное меню")
    markup.add(item1)
    bot.send_message(message.chat.id, "Список наших дорогих руководителей", reply_markup=markup)

@bot.message_handler(commands=['main'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Sections")
    item2 = types.KeyboardButton("FAQ")
    item3 = types.KeyboardButton("Список админов")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Привет!", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Sections")
def main_sections(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='CS GO 2', callback_data='cs_go_2')
    btn2 = types.InlineKeyboardButton(text='Mobile Legends', callback_data='mobile_legends')
    btn3 = types.InlineKeyboardButton(text='Dota2', callback_data='dota2')
    btn4 = types.InlineKeyboardButton(text='Apex', callback_data='apex')
    btn_back = types.InlineKeyboardButton(text='Назад', callback_data='назад')
    markup.add(btn1,btn2,btn3,btn4,btn_back)
    bot.send_photo(message.chat.id, open('cyberclub.jpg', 'rb'),
                       reply_markup=types.ReplyKeyboardRemove())
    #bot.send_message(message.chat.id, text="Окей, посмотрим...", reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id, 'Выбери секцию', reply_markup=markup)



@bot.callback_query_handler(func=lambda callback: callback.data)
def check_section(callback):
    if callback.data == 'cs_go_2':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='К списку секций', callback_data='sections')
        btn2 = types.InlineKeyboardButton(text='В главное меню', callback_data='main_menu')
        kb.add(btn1,btn2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="""Инфа про клуб Cs Go2\n Забавный факт:
                              Сколько времени? В среднем, один раунд в CS:GO длится всего 1 минуту 55 секунд. Это означает, что полная игра из 30 раундов длится чуть менее часа!""", reply_markup=kb)

    if callback.data == 'dota2':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='К списку секций', callback_data='sections')
        btn2 = types.InlineKeyboardButton(text='В главное меню', callback_data='main_menu')
        kb.add(btn1,btn2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="""Инфа про клуб Dota2 \n Забавный факт:
                              Рекордсмены! Самая продолжительная игра в истории Dota 2 длилась 6 часов 18 минут!""", reply_markup=kb)

    if callback.data == 'mobile_legends':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='К списку секций', callback_data='sections')
        btn2 = types.InlineKeyboardButton(text='В главное меню', callback_data='main_menu')
        kb.add(btn1,btn2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="""Инфа про Mobile Legends\n Забавный факт:
                              Кто самый популярный? Самым популярным героем в игре является «Милаш», которого выбирают около 7% игроков""", reply_markup=kb)

    if callback.data == 'apex':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='К списку секций', callback_data='sections')
        btn2 = types.InlineKeyboardButton(text='В главное меню', callback_data='main_menu')
        kb.add(btn1,btn2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="""Инфа про клуб Apex \n Забавный факт:
                              Рекордные 10 миллионов игроков за первые 72 часа! Игра Apex Legends установила рекорд по количеству игроков за первые 72 часа после релиза.""", reply_markup=kb)

    if callback.data == 'sections':
        #bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="Интересуешься чем-то ещё?", )
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='CS GO 2', callback_data='cs_go_2')
        btn2 = types.InlineKeyboardButton(text='Mobile Legends', callback_data='mobile_legends')
        btn3 = types.InlineKeyboardButton(text='Dota2', callback_data='dota2')
        btn4 = types.InlineKeyboardButton(text='Apex', callback_data='apex')
        btn_back = types.InlineKeyboardButton(text='Назад', callback_data='назад')
        markup.add(btn1,btn2,btn3,btn4,btn_back)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="Выбери секцию", reply_markup=markup )
        bot.edit_message_media(chat_id=callback.message.chat.id, message_id=callback.message.id, media="cyberclub.jpg")

    if callback.data == 'main_menu' or callback.data == 'назад':
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="Вернёмся к началу...", )
        main(callback.message)

#Start bot
if __name__ == '__main__':
    bot.polling(none_stop=True)