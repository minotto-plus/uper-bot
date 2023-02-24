# ランダムを読み込み
# acyncio読み込み
import asyncio
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


@bot.command()
@commands.cooldown(2, 10, type=discord.BucketType.user)
async def hello(ctx):
    await ctx.send("hello!")


@bot.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.CommandOnCooldown):
        return await ctx.send("クールダウン中だよ！")

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
        "草",
    ]

    if (
        ("?" in message.content)
        or ("？" in message.content)
        or ("たん" in message.content)
        or ("なん" in message.content)
    ):
        uperrandom = random.randint(9, 10)
        await message.channel.send(uper[int(uperrandom)])
        return
    elif (
        ("​…" in message.content)
        or ("​・" in message.content)
        or ("..." in message.content)
        or ("​。。" in message.content)
    ):
        uperruadom = random.randint(4, 8)
        await message.channel.send(uper[int(uperrandom)])
        return
    elif (
        ("​できん" in message.content)
        or ("​できない" in message.content)
        or ("むり" in message.content)
    ):
        uperrandom = random.randint(3, 4)
        await message.channel.send(uper[int(uperrandom)])
        return
    elif (
        ("​できた" in message.content)
        or ("！" in message.content)
        or ("ー" in message.content)
    ):
        await message.channel.send(uper[2])
        return
    elif "​謎" in message.content:
        uperrandom = random.randint(0, 1)
        await message.channel.send(uper[int(uperrandom)])
        return
    elif (
        ("​草" in message.content)
        or ("​w" in message.content)
        or ("ｗ" in message.content)
    ):
        await message.channel.send(uper[11])
        return
    else:
        uperrandom = random.randint(0, 11)
        await message.channel.send(uper[int(uperrandom)])
        return


# Botの起動とDiscordサーバーへの接続
client.run(env.BOT_TOKEN)
