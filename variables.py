import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

PICS = os.environ.get("PICS", "https://graph.org/file/e4b3cc8ea3b61d3098613.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6387027582').split()]

DB_URL = os.environ.get("DB_URL", "")

DB_NAME = os.environ.get("DB_NAME", "tg-multi-bot")

RemoveBG_API = os.environ.get("RemoveBG_API", "sFvSnp6KmgGi7pWDNp4sfn5P")

FORCE_SUB = os.environ.get("FORCE_SUB", None)           

HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")
 
log_channel = environ.get("LOG_CHANNEL","-1001887302664")

LOG_CHANNEL = int(log_channel) if log_channel and id_pattern.search(log_channel) else None

LOG_TEXT = """<i><u>👁️‍🗨️USER DETAILS</u>

○ ID : <code>{id}</code>
○ DC : <code>{dc_id}</code>
○ First Name : <code>{first_name}<code>
○ UserName : @{username}

By = {bot}</i>"""












