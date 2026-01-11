import asyncio
import logging
from bot import bot, dp
from handlers import start, chat

async def main():
    logging.basicConfig(level=logging.INFO)
    
    # Register routers
    dp.include_router(start.router)
    dp.include_router(chat.router)
    
    print("Bot ishga tushdi / Bot is running...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")
