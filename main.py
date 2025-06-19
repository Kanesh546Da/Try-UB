import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import os
import time

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")

app = Client(
    name="userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

@app.on_message(filters.command("alive", prefixes=".") & filters.me)
async def alive(_, m: Message):
    await m.edit("✅ I'm alive! Hosted on Railway.")

@app.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(_, m: Message):
    start = time.time()
    msg = await m.edit("🏓 Pinging...")
    end = time.time()
    await msg.edit(f"🏓 Pong! `{round((end - start) * 1000)}ms`")

async def main():
    await app.start()
    print("✅ Userbot started.")
    await asyncio.get_event_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())
  
