import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQDGTRlEi126Oi5APoKSRawxMEy1BNo4t5cy7aY7Db8z-EyewXyxrD3qOhvhxl9vuyY_NBCcNkwAb_7y2ECidCpLPSZHA4Vx8vaMrNmcALdz_QaL-SxDBuTlnMmfgk887B0e6icMsKMdD1-ZHSs7nIlNAK3VOoFJ260QYRACqRqtDh8oq9BpmebAFJ9jFIgNhJWHKCj4ztrrEZEJQJdpyXjgBhXBBaGCIAHhD7EGrq9w_CB6KhB5aDz0lSEgld4PX64zCutuQ3CT-HUjxprMgEi9ayiwMS8l53pCeJZRyeJrc4vFw_FnM815YPRYjHZ3NdMUuX_IRoBNPMNuCea79YHQccuYXQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5986072761:AAGDGSBrYlvh7AHNaI8AYj-YN9UQSUzkPDY")
BOT_NAME = getenv("BOT_NAME", "Tomiyoka")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Miku_updates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("API_ID", "15476951"))
API_HASH = getenv("API_HASH", "63d22e688f5c04e472325f03ae4b2fda")
BOT_USERNAME = getenv("BOT_USERNAME", "tomiyoka_music_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Miku 【V๏ɪ፝֟𝔡】")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "miku_support")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/yunxvoid/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "BCYKVF-KYQWFM-JCMORU-RZWOFQ-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
