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
    # /greet というコマンドで反応する
    if message.content.startswith("/!m off"):
        # メッセージが送信されたチャンネルを取得し、`channel` という変数に入れる
        channel = message.channel

        # チャンネルにメッセージを送信
        await channel.send("!m on と打つとオフが解除されます")

        # 待っているものに該当するかを確認する関数
        def check(m):
            # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
            # コマンドを打ったチャンネルという条件
            return m.content == "!m on" and m.channel == channel

        try:
            # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
            msg = await client.wait_for("message", check=check, timeout=30)
            # wait_forの1つ目のパラメータは、イベント名の on_がないもの
            # 2つ目は、待っているものに該当するかを確認する関数 (任意)
            # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

        # asyncio.TimeoutError が発生したらここに飛ぶ
        except asyncio.TimeoutError:
            await channel.send("俺タイムアウトでオンになったｗ")
        else:
            # メンション付きでメッセージを送信する。
            await channel.send("オンになったｗｗｗ")

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
