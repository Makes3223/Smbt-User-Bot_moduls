from pyrogram import Client, filters
from pyrogram.types import Message

from core_v1.modul import prefixes, app, modules_help
import asyncio, random


@app.on_message(filters.command("kokodrilo", prefixes) & filters.me)
async def kokodrilo_explodando(_, message: Message):
    amount = 1
    if len(message.command) > 1:
        amount = int(message.command[1])
    for _ in range(amount):
        await message.edit("🐊")
        await asyncio.sleep(random.uniform(1, 2.5))
        await message.edit("💥")
        await asyncio.sleep(1.8)


modules_help["kokodrilo_explodando"] = {
    "kokodrilo [number of explosions]": "<b>kOkOdRiLo ExPlOrAdO</b>",
}
