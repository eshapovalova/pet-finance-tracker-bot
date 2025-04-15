from telegram import Update
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)
from infrastructure.storage import add_income as store_income, add_expense as store_expense, get_summary

# Handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Welcome! I will help you track your finances.\n\n"
        "Available commands:\n"
        "/add_income [amount] - add income\n"
        "/add_expense [amount] [category] - add expense"
    )

# Handler for the /add_income command
async def add_income(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount = float(context.args[0])
        store_income(update.effective_user.id, amount)
        # Logic to save income to the database
        await update.message.reply_text(f"✅ Income +{amount} recorded!")
    except:
        await update.message.reply_text("❌ Error! Use: /add_income [amount]")

# Handler for the /add_expense command
async def add_expense(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("❌ Use: /add_expense [amount] [category]")
        return

    amount = float(context.args[0])
    category = " ".join(context.args[1:])
    store_expense(update.effective_user.id, amount, category)
    # Logic to save expense to the database
    await update.message.reply_text(f"✅ Expense -{amount} ({category}) recorded!")

# Register all handlers
def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add_income", add_income))
    app.add_handler(CommandHandler("add_expense", add_expense))
