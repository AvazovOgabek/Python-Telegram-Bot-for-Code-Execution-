# Telegram Python Bot

This Python script demonstrates a Telegram bot that allows users to execute Python code snippets. The bot takes Python code as input from users and provides the output after execution.

## Prerequisites

To run this bot, you need:
- Python 3.x installed on your system
- Install required libraries using pip:
  ```bash
  pip install pyTelegramBotAPI
  pip install python-decouple
  ```

## Usage
Get your Telegram Bot API token from @BotFather and replace 'YOUR_BOT_TOKEN' in the code with your actual bot token.

## Run the script by executing:

```bash
python main.py
```
## Features
- `/start` or `/help`: Displays a welcome message.
- `/execute`: Executes the Python code sent by the user and displays the output.
- Handles exceptions like timeout errors and invalid code input.
## Code Explanation
The script uses the `python-telegram-bot` library to create a Telegram bot.
Upon receiving commands `/start` or `/help`, it sends a welcome message.
The run_python_code function takes Python code from users, executes it, and sends the output.
It handles exceptions like timeouts and errors during code execution.
The script continuously polls for incoming messages using `bot.polling()`.
Security Considerations
Executing user-provided code can be a security risk. Ensure to run this script in a safe environment or use sandboxing techniques to mitigate potential risks.
Contributing
Contributions are welcome! If you have suggestions, improvements, or feature additions, feel free to create an issue or pull request.

## Disclaimer
This script is for educational purposes. Use it responsibly and avoid executing untrusted code.


Make sure to replace `'YOUR_BOT_TOKEN'` with your actual bot token in the code before using it. Also, consider adding more details or sections to the README as per your project's specific requirements or functionalities.

---

# Telegram Python boti

Ushbu Python skripti foydalanuvchilarga Python kod parchalarini bajarishga imkon beruvchi Telegram botini namoyish etadi. Bot foydalanuvchilardan kirish sifatida Python kodini oladi va bajarilgandan so'ng chiqishni ta'minlaydi.

## Old shartlar

Ushbu botni ishga tushirish uchun sizga kerak bo'ladi:
- Python 3.x tizimingizda o'rnatilgan
- Pip yordamida kerakli kutubxonalarni o'rnating:
   ``` bash

    pip install pyTelegramBotAPI
    pip install python-decouple
   ```

## Foydalanish
`@BotFather`dan Telegram Bot API tokenini oling va koddagi “YOUR_BOT_TOKEN” ni haqiqiy bot tokeni bilan almashtiring.

## Skriptni bajarish orqali ishga tushiring:

``` bash
python main.py
```
## Xususiyatlari
- `/start` yoki `/help`: Xush kelibsiz xabarni ko`rsatadi.
- `/execute`: foydalanuvchi tomonidan yuborilgan Python kodini bajaradi va natijani ko'rsatadi.
- Vaqt tugashi xatolari va yaroqsiz kod kiritish kabi istisnolarni boshqaradi.
## Kod tushuntirishi
Skript Telegram botini yaratish uchun “python-telegram-bot” kutubxonasidan foydalanadi.
`/start` yoki `/help` buyruqlarini olgach, u salomlash xabarini yuboradi.
run_python_code funksiyasi foydalanuvchilardan Python kodini oladi, uni bajaradi va natijani yuboradi.
U kodni bajarish vaqtidagi kutish vaqti va xatolar kabi istisnolarni hal qiladi.
Skript `bot.polling()` yordamida kiruvchi xabarlarni doimiy ravishda so'raydi.
Xavfsizlik masalalari
Foydalanuvchi tomonidan taqdim etilgan kodni bajarish xavfsizlik xavfi bo'lishi mumkin. Ushbu skriptni xavfsiz muhitda ishga tushirishga ishonch hosil qiling yoki potentsial xavflarni kamaytirish uchun sandboxing usullaridan foydalaning.
Hissa
Hissalar qabul qilinadi! Agar sizda takliflar, yaxshilanishlar yoki qo'shimchalar bo'lsa, muammo yarating yoki so'rovni oling.

## Rad etish
Ushbu skript ta'lim maqsadlarida. Undan mas'uliyat bilan foydalaning va ishonchsiz kodni bajarishdan qoching.


Uni ishlatishdan oldin koddagi "YOUR_BOT_TOKEN" ni haqiqiy bot tokeningiz bilan almashtirganingizga ishonch hosil qiling. Shuningdek, loyihangizning o'ziga xos talablari yoki funksiyalariga ko'ra README ga qo'shimcha tafsilotlar yoki bo'limlarni qo'shishni o'ylab ko'ring.
​
