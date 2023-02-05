import os

from pyrogram import Client, filters
from pyrogram.types import Message
from core.modul import modules_help, prefixes, app


@app.on_message(filters.command("tt", prefixes) & filters.me)
async def tiktok(client: Client, message: Message):
    if len(message.command) > 1:
        link = message.command[1]
    elif message.reply_to_message:
        link = message.reply_to_message.text
    else:
        await message.edit("<b>Link isn't provided</b>")
        return

    await message.edit("<b>Downloading...</b>")
    await client.unblock_user("@downloader_tiktok_bot")
    response = await client.send_message("@downloader_tiktok_bot", link)
    if response.video:
        await client.download_media(message=response)
        file_name = response.video.file_name
        await message.edit(f"<b>Successfully downloaded {file_name}</b>")
    else:
        await message.edit("<b>Video not found</b>")

    await message.delete()
    await client.delete_messages("@downloader_tiktok_bot", [response.message_id])


modules_help["tiktok"] = {
    "tt [link|reply]*": "download video from tiktok",
}
