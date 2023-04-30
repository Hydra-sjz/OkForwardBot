from Script import script
from pyrogram import Client, filters, enums


@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(script.START_TXT.format(message.from_user.mention))
