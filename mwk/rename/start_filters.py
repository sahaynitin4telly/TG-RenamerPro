import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from mwk.config import Config
else:
    from config import Config
from mwk.messages import Translation
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.command("help"))
async def help_user(c,m):
    try:
       await m.reply_text(Translation.HELP_USER,quote=True)
    except Exception as e:
        log.info(str(e))
        
@Client.on_message(filters.command("start"))
async def start_msg(c,m):
update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text(" Sorry, You are **B A N N E D**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="**Please Join My Update Channel Before Using Me..**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
        [
               [
                InlineKeyboardButton(
                        "⚙ Updates Channel", url=f"https://t.me/mwklinks"),
                    InlineKeyboardButton(
                        "🛠 Support Group", url=f"https://t.me/redbullfed")
                ],[
                    InlineKeyboardButton(
                        "👨‍🔬 Developer", url=f"https://t.me/shamilnelli")
                ]
            ]
        ),
    reply_to_message_id=update.message_id
    )
            return
        
@Client.on_message(filters.command("log") & filters.private & filters.user(Config.OWNER_ID))
async def log_msg(c,m):
  z =await m.reply_text("Processing..", True)
  if os.path.exists("Log.txt"):
     await m.reply_document("Log.txt", True)
     await z.delete()
  else:
    await z.edit_text("Log file not found")
