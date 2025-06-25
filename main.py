import os
import aiohttp
import discord
import asyncio
from discord.ext import tasks, commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
MESSAGE_ID = os.getenv("MESSAGE_ID")  # Optional

MESSAGE_ID_FILE = "message_id.txt"
last_ip = None

print("Starting Discord Bot...")
print(f"Using TOKEN: {TOKEN}")
print(f"Using CHANNEL_ID: {CHANNEL_ID}")
if not TOKEN or not CHANNEL_ID:
    raise ValueError("Please set DISCORD_TOKEN and CHANNEL_ID in the .env file.")

# Setup bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

def save_message_id(message_id):
    with open(MESSAGE_ID_FILE, "w") as f:
        f.write(str(message_id))

def load_message_id():
    if MESSAGE_ID:
        return int(MESSAGE_ID)
    if os.path.exists(MESSAGE_ID_FILE):
        with open(MESSAGE_ID_FILE, "r") as f:
            return int(f.read().strip())
    return None

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    check_ip.start()

@tasks.loop(minutes=1)
async def check_ip():
    global last_ip

    try:
        # Get public IP
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.ipify.org") as response:
                ip = (await response.text()).strip()

        # Only update if IP changed
        if ip != last_ip:
            print(f"IP changed to {ip}")
            last_ip = ip

            new_content = f"""**Minecraft Server IP's:**
```md
Texkit       - {ip}:25566
Prominence 2 - {ip}:25565
Tekkit 2     - {ip}:25567
RL Craft     - {ip}:25568
ALL THE MODS - {ip}:25565
```"""

            print("Fetching channel...")
            channel = await bot.fetch_channel(CHANNEL_ID)
            message_id = load_message_id()

            if message_id:
                try:
                    print("Fetching existing message...")
                    message = await channel.fetch_message(message_id)
                    print("Editing message...")
                    await message.edit(content=new_content)
                    return
                except (discord.Forbidden, discord.NotFound) as e:
                    print(f"Failed to edit message: {e}")

            # If no valid message, send a new one
            print("Sending new message...")
            new_message = await channel.send(new_content)
            save_message_id(new_message.id)
            print(f"New message created with ID: {new_message.id}")
        else:
            print("IP has not changed, skipping update.")
    except Exception as e:
        print(f"Error checking IP: {e}")

bot.run(TOKEN)
