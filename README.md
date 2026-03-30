# 📸 UGC Telegram Bot — Poly Content Bot

## 🎯 Цель проекта

Создать полностью рабочего Telegram-бота, который собирает фотографии и короткие истории от студентов и сотрудников университета.
Бот автоматически сохраняет контент на **Яндекс.Диск** + в **Google Sheets** для дальнейшего использования в соцсетях, подкастах и презентациях.

---


## 🚀 Как начать работу (для каждого участника)

### 1. Локальная разработка

```bash
# Клонируем репозиторий
git clone https://github.com/YatchenkoArD/-UGC-Bot-Telegram.git
cd -UGC-Bot-Telegram

# Создаём виртуальное окружение
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Устанавливаем зависимости
pip install -r requirements.txt

# Создаём .env файл
cp .env.example .env
# ← Открой .env и вставь свой BOT_TOKEN
```

### ▶️ Запуск бота локально

```bash
python main.py
```

---

## 🔧 2. Как работать с Git

```bash
# Создавай ветку под свою задачу
git checkout -b feature/твоя-задача
```

После работы:

```bash
git add .
git commit -m "описание изменений"
git push origin feature/твоя-задача
```

Создай Pull Request в `main`.

---

## 🚀 3. Как задеплоить изменения на сервер

После принятия PR или пуша в `main` на сервере выполни:

```bash
cd /home/content-bot && ./deploy.sh
```

---

## 📁 Структура проекта

```text
content-bot/
├── main.py                 # Главный файл бота
├── deploy.sh               # Обновление бота на сервере
├── restart.sh              # Быстрый перезапуск
├── requirements.txt
├── .env                    # ← Секретные данные (не коммитить!)
├── .env.example
├── .gitignore
└── README.md
```

---

## 🔧 Полезные команды на сервере

```bash
# Статус бота
systemctl status content-bot

# Перезапустить бота
systemctl restart content-bot

# Логи в реальном времени
journalctl -u content-bot -f

# Обновить бота после изменений в коде
cd /home/content-bot && ./deploy.sh
```

---

## ⚠️ Важные правила

* Никогда не коммитьте файл `.env`
* Всегда работайте в своей ветке
* Перед пушем проверяйте код локально
* После пуша в `main` сразу запускайте `deploy.sh` на сервере
