from telegram.ext import ApplicationBuilder
from presentation.bot.handlers import setup_handlers  # Import handlers from handlers.py
from dotenv import load_dotenv
from infrastructure.storage import init_db
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def post_init(application):
    # Optional: code that runs after the bot is initialized
    await application.bot.set_my_commands([
        ("start", "Start the bot"),
        ("add_income", "Add income"),
        ("add_expense", "Add expense")
    ])

def main():
    # Create application instance
    init_db()
    app = ApplicationBuilder() \
        .token(BOT_TOKEN) \
        .post_init(post_init) \
        .build()

    # Register command handlers
    setup_handlers(app)

    # Start the bot
    print("🚀 Bot is running. Open Telegram and send /start.")
    app.run_polling()

if __name__ == "__main__":
    main()
