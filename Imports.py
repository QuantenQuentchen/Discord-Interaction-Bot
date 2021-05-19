import discord
import time
from discord.ext import commands, tasks
import random
import pickle
from discord_slash import SlashCommand, SlashContext, SlashCommandOptionType
import random
import time
import asyncio
import discord
import json
import numpy as np
import pickle
from datetime import timedelta
import openpyxl

Prefix = "Dib/"
#  pickle.dump(TOKEN, open("Token.p", "wb"))
TOKEN = pickle.load(open("Token.p", "rb"))
# TOKEN = "ODMyNzM4MjY5NDIyNDIwMDI4.YHoJ8g.tjQj20cdhNXQOM1qej9syyIw6qc"
intents = discord.Intents().all()
intents.members = True
client = commands.Bot(command_prefix=Prefix, description="Stuff to do to others and yourself. May include NSFW!",
                      intents=intents)  # , help_command=PrettyHelp(no_category="Interactions"))

slash = SlashCommand(client, sync_commands=True)