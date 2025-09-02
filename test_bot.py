import asyncio
import os
from telegram import Bot
from telegram.error import TelegramError
from plans import meal_plan, gym_plan, daily_tasks, motivational_messages, full_body_coaching, psychological_discipline, hourly_meal_reminders, hourly_gym_reminders, coach_quotes_against_narcissists, quotes_ibn_arabi, quotes_mevlana, quotes_carl_jung, quotes_paracelsus
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '7911726308:AAFO-i9VV12PM6kCMNkdezhvm8djp38dPlg')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '6405775515')

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
                await asyncio.sleep(2 ** attempt)
            else:
                logger.error(f"Failed to send message after {retries} attempts: {text}")

async def test_all_messages():
    import random

    # Test daily meal plan
    message = "Test - Plani i Ushqimit për sot:\n"
    for key, value in meal_plan.items():
        message += f"{value}\n"
    await send_message(message)

    # Test daily gym plan
    message = "Test - Plani i Gjimnastikës për sot:\n"
    for key, value in gym_plan.items():
        message += f"{value}\n"
    await send_message(message)

    # Test daily tasks
    message = "Test - Detyrat Ditore Strikte:\n"
    for task in daily_tasks:
        message += f"- {task}\n"
    await send_message(message)

    # Test motivational message
    message = "Test - " + random.choice(motivational_messages)
    await send_message(message)

    # Test full body coaching
    message = "Test - " + random.choice(full_body_coaching)
    await send_message(message)

    # Test psychological discipline
    message = "Test - " + random.choice(psychological_discipline)
    await send_message(message)

    # Test hourly meal reminder
    message = "Test - " + random.choice(hourly_meal_reminders)
    await send_message(message)

    # Test hourly gym reminder
    message = "Test - " + random.choice(hourly_gym_reminders)
    await send_message(message)

    # Test coach quote against narcissists
    message = "Test - " + random.choice(coach_quotes_against_narcissists)
    await send_message(message)

    # Test quotes
    message = "Test - " + random.choice(quotes_ibn_arabi)
    await send_message(message)

    message = "Test - " + random.choice(quotes_mevlana)
    await send_message(message)

    message = "Test - " + random.choice(quotes_carl_jung)
    await send_message(message)

    message = "Test - " + random.choice(quotes_paracelsus)
    await send_message(message)

    await send_message("Test completed - All message types sent successfully!")

if __name__ == "__main__":
    asyncio.run(test_all_messages())
