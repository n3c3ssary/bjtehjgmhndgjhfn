# Импортируем модули  
import telebot  
import requests  
  
# Указываем токен   
bot = telebot.TeleBot('<ваш токен>')  
  
# Обработчик команды Start  
@bot.message_handler(commands=['start'])  
def start_message(message):  
    bot.send_message(message.chat.id, 'Введите номер телефона для поиска аккаунта телеграмм')  
  
# Обработчик ввода номера телефона  
@bot.message_handler(content_types=['text'])  
def send_text(message):  
    # Запрос для поиска пользователя  
    url = 'https://api.telegram.org/bot<ваш токен>/getUserByPhone' + 'phone_number=' + message.text  
    response = requests.get(url).json()  
      
    # Проверка существования пользователя  
    if 'message' in response:  
        bot.send_message(message.chat.id, 'Аккаунт телеграмм не найден')  
    else:  
        user = response['result']  
        bot.send_message(message.chat.id, 'Указанный аккаунт был найден:\n\n' +  
                         'ID пользователя: ' + str(user['id']) + '\n\n' +  
                         'Имя пользователя: ' + user['first_name'])  
  
# Запуск бота  
bot.polling()
