
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

import numpy
import os
from PIL import Image
import time
import pyrogram
from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from mwk.config import Config
from mwk.messages import Translation
from mwk.shamil.database import *
logging.getLogger("pyrogram").setLevel(logging.WARNING)



@Client.on_message(filters.photo)
async def save_photo(c,m):
    v = await m.reply_text("**Saving Thumbnail...**",True)
    if m.media_group_id is not None:
        # album is sent
        download_location = Config.DOWNLOAD_LOCATION + "/thumb/" + str(m.from_user.id) + "/" + str(m.media_group_id) + "/"
        if not os.path.isdir(download_location):
            os.mkdir(download_location)
        await df_thumb(m.from_user.id, m.message_id)
        await c.download_media(
            message=m,
            file_name=download_location
        )
    else:
        # received single photo
        download_location = Config.DOWNLOAD_LOCATION + "/thumb/" + str(m.from_user.id) + ".jpg"
        await df_thumb(m.from_user.id, m.message_id)
        await c.download_media(
            message=m,
            file_name=download_location
        ) 
        try:
           await v.edit_text("**☑ Custom Thumbnail Saved Successfully...!**")
        except Exception as e:
          log.info(f"#Error {e}")

@Client.on_message(filters.command(["delthumb"]))
async def delete_thumbnail(c,m):
    download_location = Config.DOWNLOAD_LOCATION + "/thumb/" + str(m.from_user.id)
    try:
        os.remove(download_location + ".jpg")
        await del_thumb(m.from_user.id)
    except:
        pass
    await m.reply_text("**🗑️ Custom Thumbnail Deleted Successfully...!**",quote=True)

@Client.on_message(filters.command(["showthumb"]))
async def show_thumbnail(c,m):
    thumb_image_path = Config.DOWNLOAD_LOCATION + "/thumb/" + str(m.from_user.id) + ".jpg"
    msgg = await m.reply_text("**Checking Thumbnail... 🧐**",quote=True)

    if not os.path.exists(thumb_image_path):
        mes = await thumb(m.from_user.id)
        if mes is not None:
            msgg = await c.get_messages(m.chat.id, mes.msg_id)
            await msgg.download(file_name=thumb_image_path)
            thumb_image_path = thumb_image_path
        else:
            thumb_image_path = None

    if thumb_image_path is None:
        try:
            await msgg.edit_text("**No Saved Thumbnail Found!! 😐😐**")
        except:
              pass               
    else:
        try:
           await msgg.delete()

        except:
            pass

        await m.reply_photo(
        photo=thumb_image_path,
        caption="**__🖼️ Your Custom Thumbnail...👆🏻__**",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🗑️ Delete Thumbnail", callback_data="delete")]]), 
        quote=True
    )

