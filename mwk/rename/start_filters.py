import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

if bool(os.environ.get("WEBHOOK", False)):
    from mwk.config import Config
else:
    from config import Config

# the Strings used for this "thing"
from mwk.messages import Translation
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.command("help"))
async def help_user(c,m):
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await c.get_chat_member(update_channel, m.chat.id)
            if user.status == "kicked":
               await m.reply_text("🤭 Sorry Dude, You are **B A N N E D**. If you feel You are not guilty please contact owner")
               return
        except UserNotParticipant:
            await m.reply_text(
                text="**Join My Updates Channel to use me & Enjoy the Free Service**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join Our Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
    try:
       await m.reply_text(Translation.HELP_USER,quote=True)
    except Exception as e:
        log.info(str(e))
        
@Client.on_message(filters.command("start"))
async def start_msg(c,m):
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await c.get_chat_member(update_channel, m.chat.id)
            if user.status == "kicked":
               await m.reply_text("🤭 Sorry Dude, You are **B A N N E D**. If you feel You are not guilty please contact owner")
               return
        except UserNotParticipant:
            await m.reply_text(
                text="**Join My Updates Channel to use me & Enjoy the Free Service**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join Our Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
    await m.reply_text(Translation.START_TEXT.format(m.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
               [
                InlineKeyboardButton("⚙ Updates Channel", url=f"https://t.me/mwklinks"),
                    InlineKeyboardButton("🛠 Support Group", url=f"https://t.me/redbullfed")
                ],
                [
                    InlineKeyboardButton("👨‍🔬 Developer", url=f"https://t.me/shamilnelli")
                ]
            ]
        ),
        reply_to_message_id=m.message_id
    )
          #  return
        
@Client.on_message(filters.command("log") & filters.private & filters.user(Config.OWNER_ID))
async def log_msg(c,m):
  z =await m.reply_text("Processing..", True)
  if os.path.exists("Log.txt"):
     await m.reply_document("Log.txt", True)
     await z.delete()
  else:
    await z.edit_text("Log file not found")
