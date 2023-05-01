from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    btn = [[
        InlineKeyboardButton('Updates Channel', url='https://t.me/SL_Bots_Updates'),
        InlineKeyboardButton('Support Group', url='https://t.me/SL_Bots_Support')
    ],[
        InlineKeyboardButton('Repo', url='https://github.com/Hansaka-Anuhas/ForwardBot'),
        InlineKeyboardButton('Developer', url='https://t.me/Hansaka_Anuhas')
    ]]
    text = f"""👋 Hello {message.from_user.mention},

I can forward document and video (mp4 and mkv) files.

Forward your source channel message to this bot. If source channel is forward restricted last message link send to this bot.
/set_skip - Set skip message.
/set_channel - Set target channel."""
    await message.reply(text, reply_markup=InlineKeyboardMarkup(btn))
