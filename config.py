import os
from dotenv import load_dotenv

load_dotenv()

# REUSED EMBED
F1_LOGO = "<:F1logo:784857003225776128>"
NL = "\n"

# BOT CONFIG
BOT_NAME = "Autosport Bot"
BOT_PREFIX = "f1 "
BOT_KEY = os.environ.get("DISCORD_KEY")
BOT_FOOTER = f"Autosport Bot{NL}*NOT affiliated with autosport.com"
