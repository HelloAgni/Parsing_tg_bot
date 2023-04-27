# Parsing_tg_bot

## Simple Telegram Bot for parsing average price of goods
Функции Телеграм Бота (python-telegram-bot 20.2):  
- Загрузить Excel файл из чата (образец прикреплен внизу описания)
- Открыть файл проверить расширение, если все хорошо - сохранить
- Провести проверку полей таблицы (pandas)
- Сохранить данные в db.slite и сообщить пользователю о результате
- Обработать данные из таблицы и сообщить среднюю цену товара (selenium threading)  
***How to start***  
```bash
# Клонируем проект и переходим в него
git clone <project>
cd <project>
```
```bash
# Устанавливаем окружение и активируем
python -m venv venv
. venv/Scripts/activate  # Windows
. venv/bin/activate  # Linux
python -m pip install --upgrade pip
# Устанавливаем зависимости
pip install -r requirements.txt
# Создаем своего ТГ Бота
Создать бота через помощника - @BotFather (get TOKEN)
Получить токен
# в директории проекта создать файл .env
# образец Токена в файле .env.example
touch .env
# вставить в файл .env полученный Токен в формате:
TOKEN=9999999:aaa................
# После установки зависимостей и создания бота + файла .env
# Запускаем Бота
# Первый запуск займет больше времени, будут установлены драйверы
python bot/bot.py
```
**Telegram Bot**
```bash
# Активация бота из телеграм чата
/start
# Прикрепляем файл - если все хорошо URL и Xpath прошли проверку
Бот присылает результат
# Бота можно системно остановить из телеграм чата
/stop
```
Образец Exel файла доступен по ссылке:  
https://github.com/HelloAgni/Parsing_tg_bot/blob/main/xpath.xlsx  
После загрузки файл открыть с помощью Excel редактора.