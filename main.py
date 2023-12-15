from decouple import config
import telebot
import time
import traceback
import textwrap
import subprocess
import signal
import os

BOT_TOKEN = config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Men Python botman. Python kodni yuboring, men uni bajarib natijani chiqaraman.")

@bot.message_handler(commands=['start', 'help'])
def on_command_received(message):
    send_welcome(message)

def run_python_code(message):
    code = message.text
    user_code = message.text.replace('“', '"').replace('”', '"').replace('’', "'")
    highlighted_code = f"```\n{textwrap.shorten(user_code, width=200)}\n```"
    try:
        start_time = time.time()
        process = subprocess.Popen(["python", "-c", user_code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, preexec_fn=os.setsid)
        output, error = process.communicate(timeout=10)
        end_time = time.time()
        execution_time = end_time - start_time

        if error:
            bot.reply_to(message, f"**Xatolik:**\n```\n{error}\n```", parse_mode='Markdown')
        else:
            reply_message = (
                f"**Natija:**\n```\n{output}\n```\n"
                f"**Bajarish vaqti:** `{execution_time} sekund`\n"
                f"**Kiritilgan kod:**\n\n{highlighted_code}"
            )
            bot.reply_to(message, reply_message, parse_mode='Markdown')
        
    except subprocess.TimeoutExpired:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        bot.reply_to(message, "**Xatolik:** Bajarish vaqt limiti tugirolmadi. Kodni qisqa qilishni urinib ko'ring.", parse_mode='Markdown')
    except Exception as e:
        error_message = traceback.format_exc()
        print(f"Error occurred: {error_message}")
        bot.reply_to(message, "**Xatolik:** Dasturda xatolik yuz berdi. Iltimos, dasturni tekshirib ko'ring.", parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    run_python_code(message)

try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"Bot polling error: {e}")
finally:
    bot.stop_polling()
