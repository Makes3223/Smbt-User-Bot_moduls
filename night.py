import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from core.modul import prefixes, app, modules_help

@app.on_message(filters.command("night", prefixes) & filters.me)
async def stupid(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(0, 14)
    await message.edit_text("<b>I love You</b>")
    text1 = [
        "<b>Good night bunny ð</b>", 
        "<b>Good night sunshine ð</b>",
        "<b>Goodnight kitten ð</b>",
        "<b>Good night flower ð</b>",
        "<b>Good night little angel ð</b>",
        "<b>Good night princess ð</b>",
        "<b>Good night beauty ð</b>",
        "<b>Good night sweetie ð</b>",
        "<b>Good night cute ð</b> <b>Good night bead ð</b>",
        "<b>I</b>",
        "<b>ð you ð</b>",
        "<b>ð very  ð</b>",
        "<b>ð strongly ð</b>",
        "<b>ð Loveð</b>",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit_text(text1[i % 14])

modules_help["night"] = {
    "night": "Surprise your significant other"
}