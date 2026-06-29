from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from atlas.agent.router import process_message
from atlas.core.config import TELEGRAM_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я Atlas 🤖"
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        print("=" * 40)
        print("Получено сообщение")

        user_text = update.message.text
        print("Пользователь:", user_text)

        answer = process_message(user_text)
        print("Ответ модели:", answer)

        await update.message.reply_text(answer)

        print("Сообщение отправлено!")

    except Exception as e:
        import traceback

        print("\nОШИБКА!")
        traceback.print_exc()

        await update.message.reply_text(
            f"Ошибка:\n{e}"
        )


def run():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
    )

    print("Atlas Telegram Bot запущен!")

    app.run_polling()