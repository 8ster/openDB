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

eball_data = {}
r8ball = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",      
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
    "Yeah",
    "Ye ofcourse!",
    "Yep!",
    "You got it. :thumbsup:",
    "Yes, of course",
    "Absolutely",
    "No way",
    "Nope",
    "No, I’m sorry to say that",
    "I’m not sure",
    "naturally.",
    "that’s right",
    "You're absolutely right",
    "I agree.",
    "I feel that too.",
    "That’s exactly what I was thinking",
    "I couldn’t agree with you more",
    "I think you’re totally right about that",
    "I don’t doubt you’re right…",
    "You know more about this than me…",
    "I understand what you’re saying…",
    "I see what you mean…",
    "I could be wrong about this…",
    "I don’t disagree…",
    "but maybe it's incorrect",
    "right-",
    "I couldn’t agree more",
    "I’ll drink to that",
    "sounds good! ",
    "I see what you’re saying but…",
    "Let's drop it.",
    "Let's just move on, shall we?",
    "No, I'm not so sure about that.",
    "That's not always the case.",
    "That's not always true.",
    "No doubt about it.",
    "That's not always true",
    "Not necessarily.",
    " I'd say the exact opposite.",
    "I beg to differ.",
    "I totally disagree.",
    "I'm afraid I disagree.",
    "No way.",
    "I don't think so.",]


@client.slash_command(name='8ball')
async def eball(ctx, question:str):
    random_reply = random.choice(r8ball)
    if question in eball_data: 
        await ctx.send(eball_data[question])

    else:
        eball_data[question] = random_reply
        await ctx.send(eball_data[question])

token = "some token"
client.run(token)
