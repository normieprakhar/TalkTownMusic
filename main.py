
from pyrogram import Client
from pytgcalls import PyTgCalls
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

API_ID = 29707562
API_HASH = "4b7c10879d615adb90781a4ebcbfc15d"
BOT_TOKEN = "7809941397:AAGmilCx4N5oJ1zLdKTt4aIm2hR1SjUeABw"
OWNER_ID = 6416733683
STRING_SESSION = "BQHFTSoAEzpjkaWFVwzcd3Oesy9ugWkMMQMhCQvpYdSHt4xFC9JfWgoh9y0wq7rWp10-3Ery72eegsMR6RDirZaJCK3KQ3Fn7cYvSwxBuAfs8jhDtHcah0_GwrtWH0IlnzpzFSTFn-GWi9_ZH54GzdgtVIVbonrEQsU5_9kDl9uaTjDFmjyiuEz2jL7O7SSMkl80yRHXuA-wsW3DGC_-rOGBRIZWLx2OeByCo_muN-t_Ekv8yHafFL7ExFxibhfB_b0FLpPRakuh2zkgbTO0j8CAnlGLS6nsUpzNo9F2RJ8waKifRumPOZKgcAdUpLh1hlEi17zWNiOd8LtJahzhxEBR73ZH6gAAAAGHEurKAA"

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client("user", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
call = PyTgCalls(user)

async def start_cmd(client, message: Message):
    if message.from_user and message.from_user.id == OWNER_ID:
        await message.reply("✅ Bot is Alive & Working!")

app.add_handler(MessageHandler(start_cmd))

app.start()
user.start()
call.start()
print("✅ BOT IS LIVE!")
app.idle()
