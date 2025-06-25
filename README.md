# 🌐 Dynamic IP Checker Discord Bot

A simple Discord bot that periodically checks your public IP address and updates a message in a Discord channel with the latest IP — ideal for sharing dynamic IPs for game servers like Minecraft.

## 🚀 Features

- Checks public IP every 1 minute
- Updates a single message in a Discord channel
- Avoids unnecessary edits if IP hasn't changed
- Persists message ID locally
- Supports multiple Minecraft server port formats

## 🧰 Tech Stack

- Python 3.8+
- [discord.py](https://discordpy.readthedocs.io/)
- [aiohttp](https://docs.aiohttp.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aefnor/dynamic-ip-checker-discord-bot.git
   cd dynamic-ip-checker-discord-bot

## Install Deps

pip install -r requirements.txt


## Configure Env
DISCORD_TOKEN=your_discord_bot_token
CHANNEL_ID=your_channel_id
# MESSAGE_ID=optional_existing_message_id

🛠 How It Works
On startup, the bot logs in and starts a background loop that:

Fetches your current public IP from https://api.ipify.org

If the IP changed since the last check, it updates or sends a Discord message with the new IP

Message ID is stored in message_id.txt to persist across restarts

Example Output Message:
arduino
Copy
Edit
**Minecraft Server IP's:**
```md
Texkit       - 123.456.78.90:25566
Prominence 2 - 123.456.78.90:25565
Tekkit 2     - 123.456.78.90:25567
RL Craft     - 123.456.78.90:25568
ALL THE MODS - 123.456.78.90:25565
🧪 Running the Bot
bash
Copy
Edit
python bot.py
Make sure .env is set up correctly before running.

📝 Notes
If MESSAGE_ID is provided in .env, the bot will try to edit that message directly.

If not, it will send a new message and save the new ID in message_id.txt

🛡 License
This project is licensed under the MIT License.
