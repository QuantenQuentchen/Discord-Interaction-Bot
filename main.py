from Imports import *
import Interaction as Inter
import Command_Classes as CC

random.seed(time.time() * time.time() + time.time())





@client.event
async def on_ready():
    CC.getGuilds()
    print("Done")


Inter.InitAll()
client.run(TOKEN)
