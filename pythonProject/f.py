import telebot
token='5848100454:AAGK0zxpgE6lpT2-rFKre5PnXYXZx1TQaPs'
bot=telebot.TeleBot(token)
def my_func():
    print('я работаю!')


def my_decorator(func_to_decorate):
    def decorated_func():
        print('Я начинаю работать')
        func_to_decorate()
        print('Я все сделал')
    return decorated_func

@my_decorator
def my_func():
    print('Я работаю')

my_func()
