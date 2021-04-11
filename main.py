import discord
import time
from discord.ext import commands, tasks
import random
import pickle
from pretty_help import PrettyHelp
import json

random.seed(time.time() * time.time() + time.time())
Prefix = "Dib/"
#  pickle.dump(TOKEN, open("Token.p", "wb"))
TOKEN = pickle.load(open("Token.p", "rb"))

intents = discord.Intents().default()
intents.members = True
client = commands.Bot(command_prefix=Prefix, description="Extrem wichtiger Bot für extrem wichtige Sachen!",
                      intents=intents, help_command=PrettyHelp(no_category="Interactions"))

with open("Databse.json", "r") as f:
    Data = json.loads(f.read())


@client.event
async def on_ready():
    global Data
    with open("Databse.json", "r") as f:
        Data = json.loads(f.read())


class Interactions(commands.Cog):
    """Normal non-sexual interactions for you and your friends"""

    def __init__(ctx, bot):
        ctx.bot = bot

    @commands.command(pass_context=True, aliases=["hug"])
    async def Hug(self, ctx, user: discord.User):
        """Hugs the mentioned user."""

        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['hug']['Title'][random.randint(0, len(Data['hug']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} hugs {user.mention}.")
        e.set_image(url=f"{Data['hug']['Link'][random.randint(0, len(Data['hug']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["kiss"])
    async def Kiss(self, ctx, user: discord.User):
        """Kisses the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['kiss']['Title'][random.randint(0, len(Data['kiss']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} kisses {user.mention}.")
        e.set_image(url=f"{Data['kiss']['Link'][random.randint(0, len(Data['kiss']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["pat"])
    async def Pat(self, ctx, user: discord.User):
        """Pats the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['pat']['Title'][random.randint(0, len(Data['pat']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} pats {user.mention}.")
        e.set_image(url=f"{Data['pat']['Link'][random.randint(0, len(Data['pat']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["kill"])
    async def Kill(self, ctx, user: discord.User):
        """Kills the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['kill']['Title'][random.randint(0, len(Data['kill']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} kills {user.mention}.")
        e.set_image(url=f"{Data['kill']['Link'][random.randint(0, len(Data['kill']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["punch"])
    async def Punch(self, ctx, user: discord.User):
        """Punches the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['punch']['Title'][random.randint(0, len(Data['punch']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} punches {user.mention}.")
        e.set_image(url=f"{Data['punch']['Link'][random.randint(0, len(Data['punch']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["stomp"])
    async def Stomp(self, ctx, user: discord.User):
        """Stomps the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['stomp']['Title'][random.randint(0, len(Data['stomp']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} stomps {user.mention}.")
        e.set_image(url=f"{Data['stomp']['Link'][random.randint(0, len(Data['stomp']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["roundhouse"])
    async def Roundhouse(self, ctx, user: discord.User):
        """Performing a Roundhouse-Kick hitting the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['roundhouse']['Title'][random.randint(0, len(Data['roundhouse']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is roundhousing {user.mention}.")
        e.set_image(url=f"{Data['roundhouse']['Link'][random.randint(0, len(Data['roundhouse']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["slap"])
    async def Slap(self, ctx, user: discord.User):
        """Slaps the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['slap']['Title'][random.randint(0, len(Data['slap']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} slaps {user.mention}.")
        e.set_image(url=f"{Data['slap']['Link'][random.randint(0, len(Data['slap']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["talk"])
    async def Talk(self, ctx, user: discord.User, var="talk"):
        """Talk with the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} talks with {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["simp"])
    async def Simp(self, ctx, user: discord.User, var="simp"):
        """Simp the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} simps for {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["smalltalk", "SmallTalk"])
    async def Smalltalk(self, ctx, user: discord.User, var="smalltalk"):
        """Performing Smalltalk with mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is having a little talk with {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["suicide", "Suislide"])
    async def Suicide(self, ctx):
        """You commit suicide."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['suicide']['Title'][random.randint(0, len(Data['suicide']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} committed suicide.")
        e.set_image(url=f"{Data['suicide']['Link'][random.randint(0, len(Data['suicide']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["talk_about_my_fears", "TalkaboutFears"])
    async def TalkAboutFears(self, ctx, user: discord.User, var="talk_about_my_fears"):
        """Talks about fears with the mentioned User."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} talks about own fears with {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["cry"])
    async def Cry(self, ctx):
        """You cry."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['cry']['Title'][random.randint(0, len(Data['cry']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} cries.")
        e.set_image(url=f"{Data['cry']['Link'][random.randint(0, len(Data['cry']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["love"])
    async def Love(self, ctx, user: discord.User, var="love"):
        """Loving the mentioned User."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} loves {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["cuddle"])
    async def Cuddle(self, ctx, user: discord.User, var="cuddle"):
        """Cuddles with the mentioned User."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} cuddles with {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["nya", "NYA"])
    async def Nya(self, ctx, var="nya"):
        """NYA."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"NYAAA!!!!")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["hold_hands", "holdhands", "HH", "hh", "Holdhands"])
    async def HoldHands(self, ctx, user: discord.User, var="hold_hands"):
        """Holding hands with."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} holds Hands with {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["sing"])
    async def Sing(self, ctx, var="sing"):
        """Sings a Song."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} sings.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["Kisscheek", "kissCheek", "KISSCHEEK"])
    async def KissCheek(self, ctx, user: discord.User, var="kiss_cheek"):
        """Sings a Song."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} kisses the cheek of {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["Icetogether", "Ice_Together", "ice_together"])
    async def IceTogether(self, ctx, user: discord.User, var="ice_together"):
        """ Enjoys a tasty ice cream with the mentioned User."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} kisses the cheek of {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["CP", "Channelparty", "channelparty", "channelParty"])
    async def ChannelParty(self, ctx, var="channel_party"):
        """You throw a party for everyone in the Channel."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        Namelist = ""
        i = 0
        for members in ctx.channel.members:
            if members.name is not ctx.author.name:
                i = i + 1
                print(i)
                if i is not len(ctx.channel.members) - 1:
                    Namelist = Namelist + f"{members.mention}" + " and "
                else:
                    Namelist = Namelist + f"{members.mention}"
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} has a party with {Namelist}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["PP", "privateparty", "Privateparty", "privateParty"])
    async def PrivateParty(self, ctx):
        """You throw a party for the mentioned users."""
        random.seed(time.time() * time.time() + time.time())
        var = "private_party"
        e = discord.Embed()
        Namelist = ""
        i = 0
        add = 0
        for name in ctx.message.mentions:
            if name.name is ctx.author.name:
                add = add + 1
        for members in ctx.message.mentions:
            if members.name is not ctx.author.name:
                i = i + 1
                if i is not len(ctx.message.mentions) - add:
                    Namelist = Namelist + f"{members.mention}" + " and "
                else:
                    Namelist = Namelist + f"{members.mention}"
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} has a party with {Namelist}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["smirk"])
    async def Smirk(self, ctx, user: discord.User, var="smirk"):
        """ Smirks towards the mentioned User."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} Smirks towards {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["call"])
    async def Call(self, ctx, user: discord.User, var="call"):
        """ Calls the mentioned User."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} calls {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["play_with_hair", "Playwithhair", "PlayWithHair"])
    async def PlaywithHair(self, ctx, var="play_with_hair"):
        """ Just you playing with your Hair."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} plays with Hair.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["wink"])
    async def Wink(self, ctx, user: discord.User, var="wink"):
        """ Winks towards mentioned User."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} winks towards the {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["prettyeyes", "Prettyeyes", "prettyEyes", "Peyes"])
    async def PrettyEyes(self, ctx, user: discord.User):
        """You make pretty eyes to the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['prettyeyes']['Title'][random.randint(0, len(Data['prettyeyes']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} gives {user.mention} pretty eyes.")
        e.set_image(url=f"{Data['prettyeyes']['Link'][random.randint(0, len(Data['prettyeyes']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["smile"])
    async def Smile(self, ctx, user: discord.User):
        """You smiles towards the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['smile']['Title'][random.randint(0, len(Data['smile']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} smiles towards {user.mention}.")
        e.set_image(url=f"{Data['smile']['Link'][random.randint(0, len(Data['smile']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["grin"])
    async def Grin(self, ctx, user: discord.User):
        """You grin towards the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data['grin']['Title'][random.randint(0, len(Data['grin']['Title']) - 1)]}",
                    value=f"{ctx.author.mention} grins towards {user.mention}.")
        e.set_image(url=f"{Data['grin']['Link'][random.randint(0, len(Data['grin']['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["laugh"])
    async def Laugh(self, ctx, var="laugh"):
        """ You're laughing."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} starts laughing.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["cinema"])
    async def Cinema(self, ctx):
        """You go to the Cinema with the mentioned user(s)."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        Namelist = ""
        var = "cinema"
        i = 0
        add = 0
        for name in ctx.message.mentions:
            if name.name is ctx.author.name:
                add = add + 1
        for members in ctx.message.mentions:
            if members.name is not ctx.author.name:
                i = i + 1
                if i is not len(ctx.message.mentions) - add:
                    Namelist = Namelist + f"{members.mention}" + " and "
                else:
                    Namelist = Namelist + f"{members.mention}"
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is going to the Cinema with {Namelist}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["picknick", "PickNick", "Picnic", "picnic"])
    async def Picknick(self, ctx):
        """You have a Picnic with the mentioned user(s)."""
        random.seed(time.time() * time.time() + time.time())
        var = "picknick"
        e = discord.Embed()
        Namelist = ""
        i = 0
        add = 0
        for name in ctx.message.mentions:
            if name.name is ctx.author.name:
                add = add + 1
        for members in ctx.message.mentions:
            if members.name is not ctx.author.name:
                i = i + 1
                if i is not len(ctx.message.mentions) - add:
                    Namelist = Namelist + f"{members.mention}" + " and "
                else:
                    Namelist = Namelist + f"{members.mention}"
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} has a Picnic with {Namelist}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["eva", "Evangelion", "evangelion", ])
    async def Eva(self, ctx):
        """You're just appreciating a great Anime."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Evas['Title'][random.randint(0, len(Evas['Title']) - 1)]}",
                    value=f"Just a bit of depression and religion...")
        e.set_image(url=f"{Evas['Link'][random.randint(0, len(Evas['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["scream"])
    async def Scream(self, ctx, var="scream"):
        """ Screams."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} screams.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["insult"])
    async def Insult(self, ctx, user: discord.User, var="insult"):
        """ Insults the mentioned User."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} insults {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["bite"])
    async def Bite(self, ctx, user: discord.User, var="bite"):
        """ Bites the mentioned User."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} bites {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["vampire_bite", "VampBite", "Vampirebite"])
    async def VampireBite(self, ctx, user: discord.User, var="vampire_bite"):
        """ Bites the mentioned User and sucks the Blood."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} bites {user.mention} and sucked the Blood out.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True)
    async def ShareEarphones(self, ctx, user: discord.User, var="share_earphones"):
        """You share earphones with the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} shares earphones with {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["choke"])
    async def Choke(self, ctx, user: discord.User, var="choke"):
        """You choke the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} chokes {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["uppercut"])
    async def Uppercut(self, ctx, user: discord.User, var="uppercut"):
        """You're performing a Uppercut to punch the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is uppercutting {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["creepy_laugh", "creepylaugh"])
    async def CreepyLaugh(self, ctx, var="creepy_laugh"):
        """You're laughing quite creepily ."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is laughing creepy.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True)
    async def Blush(self, ctx, var="blush"):
        """You're blushing."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} blushes.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True)
    async def Dance(self, ctx, user: discord.User, var="dance"):
        """You dance with the mentioned User."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} dances with {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)


class NSFW_Interactions(commands.Cog):
    """Very NSFW Sexual Stuff you can do with each other"""

    def __init__(ctx, bot):
        ctx.bot = bot

    @commands.command(pass_context=True, aliases=["gangbang", "GangBang", "GANGBANG"])
    @commands.is_nsfw()
    async def Gangbang(self, ctx):
        """You have a Gangbang with the mentioned user(s)."""
        random.seed(time.time() * time.time() + time.time())
        var = "gangbang"
        e = discord.Embed()
        Namelist = ""
        i = 0
        add = 0
        for name in ctx.message.mentions:
            if name.name is ctx.author.name:
                add = add + 1
        for members in ctx.message.mentions:
            if members.name is not ctx.author.name:
                i = i + 1
                if i is not len(ctx.message.mentions) - add:
                    Namelist = Namelist + f"{members.mention}" + " and "
                else:
                    Namelist = Namelist + f"{members.mention}"
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} has a Gangbang with {Namelist}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["bdsm"])
    @commands.is_nsfw()
    async def BDSM(self, ctx):
        """You have a BDSM-Session with the mentioned user(s)."""
        random.seed(time.time() * time.time() + time.time())
        var = "bdsm"
        e = discord.Embed()
        Namelist = ""
        i = 0
        add = 0
        for name in ctx.message.mentions:
            if name.name is ctx.author.name:
                add = add + 1
        for members in ctx.message.mentions:
            if members.name is not ctx.author.name:
                i = i + 1
                if i is not len(ctx.message.mentions) - add:
                    Namelist = Namelist + f"{members.mention}" + " and "
                else:
                    Namelist = Namelist + f"{members.mention}"
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} has a BDSM-Session with {Namelist}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def Squirt(self, ctx):
        var = "squirt"
        """You're Squirting."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} squirts.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def Cum(self, ctx):
        var = "cum"
        """You're cumming."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} cums.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def Masturbate(self, ctx):
        var = "masturbate"
        """You're Masturbating."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} masturbates.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["Boobshake", "boobshake"])
    @commands.is_nsfw()
    async def BoobShake(self, ctx):
        var = "boobshake"
        """You're shaking your boobs."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} shakes those boobs.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["oral"])
    @commands.is_nsfw()
    async def Oral(self, ctx, user: discord.User):
        var = "oral"
        """You're having Oral Sex with the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is licking {user.mention}s privat Parts.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["vaginal"])
    @commands.is_nsfw()
    async def Vaginal(self, ctx, user: discord.User):
        var = "vaginal"
        """You're having Sex with the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is fucking {user.mention}s privat Parts.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["blowjob", "BJ", "bj"])
    @commands.is_nsfw()
    async def Blowjob(self, ctx, user: discord.User):
        var = "blowjob"
        """You're sucking the mentioned users Dick."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is blowing {user.mention}")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["Boobjob", "boobjob", "BoobJob", "Titfuck", "tityfuck"])
    @commands.is_nsfw()
    async def Tityfuck(self, ctx, user: discord.User):
        var = "tityfuck"
        """You're fucking the mentioned users Tits."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is fucking {user.mention}s tits")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["cowgirl", "CowGirl"])
    @commands.is_nsfw()
    async def Cowgirl(self, ctx, user: discord.User):
        var = "cowgirl"
        """You're having sex with the mentioned user in the Cowgirl position."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is fucking {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["missionary"])
    @commands.is_nsfw()
    async def Missionary(self, ctx, user: discord.User):
        var = "missionary"
        """You're having sex with the mentioned user in the Missionary position."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is fucking {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["doggy"])
    @commands.is_nsfw()
    async def Doggy(self, ctx, user: discord.User):
        var = "doggy"
        """You're having sex with the mentioned user in the Doggy position."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is fucking {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["anal"])
    @commands.is_nsfw()
    async def Anal(self, ctx, user: discord.User):
        var = "anal"
        """You're having anal sex with the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is fucking {user.mention}s Ass.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["Sexslap", "sexslap"])
    @commands.is_nsfw()
    async def SexSlap(self, ctx, user: discord.User):
        var = "sexslap"
        """You're slapping the mentioned user. But it's sexual."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is slapping {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["rape"])
    @commands.is_nsfw()
    async def Rape(self, ctx, user: discord.User):
        var = "rape"
        """You're raping the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is raping {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["incest"])
    @commands.is_nsfw()
    async def Incest(self, ctx, user: discord.User):
        var = "incest"
        """You're having incestuous Relations the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is having incest with {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["petting"])
    @commands.is_nsfw()
    async def Petting(self, ctx, user: discord.User):
        var = "petting"
        """You're petting the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is petting {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["play_with_boobs", "PwB", "BoobyPlay"])
    @commands.is_nsfw()
    async def PlayWithBoobs(self, ctx, user: discord.User):
        var = "play_with_boobs"
        """You're playing the mentioned users Boobs."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is playing with {user.mention}s Boobs.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["seduce"])
    @commands.is_nsfw()
    async def Seduce(self, ctx, user: discord.User):
        var = "seduce"
        """You're seducing the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is seducing {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["date"])
    @commands.is_nsfw()
    async def Date(self, ctx, user: discord.User):
        var = "date"
        """You're dating the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is dating {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["gay"])
    @commands.is_nsfw()
    async def Gay(self, ctx, user: discord.User):
        var = "gay"
        """You're gaying the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is gaying {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["Outdoors","Outdoorfuck"])
    @commands.is_nsfw()
    async def OutdoorFuck(self, ctx, user: discord.User):
        var = "outdoors_fuck"
        """You're fucking the mentioned user Outside."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is fucking {user.mention} in the open air.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["torture"])
    @commands.is_nsfw()
    async def Torture(self, ctx, user: discord.User):
        var = "torture"
        """You're torturing the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is torturing {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["DP","Doublepenetration"])
    @commands.is_nsfw()
    async def DoublePenetration(self, ctx, user: discord.User, user2: discord.User):
        var = "double_penetration"
        """You and the first mentioned user both fuck the second mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} and {user.mention} are fucking {user2.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["Sexbite","SB"])
    @commands.is_nsfw()
    async def SexBite(self, ctx, user: discord.User):
        var = "sexbite"
        """You bite the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} bites {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["feet","foot"])
    @commands.is_nsfw()
    async def Feet(self, ctx, user: discord.User):
        var = "feet"
        """You do stuff to the mentioned users Feet."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} does Stuff to {user.mention}s Feet.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["fist","fisting"])
    @commands.is_nsfw()
    async def Fisting(self, ctx, user: discord.User):
        var = "fisting"
        """You fist the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} fists {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["Cum_On","cum_on"])
    @commands.is_nsfw()
    async def CumOn(self, ctx, user: discord.User):
        var = "cum_on"
        """You cum on the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} cums on {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["Cum_In","cum_in"])
    @commands.is_nsfw()
    async def CumIn(self, ctx, user: discord.User):
        var = "cum_in"
        """You cum in the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} cums in {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["Cum_With","cum_with"])
    @commands.is_nsfw()
    async def CumWith(self, ctx, user: discord.User):
        var = "cum_with"
        """You cum with the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} cums with {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["Futa", "futa"])
    @commands.is_nsfw()
    async def Futanari(self, ctx, user: discord.User):
        var = "futanari"
        """You fuck the mentioned user as a Futanari."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} fucks {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["Sexchoke"])
    @commands.is_nsfw()
    async def SexChoke(self, ctx, user: discord.User):
        var = "sexchoke"
        """You choke the mentioned user. But Sexy..."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} chokes {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["watersports","ws"])
    @commands.is_nsfw()
    async def Watersports(self, ctx, user: discord.User):
        var = "watersports"
        """You urinate on mentioned user. But Sexy..."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} pisses on {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["bestiality"])
    @commands.is_nsfw()
    async def Bestiality(self, ctx):
        var = "bestiality"
        """You fuck an Animal."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} is fucked by.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["bondage"])
    @commands.is_nsfw()
    async def Bondage(self, ctx, user: discord.User):
        var = "bondage"
        """You tie up the mentioned user. But Sexy..."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} ties up {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["furry"])
    @commands.is_nsfw()
    async def Furry(self, ctx, user: discord.User):
        var = "furry"
        """You have Sex with the mentioned user. But as an Animal ?"""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} fucks {user.mention} Fursona.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)

    @commands.command(pass_context=True, aliases=["molest"])
    @commands.is_nsfw()
    async def Molest(self, ctx, user: discord.User):
        var = "molest"
        """You molest the mentioned user."""
        random.seed(time.time() * time.time() + time.time())
        e = discord.Embed()
        e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                    value=f"{ctx.author.mention} molests {user.mention}.")
        e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
        await ctx.send(embed=e)


client.add_cog(NSFW_Interactions(client))
client.add_cog(Interactions(client))
client.run(TOKEN)
