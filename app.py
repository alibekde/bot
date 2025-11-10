from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime, timedelta
import os
TOKEN = os.getenv("TOKEN")

# 🔹 Dars jadvali
schedule = {
    "Dushanba": [
        "1. Kelajak soati",
        "2. Adabiyot",
        "3. Ona tili",
        "4. Rus til va adabiyoti",
        "5. Algebra"
        "6. IBA"
    ],
    "Seshanba": [
        "1. Ingliz tili",
        "2. Algebra",
        "3. Davlat va huquq",
        "4. Fizika",
        "5. Informatika"
    ],
    "Chorshanba": [
        "1. Jahon tarixi",
        "2. Algebra",
        "3. Rus tili va adabiyoti",
        "4. Texnologiya",
        "5. O‘zbekiston tarixi",
        "6. Ingliz tili"
    ],
    "Payshanba": [
        "1. Adabiyot",
        "2. Geografiya",
        "3. Jismoniy tarbiya",
        "4. Chizmachilik",
        "5. Biologiya",
        "6. Kimyo"
    ],
    "Juma": [
        "1. Fizika",
        "2. Tarbiya",
        "3. Jismoniy tarbiya",
        "4. Geometriya",
        "5. Biologiya",
        "6. Ona tili"
    ],
    "Shanba": [
        "1. Informatika",
        "2. Kimyo",
        "3. Ingliz tili",
        "4. Ona tili",
        "5. Geometriya",
        "6. O‘zbekiston tarixi"
    ],
    "Yakshanba": ["Bugun dam olish kuni 😊"]
}

# 🔹 Start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Bugungi", "Ertangi"], ["Haftalik jadval"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Assalomu alaykum! 👋\nQuyidagi tugmalardan birini tanlang:", reply_markup=reply_markup)

# 🔹 Bugungi kun nomini olish
def get_day_name(offset=0):
    days = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
    today = datetime.now() + timedelta(days=offset)
    return days[today.weekday() % 7]

# 🔹 Xabarlar uchun handler
async def send_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Bugungi":
        day = get_day_name(0)
        lessons = "\n".join(schedule[day])
        await update.message.reply_text(f"📅 Bugun — {day}:\n\n{lessons}")

    elif text == "Ertangi":
        day = get_day_name(1)
        lessons = "\n".join(schedule[day])
        await update.message.reply_text(f"📅 Ertangi — {day}:\n\n{lessons}")

    elif text == "Haftalik jadval":
        all_days = ""
        for d, lessons in schedule.items():
            all_days += f"📘 {d}:\n" + "\n".join(lessons) + "\n\n"
        await update.message.reply_text(all_days)

    else:
        await update.message.reply_text("Iltimos, tugmalardan birini tanlang!")

# 🔹 Asosiy funksiya
def main():
    TOKEN = "8325737323:AAE2HSw7hp6Nqz6l145KaNEC84NDx4nP214"  # ⚠️ O‘zingning tokeningni bu yerga yoz
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_schedule))

    print("🤖 Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
