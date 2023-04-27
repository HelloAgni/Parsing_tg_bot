import os
import signal

import msg
from dotenv import load_dotenv
from parsing_thread import main_parsing
from table_to_db import check_table_and_insert_data
from telegram import ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from validators import check_file

load_dotenv()

TOKEN = os.getenv('TOKEN')

app = Application.builder().token(token=TOKEN).build()


async def my_file(update, context):
    """
    Проверка расширения файла.
    Получение имени и указание пути для загрузки.
    Провека состояние таблицы и валидация.
    """
    chat = update.effective_chat
    doc = await context.bot.get_file(update.message.document)
    file_path = check_file(doc=doc)
    if file_path:
        await doc.download_to_drive(custom_path=file_path)
        report = check_table_and_insert_data(file_path=file_path)
        if isinstance(report, str):
            await context.bot.send_message(
                chat_id=chat.id,
                text=report
            )
        elif isinstance(report, dict):
            await context.bot.send_message(
                chat_id=chat.id,
                text=msg.msg_upload(report['table'])
            )
            try:
                result, pars_time = main_parsing(file=file_path)
                await context.bot.send_message(
                    chat_id=chat.id,
                    text=f'{result}{msg.msg_time_pars()}{pars_time}c.')
            except Exception as er:
                await context.bot.send_message(
                    chat_id=chat.id,
                    text=f'{msg.msg_tolong_pars()} {er}')
    else:
        await context.bot.send_message(
            chat_id=chat.id,
            text=msg.msg_file_check_error()
            )


async def wake_up(update, context):
    """
    Активация Бота и приветствие команда /start.
    """
    chat = update.effective_chat
    name = update.message.chat.first_name
    await context.bot.send_message(
        chat_id=chat.id,
        text=msg.msg_hi(name=name))


async def bot_break(update, context):
    """
    Остановка бота из чата комманда /stop.
    """
    remove_button = ReplyKeyboardRemove()
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id,
                                   text=msg.msg_stop(),
                                   reply_markup=remove_button)
    os.kill(os.getpid(), signal.SIGINT)


if __name__ == '__main__':
    app.add_handler(CommandHandler('start', wake_up))
    app.add_handler(CommandHandler('stop', bot_break))
    app.add_handler(MessageHandler(filters.Document.ALL, my_file))
    app.run_polling()
