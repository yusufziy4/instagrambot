from instagrambot import *
import json

with open("creds.json", "r") as settings:
    creds = json.loads(settings.read())
    bot = Bot(creds["username"],creds["password"])
    bot.login()