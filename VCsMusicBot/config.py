import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "5959732701:AAFGrPrFwvwd0W39-9smF0EMCkC55bPSx04")
BOT_NAME = getenv("BOT_NAME", "Miku Test")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Miku_updates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/1460234d4ab99e311e3c0.png")
admins = {}
API_ID = int(getenv("API_ID", "15476951"))
API_HASH = getenv("API_HASH", "63d22e688f5c04e472325f03ae4b2fda")
BOT_USERNAME = getenv("BOT_USERNAME", "miku_mctest_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Miku 【V๏ɪ፝֟𝔡】")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "miku_support")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/yunxvoid/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "BCYKVF-KYQWFM-JCMORU-RZWOFQ-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "-1001299748978")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5001899507").split()))
