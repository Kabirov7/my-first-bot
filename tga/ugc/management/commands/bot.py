from django.core.management.base import BaseCommand
from django.conf import settings
import telebot
from .output.films import filmss
from .output.netflix import netflix
from .output.serials import serials
from telebot import types


def log_errors(f):

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:

            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e
    return inner()

class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        #1- Правильное подключение
        bot = telebot.TeleBot(settings.TOKEN)
        print(bot.get_me())

        @bot.message_handler(commands=['start'])
        def start(message):
            send_mess = f"<b> Вулканский салют, {message.from_user.first_name}!!!</b>\n" \
                        f"Я бот 🤖<b>Мандо</b>🤖! Мои создатели <a href='https://www.instagram.com/renat.kab/'><b>@kabir.off</b></a> и <a href='https://www.instagram.com/renat.kab/'><b>@renat.kab</b></a>.\n" \
                        f"Я много блуждал во вселенной в поисках лучших фильмов и сериалов📹.\n Мне удалось собрать базу данных в которой всё только самое лучшее🥇\n" \
                        f"Я могу помочь тебе с выбором.\n" \
                        f"Нажми сюда /choose "
            bot.send_message(message.chat.id, send_mess, parse_mode='html')

        @bot.message_handler(commands=['choose'])
        def choose(message):
            send_mess = f'Выбери что ты будешь смотреть🤖🤖🤖'

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton('cinema')
            # btn2 = types.KeyboardButton('serials')
            btn3 = types.KeyboardButton('netflix')
            markup.add(btn1, btn3)
            bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def mess(message):
            get_message_bot = message.text.strip().lower()
            final_message = ''

            if get_message_bot == 'cinema':
                final_message = 'Я нашёл эти фильмы в дальнем парсеке, а потом <b>я- цыган😎🤗</b>'
                for i in range(5):
                    films_ = filmss()
                    fl = films_.output()
                    bot.send_message(message.chat.id, fl, parse_mode='html')

            # elif get_message_bot == 'serials':
            #     final_message = 'Не зря я взорвал <b>"Звезду Смерти"</b>🔫 что бы добыть эти данные, никому не говори про них😐😐😐'
            #     for i in range(5):
            #         serials_ = serials()
            #         sl = serials_.output()
            #         bot.send_message(message.chat.id, sl, parse_mode='html')

            elif get_message_bot == 'netflix':
                final_message = "Я охотился за сериалами netlfix'a <b>сотни тысяч миллионов триллиардов световых лет🤓</b>\n Cпрячь их глубоко под подушкой😘✨😘✨😘"
                for i in range(5):
                    netflix_ = netflix()
                    nx = netflix_.output()
                    bot.send_message(message.chat.id, nx, parse_mode='html')

            else:
                final_message = 'В моей базе все существующие языки во вселенной, и твой не похож не на один! Что ты такое???🤖🤖🤖'

            bot.send_message(message.chat.id, final_message, parse_mode='html')
            final_message = 'Захочешь что-то посмотреть, жми сюда /choose, и выбирай из кнопок ниже\n'
            bot.send_message(message.chat.id, final_message, parse_mode='html')

        bot.polling(none_stop=True)