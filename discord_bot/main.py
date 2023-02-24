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
        "俺も意味わからん",
        "pﾌｩﾝｴｪｪﾝ!",
        "うちは問題ナッシング℣",
        "電",
        "。。",
        "腐",
        "わ",
        "あ、、",
        "そうだよ",
        "？ (?)",
    ]

    if (
        ("?" in message.content)
        and ("？" in message.content)
        and ("たん" in message.content)
        and ("なん" in message.content)
    ):
        uperrundom = random.randint(9, 10)
        await message.channel.send(uper[int(uperrundom)])
        return
    elif (
        ("​…" in message.content)
        and ("​・" in message.content)
        and ("..." in message.content)
        and ("​。。" in message.content)
    ):
        uperrundom = random.randint(4, 8)
        await message.channel.send(uper[int(uperrundom)])
        return
    elif (
        ("​できん" in message.content)
        and ("​できない" in message.content)
        and ("むり" in message.content)
    ):
        uperrundom = random.randint(3, 4)
        await message.channel.send(uper[int(uperrundom)])
        return
    elif (
        ("​できた" in message.content)
        and ("！" in message.content)
        and ("ー" in message.content)
    ):
        await message.channel.send(uper[2])
        return
    elif "​謎" in message.content:
        uperrundom = random.randint(0, 1)
        await message.channel.send(uper[int(uperrundom)])
        return
    else:
        uperrundom = random.randint(0, 9)
        await message.channel.send(uper[int(uperrundom)])
        return


# Botの起動とDiscordサーバーへの接続
client.run(env.BOT_TOKEN)
