#CREDIT : GURU BOT THANKS FOR YOUR ANIME API 

#REMAKE BY : NOBITA XD AND TRYTOLIVEALONE
# Copyright (C) 2024 JAPANESE X USERBOT
#DON'T KANG FUCKING COWARD
#BSDKE KANG KIYA TOH SOCH LIYO
#AAG LAGA DUNGA TERE ANDAR 
#SAMJHA ? 







import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from config import CMD_HANDLER as cmd

from .help import * 

API_URL = "https://api.nekosapi.com/v3/images/random"


@Client.on_message(filters.command("randomanime", cmd) & filters.me)
async def random_anime(client: Client, message: Message):
    # Send the "Processing..." message
    await message.edit("Fetching a random anime image...")

    # Make the API request
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()["data"]["attributes"]
        image_url = data["file"]
        title = data["title"]
    except (requests.exceptions.RequestException, KeyError):
        await message.edit("Failed to fetch a random anime image.")
        return

    # Send the image and title as a reply
    await client.send_photo(message.chat.id, image_url, caption=f"**Title:** {title}")

    # Edit the original message to indicate success
    await message.edit("Random anime image sent!")

add_command_help(
    "•─╼⃝𖠁 ᴀɴɪᴍᴇ1",
    [
       ["randomanime", "Gɪᴠᴇ random anime pic."],
        ],
                                         )
