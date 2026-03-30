#!/bin/bash
# =============================================
# Deploy script для UGC Telegram Bot
# =============================================

echo "🚀 Начинаем обновление бота..."

cd /home/content-bot || {
    echo "❌ Ошибка: папка /home/content-bot не найдена!"
    exit 1
}

echo "📥 Выполняем git pull..."
git pull origin main

echo "📦 Обновляем зависимости..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt --upgrade

echo "🔄 Перезапускаем сервис..."
systemctl restart content-bot

echo "📊 Статус сервиса:"
systemctl status content-bot --no-pager -l

echo "✅ Бот успешно обновлён и перезапущен!"