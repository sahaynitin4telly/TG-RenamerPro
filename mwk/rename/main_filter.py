
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant

if bool(os.environ.get("WEBHOOK", False)):
    from mwk.config import Config
else:
    from config import Config

# the Strings used for this "thing"
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

@Client.on_message(filters.document | filters.video | filters.audio | filters.voice | filters.video_note | filters.animation) 
async def rename_filter(c,m):
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
    media = m.document or m.video or m.audio or m.voice or m.video_note or m.animation
    text = ""
    button = []
    try:
      filename = media.file_name
      text += f"FileName:\n{filename}\n"
    except:
    # some files dont gib name ..
      filename = None 
    
    text += "Select the desired Option"
    button.append([InlineKeyboardButton("📂 Rename as File 📂", callback_data="rename_file")])
  # Thanks to albert for mime_type suggestion 
    if media.mime_type.startswith("video/"):
    ## how the f the other formats can be uploaded as video 
      button.append([InlineKeyboardButton("🎞️ Rename as Video 🎞️",callback_data="rename_video")])
      button.append([InlineKeyboardButton("🎞️ Convert to File 📂",callback_data="convert_file")])
      button.append([InlineKeyboardButton("📂 Convert to Video 🎞️",callback_data="convert_video")])
    button.append([InlineKeyboardButton("Cancel ❌",callback_data="cancel")])
 
    markup = InlineKeyboardMarkup(button)
    try:
      await m.reply_text(text,quote=True,reply_markup=markup,parse_mode="markdown",disable_web_page_preview=True)
    except Exception as e:
      log.info(str(e))
