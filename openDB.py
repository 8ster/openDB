import nextcord
from nextcord import Interaction
from nextcord.ext import commands

# intents = nextcord.Intents.default()
intents= nextcord.Intents.all()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix="/", intents=intents)


@client.event
async def on_ready():
    print("Bot is Ready For Use!")


testingServerID = "server id"

# your slash commands
@client.slash_command(name='hello', description="Replies with Hello", guild_ids=[testingServerID])
async def hello(interaction: Interaction):
    await interaction.response.send_message("Hello There")


token = "some token"
client.run(token)
