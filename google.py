from pyrogram import Client, filters
from pyrogram.types import Message
from core_v1.modul import prefixes, app, modules_help
from core_v1.script import format_exc


@app.on_message(filters.command(["google", "g"], prefixes) & filters.me)
async def webshot(_, message: Message):
    user_request = " ".join(message.command[1:])

    if user_request == "":
        if message.reply_to_message:
            reply_user_request = message.reply_to_message.text
            request = reply_user_request.replace(" ", "+")
            full_request = f"https://www.google.com/search?q={request}"
            await message.edit(
                f"<a href={full_request}>{reply_user_request}</a>",
                disable_web_page_preview=True,
            )

    else:
        request = user_request.replace(" ", "+")
        full_request = f"https://www.google.com/search?q={request}"
        await message.edit(
            f"<a href={full_request}>{user_request}</a>", disable_web_page_preview=True
        )


modules_help["google"] = {
    "google [request]": "To teach the interlocutor to use Google. Request isn't required."
}
