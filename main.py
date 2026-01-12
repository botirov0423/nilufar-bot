import asyncio
import logging
import os
from aiohttp import web
from bot import bot, dp
from handlers import start, chat

async def health_check(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    logging.info(f"Web server started on port {port}")

async def main():
    logging.basicConfig(level=logging.INFO)
    
    # Register routers
    dp.include_router(start.router)
    dp.include_router(chat.router)
    
    # Start the dummy web server for Render
    await start_web_server()
    
    print("Bot ishga tushdi / Bot is running...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")
