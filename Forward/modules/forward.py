import os
import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from config import SUDO_USERS, SERIES_ID, MOVIES_ID, FORWARD_IDS
from Forward import app
from pyromod import listen
from Forward.modules.channel import x

lock = asyncio.Lock()



@app.on_message(filters.command("index") & filters.user(SUDO_USERS))
async def batch(client, message):
    if lock.locked():
        await message.reply("<code>Wait until previous process completes.</code>")
    else:
        last_msg = await client.ask(text="<code>Forward last message from DB channel (with quotes)\n\nor send the DB channel post link</code>", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)        
        try:
            last_msg_id = last_msg.forward_from_message_id
            chat_id = last_msg.forward_from_chat.username or last_msg.forward_from_chat.id
            lol = await client.get_messages(chat_id, last_msg_id)
                
            if "document" in lol:
                file_name = lol.docoument.file_name
            elif "video" in lol:
                file_name = lol.video.file_name

        except Exception as e:
            await last_msg.reply_text(f"<code>This is an invalid message, either the channel is private and bot is not an admin in the forwarded chat, or you forwarded messages as copy.\nError: {e}</code>")
        try:
            print(file_name)
            for i in int(last_msg_id):
                for keyword in x:
                    if keyword in file_name:
                        await app.copy_message(chat_id=SERIES_ID, from_chat_id=FORWARD_IDS, message_id=i)
                        break
                else:
                    await app.copy_message(chat_id=MOVIES_ID, from_chat_id=FORWARD_IDS, message_id=i)

        except Exception as e:
            print(e)
            continue
                

       
        
