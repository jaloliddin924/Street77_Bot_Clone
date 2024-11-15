# from aiogram import Bot, Dispatcher, executor
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# import logging
# import asyncio
# from config import API_TOKEN, ADMIN

# #
# # token = "7808486852:AAHcykfAXfB8mZGsBFye1xOhyoMFjU5zLmE"
# # admin = 6271337642  # Replace with the integer ID of the admin (e.g., admin = 123456789)



# logging.basicConfig(level=logging.INFO)
# bot = Bot(token=API_TOKEN, parse_mode="HTML")
# dp = Dispatcher(bot, storage=MemoryStorage())

# async def on_startup(dp):
#     try:
#         logging.info("Bot is starting up...")
#         await bot.send_message(chat_id=ADMIN, text="Bot ishga tushdi")
#         logging.info("Startup notification sent successfully.")
#     except Exception as e:
#         logging.error(f"Failed to send startup notification: {e}")

# async def on_shutdown(dp):
#     try:
#         logging.info("Bot is shutting down...")
#         await bot.send_message(chat_id=admin, text="Bot to'xtadi")
#         logging.info("Shutdown notification sent successfully.")
#     except Exception as e:
#         logging.error(f"Failed to send shutdown notification: {e}")

# if __name__ == '__main__':
#     # Use start_polling with on_startup and on_shutdown handlers
#     executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)





from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from config import API_TOKEN, ADMIN

logging.basicConfig(level=logging.INFO)

API_TOKEN = "7808486852:AAHcykfAXfB8mZGsBFye1xOhyoMFjU5zLmE"
ADMIN =  6271337642  


bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())

async def on_startup(dp):
    try:
        logging.info("Bot is starting up...")
        await bot.send_message(chat_id=ADMIN, text="Bot ishga tushdi")
        logging.info("Startup notification sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send startup notification: {e}")

async def on_shutdown(dp):
    try:
        logging.info("Bot is shutting down...")
        await bot.send_message(chat_id=ADMIN, text="Bot to'xtadi")
        logging.info("Shutdown notification sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send shutdown notification: {e}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
