<div align="center">

# 🤖 Atlas AI

### Open Source AI Agent powered by Ollama

Планирует • Выполняет • Автоматизирует

![Version](https://img.shields.io/badge/version-v0.1.0-blue)
![Python](https://img.shields.io/badge/python-3.11+-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Active-success)

</div>

---

# 🚀 Что такое Atlas?

**Atlas** — это открытый AI-агент нового поколения.

Он не просто отвечает на вопросы, а способен:

- 🧠 понимать задачи пользователя
- 📋 самостоятельно строить план выполнения
- 🔧 использовать инструменты
- 📂 работать с файлами
- ▶️ запускать Python
- 🤖 работать локально через **Ollama**
- 💬 общаться через **Telegram**

---

# ✨ Возможности

- ✅ Telegram Bot
- ✅ Ollama Integration
- ✅ AI Planner
- ✅ Executor
- ✅ Tool Registry
- ✅ Read File
- ✅ Write File
- ✅ List Files
- ✅ Run Python
- ✅ Workspace Sandbox

---

# 🏗 Архитектура

```text
                Пользователь
                     │
                     ▼
             Telegram Bot
                     │
                     ▼
              Atlas Agent
                     │
      ┌──────────────┴──────────────┐
      ▼                             ▼
  AI Planner                  Tool Executor
      │                             │
      └──────────────┬──────────────┘
                     ▼
                Tool Registry
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Read File      Write File     Run Python
```

---

# 📂 Структура проекта

```text
Atlas/

├── atlas/
│   ├── agent/
│   ├── ai/
│   ├── bot/
│   ├── core/
│   ├── executor/
│   ├── planner/
│   ├── tools/
│   └── workspace/
│
├── requirements.txt
├── main.py
├── README.md
└── CHANGELOG.md
```

---

# ⚡ Быстрый старт

### 1. Клонировать проект

```bash
git clone https://github.com/sharauttxt/Atlas.git
cd Atlas
```

### 2. Создать виртуальное окружение

```bash
python -m venv .venv
```

### 3. Активировать

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

### 5. Настроить `.env`

```env
TELEGRAM_TOKEN=YOUR_TOKEN
AI_PROVIDER=ollama
MODEL_NAME=qwen2.5-coder:7b
```

### 6. Запустить

```bash
python main.py
```

---

# 💬 Примеры команд

```
Покажи все файлы

Прочитай README.md

Создай hello.py

Запусти hello.py
```

---

# 🛣 Roadmap

## ✅ v0.1.0

- Telegram Bot
- Ollama
- Planner
- Executor
- Tool Registry
- File Tools
- Python Runner

---

## 🚧 v0.2.0

- Memory
- Multi-Step Planning
- Better JSON Parser
- Tool Chaining

---

## 🚀 v0.3.0

- Autonomous Reasoning
- Self-Correction
- Project Generator
- Web Search
- Git Integration

---

# 🎯 Цель проекта

Atlas создаётся как **полностью автономный AI Developer**.

В будущем он сможет:

- создавать сайты;
- писать Telegram-ботов;
- генерировать API;
- исправлять собственные ошибки;
- работать с Git;
- управлять Linux;
- автоматически создавать полноценные проекты по одному запросу.

---

# 📜 Лицензия

MIT License

---

<div align="center">

**⭐ Если проект понравился — поставьте звезду на GitHub!**

Made with ❤️ by **sharautt**

</div>