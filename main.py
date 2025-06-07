import discord
import requests
import os

# NOTE: We have removed the TARGET_CHANNEL_ID variable.

# --- No need to touch anything below this line ---

TOKEN = os.environ['DISCORD_TOKEN']
WEBHOOK_URL = os.environ['WEBHOOK_URL']

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is logged in as {client.user} and listening to all accessible channels.')

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # The check for a specific channel has been removed.
    # This code will now run for any message in any channel the bot can see.

    print(f"Caught message in #{message.channel.name}: '{message.content}'")

    payload = {
        'content': message.content,
        'author_name': message.author.name,
        'timestamp': message.created_at.isoformat(),
        'channel_name': message.channel.name
    }

    try:
        requests.post(WEBHOOK_URL, json=payload)
        print("Successfully forwarded message to n8n.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending to n8n webhook: {e}")

client.run(TOKEN)