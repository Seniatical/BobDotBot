import sr_api
import discord
import datetime
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot, BucketType
api = sr_api.Client()
async def get_the_image(self, ctx, animal):
    data = await api.get_image(animal)
    animal = "Bird" if animal == "Birb" else animal
    embed = discord.Embed(title=animal)
    embed.set_image(url=data)
    await ctx.send(embed=embed)

async def get_the_gif(self, ctx, option):
    data = await api.get_gif(option)
    embed = discord.Embed(title=option)
    embed.set_image(url=data)
    await ctx.send(embed=embed)

class FunCog(commands.Cog, name = "Fun"):
    """Fun Commands"""
    def __init__(self, client):
        self.client = client
        self.bot = client
        self.client.owner_id = 690420846774321221

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def amongus(self, ctx, *, member: discord.Member = None):
      member = ctx.author if not member else member
      await ctx.send('command not made yet')

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def dog(self,ctx):
      async with ctx.typing():
        await get_the_image(self,ctx,"Dog")
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def cat(self,ctx):
      async with ctx.typing():
        await get_the_image(self,ctx,"Cat")

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def panda(self, ctx):
      async with ctx.typing():
        await get_the_image(self, ctx, "Panda")
        
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def red_panda(self,ctx):
      async with ctx.typing():
        await get_the_image(self,ctx,"Red_Panda")

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def fox(self,ctx):
      async with ctx.typing():
        await get_the_image(self,ctx,"Fox")

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def bird(self, ctx):
      async with ctx.typing():
        await get_the_image(self, ctx, "Birb")

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def koala(self, ctx):
      async with ctx.typing():
        await get_the_image(self, ctx, "Koala")

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def kangaroo(self, ctx):
      async with ctx.typing():
        await get_the_image(self, ctx, "Kangaroo")

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def giraffe(self,ctx):
      async with ctx.typing():
        await get_the_image(self,ctx,"Giraffe")

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def whale(self,ctx):
      async with ctx.typing():
        await get_the_image(self,ctx,"Whale")

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def bot_token(self, ctx):
      async with ctx.typing():
        token = await api.bot_token()
        await ctx.send(token)

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def wink(self, ctx):
      async with ctx.typing():
        await get_the_gif(self, ctx, "Wink")
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def pat(self,ctx):
      async with ctx.typing():
        await get_the_gif(self,ctx,"Pat")
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def hug(self,ctx):
      async with ctx.typing():
        await get_the_image(self,ctx,"Hug")
    @commands.command(aliases=["fp"])
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def facepalm(self,ctx):
      async with ctx.typing():
        await get_the_gif(self,ctx,"Face-Palm")
    
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.channel)
    @commands.max_concurrency(1, per=BucketType.channel)
    async def chatbot(self,ctx,*,chat = None):
      """Start a chat with a bot. Once you send your first message
      Uses `chatbot <chat>`
      Once you send your first message, the bot will reply to your messages until you say cancel"""
      try:
        if chat:
          async with ctx.typing():
            try:
                data = await api.chatbot(chat)
                embed = discord.Embed(title="Chatbot says:",description=data,timestamp=ctx.message.created_at)
                embed.set_footer(text="Chatbot api by some-random-api - Say cancel to exit\nTimeout:45 seconds")
                await ctx.send(embed=embed)
            except:
                await ctx.send("Error with Chatbot, please try again later")
                return
        else:
          async with ctx.typing():
            embed = discord.Embed(title="I started a chat for you with AI. Type any message to send to the bot, or type cancel to exit",timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
        done = False
        while not done:
            err = None
            def check(msg):
              return msg.author == ctx.author and msg.channel == ctx.channel
            try:
              m = await ctx.bot.wait_for('message', check=check, timeout=45.0)
            except asyncio.TimeoutError:
              err = 'timeout'
            async with ctx.typing():
              source = m.content
              if m.content == 'cancel' or m.content == "Cancel":
                err = 'cancel'
              if err == 'cancel':
                    await ctx.send(':white_check_mark:')
                    done = True
              elif err == 'timeout':
                    await ctx.send(':alarm_clock: **Time\'s up bud**')
                    done = True
              else:
                try:
                    data = await api.chatbot(source)
                    embed = discord.Embed(title="Chatbot says:",description=data)
                    embed.set_footer(text=f"Say cancel to exit - Timeout:45s - started at: {ctx.message.created_at}")
                    await ctx.send(embed=embed)
                except:
                    await ctx.send("Error with Chatbot, please try again later")
                    return
      except:
        try:
            await ctx.send("error")
            return
        except:
            return
    @commands.command(aliases=["mc"])
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def minecraft(self,ctx,*,username):
      async with ctx.typing():
        user = await api.mc_user(username)
        try:
          embed = discord.Embed(title='MineCraft user details:',descriptiom="Provided by some-random-api",timestamp=ctx.message.created_at)
          embed.add_field(name="Username:",value=user.name)
          embed.add_field(name='User UUID',value=user.uuid)
          embed.add_field(name='History',value=user.history)
          embed.add_field(name='History',value=user.formatted_history)
        except:
          embed = discord.Embed(title='Error',descriptiom="Api may be down",timestamp=ctx.message.created_at)
        await ctx.senc(embed=embed)
                  
def setup(client):
    client.add_cog(FunCog(client))
