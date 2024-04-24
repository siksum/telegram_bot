from telegram import *
from telegram.ext import *

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3"),
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6"),
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9"),
        ]
    ]

    await update.effective_message.reply_text(
        text=f"입장퀴즈! {update.effective_user.name}\n여름이의 몸무게는?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def good(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.effective_message.reply_text(f'Hello {update.effective_user.first_name}!') 
    await update.effective_message.reply_photo('/Users/sikk/Desktop/project/telegram_bot/summer.jpg')
    await update.effective_message.reply_text(text="뚱땡이 여름이")


async def bad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await update.effective_message.reply_text(text="바보! 메롱 안녕히가세요")
    



app = ApplicationBuilder().token("6358694938:AAF-fs8oXwbWdi7smqGArF1oYA3itL2sNHE").build() # YOUR TOKEN HERE에 위의 API Key를 입력한다.
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(good, pattern="^6$"))
app.add_handler(CallbackQueryHandler(bad, pattern='^(?!6).*$'))
app.run_polling()