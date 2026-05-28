# Personal Finance Tracker (Telegram Bot)

**Goal**: A bot for tracking income/expenses with basic analytics.

## Core Features
✅ **Transaction Recording**:
- `/add_income [amount]` - Record income  
- `/add_expense [amount] [category]` - Record expense  

✅ **Transaction History**:
- `/history` - Show last 10 transactions  

✅ **Basic Analytics**:
- `/stats` - Pie chart of expenses by category  

## Tech Stack
- Python 3.10+  
- python-telegram-bot v20+  
- SQLite (database)  
- Matplotlib (visualization)  

## Setup
1. Clone repository  
2. Install dependencies:  
   ```bash  
   pip install python-telegram-bot matplotlib python-dotenv  