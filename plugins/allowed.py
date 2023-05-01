from pyrogram import Client, filters
from pyrogram.types import Message
from info import PRIVATE_BOT, ADMINS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def admins(_, client, message: Message):
    if PRIVATE_BOT:
        return message.from_user.id not in ADMINS

allowed_users = filters.create(admins)

@Client.on_message(filters.private & allowed_users & filters.incoming)
async def not_admins(bot, message):
    btn = [[
        InlineKeyboardButton('Repo', url='https://github.com/Hansaka-Anuhas/ForwardBot')
    ],[
        InlineKeyboardButton('Developer', url='https://t.me/Hansaka_Anuhas')
    ]]
    await message.reply("You can't access this bot, Create your own bot", reply_markup=InlineKeyboardMarkup(btn))
