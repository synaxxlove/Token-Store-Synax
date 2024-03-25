#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>⦾ 𝐎𝐰𝐧𝐞𝐫 : <a href='t.me/leackedmmslink'>𝐓𝐮𝐣𝐡𝐞 𝐮𝐬𝐬𝐞 𝐤𝐲 𝐥𝐞𝐧𝐚 🤣</a>\n⦾ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞: <code>𝐏𝐲𝐭𝐡𝐨𝐧 3 🦄</code>\n⦾ 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : <a href='https://docs.pyrogram.org/'>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 {__version__}</a>\n⦾ 𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : <a href='t.me/titaniummovieflix'>𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 🌷</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("☣️ ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pas
