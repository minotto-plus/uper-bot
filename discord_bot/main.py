# ランダムを読み込み
import random

# インストールした discord.py を読み込む
import discord

# アクセストークンを読み込み
import env

# インテントの設定
intents = discord.Intents.all()

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=intents)

overwrite = discord.PermissionOverwrite()


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print(f"{client.user}がログインしました")


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # on/off
    if message.content == "!m on":
        overwrite.send_messages = True

    if message.content == "!m off":
        overwrite.send_messages = False

    # 発言したら迷言が返る処理

    uper = [
        "これは意味ある、、はず",
        "わ",
        "あ、、",
        "俺も意味わからん",
        "？ (?)",
        "。。",
        "うちは問題ナッシング℣",
        "pﾌｩﾝｴｪｪﾝ!",
        "腐",
    ]
    uperrundom = random.randint(0, 8)
    print(uperrundom)
    await message.channel.send(uper[int(uperrundom)])
    return


# Botの起動とDiscordサーバーへの接続
client.run(env.BOT_TOKEN)
