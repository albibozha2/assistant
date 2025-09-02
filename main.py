import logging
import time
import asyncio
import os
from telegram import Bot
from telegram.error import TelegramError
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from plans import meal_plan, gym_plan, daily_tasks, motivational_messages, full_body_coaching, psychological_discipline, hourly_meal_reminders, hourly_gym_reminders, coach_quotes_against_narcissists, quotes_ibn_arabi, quotes_mevlana, quotes_carl_jung, quotes_paracelsus

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram Bot Token and Chat ID - Set as environment variables
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '7911726308:AAFO-i9VV12PM6kCMNkdezhvm8djp38dPlg')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '6405775515')

if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    raise ValueError("Please set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID environment variables.")

bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_message(text, retries=3):
    for attempt in range(retries):
        try:
            await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text)
            logger.info(f"Sent message: {text}")
            return
        except TelegramError as e:
            logger.error(f"Failed to send message (attempt {attempt + 1}/{retries}): {e}")
            if attempt < retries - 1:
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
            else:
                logger.error(f"Failed to send message after {retries} attempts: {text}")


async def send_daily_meal_plan():
    message = "Plani i Ushqimit për sot:\n"
    for key, value in meal_plan.items():
        message += f"{value}\n"
    await send_message(message)

async def send_daily_gym_plan():
    message = "Plani i Gjimnastikës për sot:\n"
    for key, value in gym_plan.items():
        message += f"{value}\n"
    await send_message(message)

async def send_daily_tasks():
    message = "Detyrat Ditore Strikte:\n"
    for task in daily_tasks:
        message += f"- {task}\n"
    await send_message(message)

async def send_motivational_message():
    import random
    message = random.choice(motivational_messages)
    await send_message(message)

async def send_full_body_coaching():
    import random
    message = random.choice(full_body_coaching)
    await send_message(message)

async def send_psychological_discipline():
    import random
    message = random.choice(psychological_discipline)
    await send_message(message)

async def send_hourly_meal_reminder():
    import random
    message = random.choice(hourly_meal_reminders)
    await send_message(message)

async def send_hourly_gym_reminder():
    import random
    message = random.choice(hourly_gym_reminders)
    await send_message(message)

async def send_coach_quote_against_narcissists():
    import random
    message = random.choice(coach_quotes_against_narcissists)
    await send_message(message)

async def send_quote_ibn_arabi():
    import random
    message = random.choice(quotes_ibn_arabi)
    await send_message(message)

async def send_quote_mevlana():
    import random
    message = random.choice(quotes_mevlana)
    await send_message(message)

async def send_quote_carl_jung():
    import random
    message = random.choice(quotes_carl_jung)
    await send_message(message)

async def send_quote_paracelsus():
    import random
    message = random.choice(quotes_paracelsus)
    await send_message(message)

async def schedule_notifications():
    scheduler = AsyncIOScheduler()
    # Schedule meal plan notifications at 8:00, 13:00, 19:00
    scheduler.add_job(send_daily_meal_plan, 'cron', hour=8, minute=0)
    scheduler.add_job(send_daily_meal_plan, 'cron', hour=13, minute=0)
    scheduler.add_job(send_daily_meal_plan, 'cron', hour=19, minute=0)
    # Schedule gym plan notifications at 7:00, 15:00, 20:00
    scheduler.add_job(send_daily_gym_plan, 'cron', hour=7, minute=0)
    scheduler.add_job(send_daily_gym_plan, 'cron', hour=15, minute=0)
    scheduler.add_job(send_daily_gym_plan, 'cron', hour=20, minute=0)
    # Schedule daily tasks notification at 9:00
    scheduler.add_job(send_daily_tasks, 'cron', hour=9, minute=0)
    # Schedule motivational messages at 12:00 and 18:00
    scheduler.add_job(send_motivational_message, 'cron', hour=12, minute=0)
    scheduler.add_job(send_motivational_message, 'cron', hour=18, minute=0)
    # Schedule full body coaching every 2 hours
    scheduler.add_job(send_full_body_coaching, 'interval', hours=2)
    # Schedule psychological discipline every 2 hours
    scheduler.add_job(send_psychological_discipline, 'interval', hours=2)
    # Schedule hourly meal reminders every hour
    scheduler.add_job(send_hourly_meal_reminder, 'interval', hours=1)
    # Schedule hourly gym reminders every hour
    scheduler.add_job(send_hourly_gym_reminder, 'interval', hours=1)
    # Schedule coach quotes against narcissists every 3 hours
    scheduler.add_job(send_coach_quote_against_narcissists, 'interval', hours=3)
    # Schedule quotes from Ibn Arabi every 4 hours
    scheduler.add_job(send_quote_ibn_arabi, 'interval', hours=4)
    # Schedule quotes from Mevlana every 4 hours
    scheduler.add_job(send_quote_mevlana, 'interval', hours=4)
    # Schedule quotes from Carl Jung every 4 hours
    scheduler.add_job(send_quote_carl_jung, 'interval', hours=4)
    # Schedule quotes from Paracelsus every 4 hours
    scheduler.add_job(send_quote_paracelsus, 'interval', hours=4)

    scheduler.start()
    logger.info("Scheduler started. Notifications will be sent according to the schedule.")

    try:
        # Keep the script running
        while True:
            await asyncio.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logger.info("Scheduler stopped.")

async def main():
    await send_message("Asistent shëndetësor i rreptë është duke filluar! Përgatitu për një rikthim të fuqishëm të trupit dhe mendjes!")
    await schedule_notifications()

if __name__ == "__main__":
    asyncio.run(main())
