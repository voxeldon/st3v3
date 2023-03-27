import discord
from discord.ext import commands
from utils.embed_parser import embed_parser
from utils.embed_builder import EmbedBuilder
from config import private_token as token # Replace with bot token

prefix = '!'
version = '0.0.1'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#Test embed message.
@bot.command(name='test', help='A test message')
async def test(ctx):
    embed = EmbedBuilder() \
        .title('The Title') \
        .description('message description') \
        .author(name='author name', icon_url='https://www.catholicregister.org/media/k2/items/cache/b38830b5df4555b9ee0abe96c1a0a40f_XL.jpg') \
        .footer('footer text') \
        .image('https://www.catholicregister.org/media/k2/items/cache/b38830b5df4555b9ee0abe96c1a0a40f_XL.jpg')

    await embed.send(ctx)
#From Discord embed parser.
@bot.command(name='embed', help='Create an embed message')
@commands.has_permissions(manage_messages=True)
async def embed(ctx):
    message = ctx.message.content.split(' ', 1)[1]
    await embed_parser(ctx, message)

bot.run(token)