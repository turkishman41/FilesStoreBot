# (c) @senuinfinity

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
මම Permanent Files Store Bot 🤖 කෙනෙක්!
මට ඕනේ files එවන්න මන් ඒවා මගේ database එකට දා ගන්නම් 😏. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **මගේ නම:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **මාව හැදුවේ :** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **මන් ජිවත් වෙන්නේ Heroku server එකේ:** [Heroku](https://heroku.com)

🧑🏻‍💻 **මාව හැදුවේ නම කියන්න අකමැති කෙනෙක්:** @senuinfinity

👥 **උදව් ඕනෙද මේ group එකෙන් උදව් ගන්න:** [Senu Infinity Support](https://t.me/senuinfinitygroup)

📢 **මගේ update channel එක:** [Senu Infinity](https://t.me/senuinfinity)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @senuinfinity

මාව හදපු කෙනා තාම මන් ඉස්කෝලේ යනවා . පුලුවන්නම් Donate කරාන්න මේ දේවල් පවත්වාගෙන යන්න.

📌ඔන්න කිව්වා මගේ database එකට නරක ඒවා දැම්මොත් එවෙලේම remove කරනවා

[Donate Now](Cooming Soon) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
