#!/bin/bash

# Strict Health Assistant Install Script for Termux

echo "Starting installation for Strict Health Assistant in Termux..."

# Update package lists
echo "Updating package lists..."
pkg update

# Upgrade packages
echo "Upgrading packages..."
pkg upgrade -y

# Install Python and timezone data
echo "Installing Python..."
pkg install python -y

echo "Installing timezone data..."
pkg install tzdata -y

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Instructions for environment variables
echo ""
echo "Installation complete!"
echo ""
echo "To use the bot, you need to set your Telegram Bot Token and Chat ID as environment variables."
echo ""
echo "1. Create a Telegram bot using @BotFather and get your BOT_TOKEN."
echo "2. Send a message to your bot and visit https://api.telegram.org/bot<BOT_TOKEN>/getUpdates to get your CHAT_ID."
echo ""
echo "Then, run the following commands:"
echo "export TELEGRAM_BOT_TOKEN='YOUR_BOT_TOKEN_HERE'"
echo "export TELEGRAM_CHAT_ID='YOUR_CHAT_ID_HERE'"
echo ""
echo "Finally, start the bot with:"
echo "python main.py"
echo ""
echo "The bot will start sending scheduled health notifications via Telegram."
