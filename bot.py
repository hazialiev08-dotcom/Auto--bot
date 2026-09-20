import telebot
import time
import json
import os
import re
from gigachat import GigaChat
from telebot import types

# ============ НАСТРОЙКИ ============
TELEGRAM_TOKEN = os.environ.get('BOT_TOKEN')
GIGACHAT_KEY = os.environ.get('GIGACHAT_KEY')
ADMIN_ID = int(os.environ.get('ADMIN_ID', 0))
# ==================================
