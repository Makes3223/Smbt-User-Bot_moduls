import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from core.modul import prefixes, app, modules_help

@app.on_message(filters.command("stupid", prefixes) & filters.me)
async def stupid(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(0, 14)
    await message.edit_text("stupid boy")
    animation_chars = [
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\nš§          (^_^)š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\nš§        (^_^)  š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\nš§      (^_^)    š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\nš§    (^_^)      š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\nš§  (^_^)        š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\nš§ < (^_^ <)         š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\n(> ^_^)>š§          š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\n  (> ^_^)>š§        š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\n    (> ^_^)>š§      š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\n      (> ^_^)>š§    š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\n        (> ^_^)>š§  š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\n          (> ^_^)>š§ š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\n           (> ^_^)>š",
        "<b>YOUR BRAIN</b> ā”ļø š§ \n\n           < (^_^ <)š",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit_text(animation_chars[i % 14])

modules_help["stupid"] = {
    "stupid": " stupid animation"
}