#!/bin/bash
echo "🛑 Останавливаем бота..."
systemctl stop content-bot
sleep 3

echo "🚀 Запускаем бота..."
systemctl start content-bot

echo "📊 Статус:"
systemctl status content-bot --no-pager -l