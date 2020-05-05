from module import Bot

bot = Bot("bot_olmayan_bot","yzh54321")
bot.login()

bot.users_all_posts(["hacksmith"],like=True,comment=False,amount=1,save=True,comment_options=["Wow!","Amazing"])