from Imports import *

ActList = []
Memberlist = {}
Gender = ["Male", "Female"]

def getGuilds():
    Serverlist = []
    for guild in client.guilds:
        Serverlist.append(guild.id)
    return True


def integrate(Object):
    Memberlist[Object.id] = Object
    pickle.dump(Memberlist, open("Test.p", "wb"))


def MakeChild(Mother, Father, Adoption):
    if not Adoption:
        ChildGender = Gender[random.randint(0, len(Gender) - 1)]
        ChildName = input("Name: ")
        ChildSex = input("Sex: ")
        Child = Member(ChildGender, 0, ChildName, False, ChildSex)  # , Special().gen_gen(Mother, Father))
    else:
        pass
    Mother.add_Offspring(Child)
    Father.add_Offspring(Child)

class Interaction:
    Pos_Emoj = "✅"
    Neg_Emoj = "❌"
    Cockie = ":cookie:"  # e8f23286ca11816c9ab8c145de57793d>"
    Pos_Emoj_id = "843227220512079893"
    Neg_Emoj_id = "843227220512079893"
    Newline = "\n"
    AuthorStandin = "//Author//"
    TargetStandin = "//Target//"
    Emoji = {"✅": True, "❌": False}

    def __init__(self, command, aliases, action, verb, description, data_name, alone, number, everyone, nsfw, Agree,
                 category):
        self.command: str = command
        self.aliases: list = aliases
        self.action: str = action
        self.description: str = description
        self.data_name: str = data_name
        self.alone: bool = alone
        self.number: int = number
        self.everyone: bool = everyone
        self.nsfw: bool = nsfw
        self.category: str = category
        self.Verb: str = verb
        with open("Databse.json", "r") as f:
            self.Data = json.loads(f.read())
        if self.command.lower() not in self.aliases:
            self.aliases.append(self.command.lower())
        self.Agree: bool = Agree
        self.options = []
        if self.number is False and self.alone is False:
            for mention in range(50):
                self.options.append({
                    "name": f"target{mention}",
                    "description": f"Your {mention} User",
                    "required": True,
                    "type": 6
                })
        if self.number is not False and not self.everyone:
            for mention in range(self.number):
                self.options.append({
                    "name": f"target{mention + 1}",
                    "description": f"Your {mention + 1} User",
                    "required": True,
                    "type": 6
                })
        ActList.append(self)

    def get_list(self):
        List = []
        for guild in client.guilds:
            List.append(guild.id)
        return List

    def Command(self):
        var = self.data_name
        Description = self.description
        Data = self.Data
        Actio = self.action
        Everyone = self.everyone
        Single = self.alone
        NSFW = self.nsfw
        Newline = self.Newline
        AuthorStandin = self.AuthorStandin
        TargetStandin = self.TargetStandin
        Neg_Emoj = self.Neg_Emoj
        Pos_Emoj = self.Pos_Emoj
        Pos_Emoj_id = int(self.Pos_Emoj_id)
        Neg_Emoj_id = int(self.Neg_Emoj_id)
        Verb = self.Verb
        Emoji = self.Emoji
        Cockie = self.Cockie
        options = self.options
        if Single:
            Number = 0
        Number = self.number
        Agree = self.Agree

        @slash.slash(guild_ids=[701051127612964964], description=Description, name=self.command,
                     options=options)  # ,aliases=self.aliases)
        async def Cummand(ctx: SlashContext, *args, **kwargs):
            Inputlist = []
            for mention in ctx.args:
                Inputlist.append(mention)
            Author = ctx.author
            random.seed(time.time() * time.time() + time.time())
            Namelist = ""
            NSFWpile = ""
            Memberlist = []
            Memberidlist = []
            Yeslist = {}
            Nopelist = []
            Yespile = []
            i = 0
            add = 0
            Action = Actio.replace(AuthorStandin, str(Author.mention))

            PoMo = client.get_emoji(843236144803741716)
            NeMo = client.get_emoji(843236279364878346)

            for name in Inputlist:
                if name.name is Author.name or name.bot:
                    add = add + 1
            for members in Inputlist:
                if members.name is not Author.name:
                    i = i + 1
                    if i is not len(Inputlist) - add:
                        Namelist = Namelist + f"{members.mention}" + " and "
                        Memberlist.append(members)
                        Memberidlist.append(members.id)
                    else:
                        Namelist = Namelist + f"{members.mention}"
                        Memberlist.append(members)
                        Memberidlist.append(members.id)
            Action = Action.replace(TargetStandin, Namelist)

            async def check_msg(Timeout):
                Check = discord.Embed(title="And the Results are in...")
                if not any(Yeslist.values()):
                    await Rejected()
                    return
                else:
                    Check.add_field(name=f"Agreed:",
                                    value=f"{Newline.join(f'{user.mention}' for user in Memberlist)}")
                    Timeouts = []
                    if False in Yeslist.values():
                        for user, att in Yeslist.items():
                            if not att:
                                Nopelist.append(user)
                        Check.add_field(
                            name=f"Declined:",
                            value=f"{Newline.join(f'{user.mention}' for user in Nopelist)}")
                    if Yeslist.keys() != Memberlist:
                        for i in Memberlist:
                            if i not in Yeslist:
                                Timeouts.append(i)
                        if Timeout:
                            Check.add_field(
                                name=f"Timeout:",
                                value=f"{Newline.join(f'{user.mention}' for user in Timeouts)}")
                    Poll_msg = await ctx.send(embed=Check)
                    await main_int()
                    await asyncio.sleep(15)
                    await Poll_msg.delete()

            async def main_int():  # if str(reaction.emoji) == Pos_Emoj:
                global inter
                global msg
                random.seed(time.time() * time.time() + time.time())
                e = discord.Embed()
                e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                            value=f"{Action}.")  # {Newline.join(f'{user.mention}' for user in Yeslist)}.")
                e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
                inter = await ctx.send(embed=e)
                await asyncio.sleep(3)
                await msg.delete()

            async def Korb():
                await ctx.send(f"Sorry {Author.mention} But that's more of a Multiplayer Activity. But here have "
                               f"some Cookies:")
                await ctx.send(f"{Cockie}{Cockie}{Cockie}{Cockie}")

            async def Rejected():  # str(reaction.emoji) == Neg_Emoj:
                nope = discord.Embed()
                nope.add_field(name=f"Well you tried...", value=f"{Author.mention}")
                nope.set_image(
                    url="https://media1.tenor.com/images/3fd96f4dcba48de453f2ab3acd657b53/tenor.gif?itemid=14358509")
                await ctx.send(embed=nope)

            async def Opener():
                global msg
                if Everyone is True:
                    cum = discord.Embed()
                    cum.add_field(name=f"Your big decision:",
                                  value=f"{Author.mention} wants to {Verb.lower()} you. \n Click on {Pos_Emoj} to accept the Offer. \n "
                                        f"Click "
                                        f"on {Neg_Emoj} to decline the Offer.")
                    msg = await ctx.send(content=f'{" ".join(f"{user.mention}" for user in Memberlist)}', embed=cum)
                    await msg.add_reaction(f"<a:{Pos_Emoj}")
                    await msg.add_reaction(f"<a:{Neg_Emoj}")
                    return True
                elif Number is None:
                    cum = discord.Embed()
                    cum.add_field(name=f"Your big decision:",
                                  value=f"{Author.mention} wants to {Verb.lower()} you. \n Click on {Pos_Emoj} to "
                                        f"accept the Offer. \n "
                                        f"Click "
                                        f"on {Neg_Emoj} to decline the Offer.")
                    msg = await ctx.send(content=f'{" ".join(f"{user.mention}" for user in Inputlist)}',
                                         embed=cum)
                    await msg.add_reaction(f"<a:{Pos_Emoj}")
                    await msg.add_reaction(f"<a:{Neg_Emoj}")
                    return True

                elif Number != len(Inputlist) or not Inputlist:
                    Much = discord.Embed()
                    Much.add_field(name="Sorry bud.",
                                   value=f"You can only {Verb.lower()} {Number} and not {len(Inputlist)}.")
                    msg = await ctx.send(content=f"{Author.mention}", embed=Much)
                    return False
                else:
                    cum = discord.Embed()
                    cum.add_field(name=f"Your big decision:",
                                  value=f"{Author.mention} wants to {Verb.lower()} you. \n Click on {Pos_Emoj} to "
                                        f"accept the Offer. \n "
                                        f"Click "
                                        f"on {Neg_Emoj} to decline the Offer.")
                    msg = await ctx.send(content=f'{" ".join(f"{user.mention}" for user in Inputlist)}',
                                         embed=cum)
                    await msg.add_reaction("✅")
                    await msg.add_reaction("❌")
                    return True

            def check(reaction, user):

                if user in Memberlist:
                    Yeslist[user] = Emoji[reaction.emoji]
                    Yespile.append(user.id)
                return Yespile == Memberidlist and (
                        str(reaction.emoji) == Pos_Emoj or str(reaction.emoji) == Neg_Emoj)

            async def NSFNo():
                for Channel in ctx.guild.channels:
                    if Channel.type == discord.ChannelType.text:
                        if Channel.is_nsfw():
                            NSFWpile = NSFWpile + str(Channel.mention) + "\n"

                Nsfno = discord.Embed(title="Get a room you two.")
                Nsfno.set_image(url="https://i.chzbgr.com/full/8474882048/h22A2BFCE/get-a-room.gif")
                Nsfno.add_field(name="You could do it in those Channels:", value=f"NSFW Channels:\n{NSFWpile}")
                await ctx.send(content=f"{Author.mention}", embed=Nsfno)
                return

            if not Agree:
                await main_int()
                return

            if Everyone:
                Namelist = ""
                i = 0
                for members in ctx.channel.members:
                    if members.name is not Author.name:
                        i = i + 1
                        if i is not len(ctx.channel.members) - 1:
                            Namelist = Namelist + f"{members.mention}" + " and "
                        else:
                            Namelist = Namelist + f"{members.mention}"

            if Inputlist[0].bot or Inputlist[0] == Author and len(
                    Inputlist) == 1 and not Single:
                await Korb()
                return
            if NSFW and not ctx.channel.is_nsfw():
                NSFNo()
            if Namelist:
                Action = Action.replace(TargetStandin, Namelist)
            if not Single:
                if not await Opener():
                    return
                try:
                    await client.wait_for('reaction_add', timeout=60.0, check=check)
                    await check_msg(False)

                except asyncio.TimeoutError:
                    if not Yeslist:
                        Err = discord.Embed()
                        Err.add_field(name="Sorry but you waited too long!",
                                      value="You have 60 Seconds after you're asked.")
                        await ctx.send(embed=Err)
                    else:
                        await check_msg(True)
                    return
            else:
                await main_int()
                return

    def Kommand(self):
        var = self.data_name
        Description = self.description
        Data = self.Data
        Actio = self.action
        Everyone = self.everyone
        Single = self.alone
        NSFW = self.nsfw
        Newline = self.Newline
        AuthorStandin = self.AuthorStandin
        TargetStandin = self.TargetStandin
        Neg_Emoj = self.Neg_Emoj
        Pos_Emoj = self.Pos_Emoj
        Pos_Emoj_id = int(self.Pos_Emoj_id)
        Neg_Emoj_id = int(self.Neg_Emoj_id)
        Verb = self.Verb
        Emoji = self.Emoji
        Cockie = self.Cockie
        options = self.options
        if Single:
            Number = 0
        Number = self.number
        Agree = self.Agree

        @client.command(pass_context=True, description=Description, name=self.command, aliases=self.aliases)
        async def Cummand(ctx):
            Inputlist = []
            for mention in ctx.message.mentions:
                Inputlist.append(mention)
            Author = ctx.message.author
            random.seed(time.time() * time.time() + time.time())
            Namelist = ""
            NSFWpile = ""
            Memberlist = []
            Memberidlist = []
            Yeslist = {}
            Nopelist = []
            Yespile = []
            i = 0
            add = 0
            Action = Actio.replace(AuthorStandin, str(Author.mention))
            PoMo = client.get_emoji(843236144803741716)
            NeMo = client.get_emoji(843236279364878346)

            for name in Inputlist:
                if name.name is Author.name or name.bot:
                    add = add + 1
            for members in Inputlist:
                if members.name is not Author.name:
                    i = i + 1
                    if i is not len(Inputlist) - add:
                        Namelist = Namelist + f"{members.mention}" + " and "
                        Memberlist.append(members)
                        Memberidlist.append(members.id)
                    else:
                        Namelist = Namelist + f"{members.mention}"
                        Memberlist.append(members)
                        Memberidlist.append(members.id)
            Action = Action.replace(TargetStandin, Namelist)

            async def check_msg(Timeout):
                Check = discord.Embed(title="And the Results are in...")
                if not any(Yeslist.values()):
                    await Rejected()
                    return
                else:
                    Check.add_field(name=f"Agreed:",
                                    value=f"{Newline.join(f'{user.mention}' for user in Memberlist)}")
                    Timeouts = []
                    if False in Yeslist.values():
                        for user, att in Yeslist.items():
                            if not att:
                                Nopelist.append(user)
                        Check.add_field(
                            name=f"Declined:",
                            value=f"{Newline.join(f'{user.mention}' for user in Nopelist)}")
                    if Yeslist.keys() != Memberlist:
                        for i in Memberlist:
                            if i not in Yeslist:
                                Timeouts.append(i)
                        if Timeout:
                            Check.add_field(
                                name=f"Timeout:",
                                value=f"{Newline.join(f'{user.mention}' for user in Timeouts)}")
                    Poll_msg = await ctx.send(embed=Check)
                    await main_int()
                    await asyncio.sleep(15)
                    await Poll_msg.delete()

            async def main_int():  # if str(reaction.emoji) == Pos_Emoj:
                global inter
                global msg
                random.seed(time.time() * time.time() + time.time())
                e = discord.Embed()
                e.add_field(name=f"{Data[var]['Title'][random.randint(0, len(Data[var]['Title']) - 1)]}",
                            value=f"{Action}.")  # {Newline.join(f'{user.mention}' for user in Yeslist)}.")
                e.set_image(url=f"{Data[var]['Link'][random.randint(0, len(Data[var]['Link']) - 1)]}")
                inter = await ctx.send(embed=e)
                await asyncio.sleep(3)
                await msg.delete()

            async def Korb():
                await ctx.send(f"Sorry {Author.mention} But that's more of a Multiplayer Activity. But here have "
                               f"some Cookies:")
                await ctx.send(f"{Cockie}{Cockie}{Cockie}{Cockie}")

            async def Rejected():  # str(reaction.emoji) == Neg_Emoj:
                nope = discord.Embed()
                nope.add_field(name=f"Well you tried...", value=f"{Author.mention}")
                nope.set_image(
                    url="https://media1.tenor.com/images/3fd96f4dcba48de453f2ab3acd657b53/tenor.gif?itemid=14358509")
                await ctx.send(embed=nope)

            async def Opener():
                global msg
                if Everyone is True:
                    cum = discord.Embed()
                    cum.add_field(name=f"Your big decision:",
                                  value=f"{Author.mention} wants to {Verb.lower()} you. \n Click on {Pos_Emoj} to accept the Offer. \n "
                                        f"Click "
                                        f"on {Neg_Emoj} to decline the Offer.")
                    msg = await ctx.send(content=f'{" ".join(f"{user.mention}" for user in Memberlist)}', embed=cum)
                    await msg.add_reaction(f"<a:{Pos_Emoj}")
                    await msg.add_reaction(f"<a:{Neg_Emoj}")
                    return True
                elif Number is None:
                    cum = discord.Embed()
                    cum.add_field(name=f"Your big decision:",
                                  value=f"{Author.mention} wants to {Verb.lower()} you. \n Click on {Pos_Emoj} to "
                                        f"accept the Offer. \n "
                                        f"Click "
                                        f"on {Neg_Emoj} to decline the Offer.")
                    msg = await ctx.send(content=f'{" ".join(f"{user.mention}" for user in Inputlist)}',
                                         embed=cum)
                    await msg.add_reaction(f"<a:{Pos_Emoj}")
                    await msg.add_reaction(f"<a:{Neg_Emoj}")
                    return True

                elif Number != len(Inputlist) or not Inputlist:
                    Much = discord.Embed()
                    Much.add_field(name="Sorry bud.",
                                   value=f"You can only {Verb.lower()} {Number} and not {len(Inputlist)}.")
                    msg = await ctx.send(content=f"{Author.mention}", embed=Much)
                    return False
                else:
                    cum = discord.Embed()
                    cum.add_field(name=f"Your big decision:",
                                  value=f"{Author.mention} wants to {Verb.lower()} you. \n Click on {Pos_Emoj} to "
                                        f"accept the Offer. \n "
                                        f"Click "
                                        f"on {Neg_Emoj} to decline the Offer.")
                    msg = await ctx.send(content=f'{" ".join(f"{user.mention}" for user in Inputlist)}',
                                         embed=cum)
                    await msg.add_reaction("✅")
                    await msg.add_reaction("❌")
                    return True

            def check(reaction, user):

                if user in Memberlist:
                    Yeslist[user] = Emoji[reaction.emoji]
                    Yespile.append(user.id)
                return Yespile == Memberidlist and (
                        str(reaction.emoji) == Pos_Emoj or str(reaction.emoji) == Neg_Emoj)

            async def NSFNo():
                for Channel in ctx.guild.channels:
                    if Channel.type == discord.ChannelType.text:
                        if Channel.is_nsfw():
                            NSFWpile = NSFWpile + str(Channel.mention) + "\n"

                Nsfno = discord.Embed(title="Get a room you two.")
                Nsfno.set_image(url="https://i.chzbgr.com/full/8474882048/h22A2BFCE/get-a-room.gif")
                Nsfno.add_field(name="You could do it in those Channels:", value=f"NSFW Channels:\n{NSFWpile}")
                await ctx.send(content=f"{Author.mention}", embed=Nsfno)
                return

            if not Agree:
                await main_int()
                return

            if Everyone:
                Namelist = ""
                i = 0
                for members in ctx.channel.members:
                    if members.name is not Author.name:
                        i = i + 1
                        if i is not len(ctx.channel.members) - 1:
                            Namelist = Namelist + f"{members.mention}" + " and "
                        else:
                            Namelist = Namelist + f"{members.mention}"

            if Inputlist[0].bot or Inputlist[0] == Author and len(
                    Inputlist) == 1 and not Single:
                await Korb()
                return
            if NSFW and not ctx.channel.is_nsfw():
                NSFNo()
            if Namelist:
                Action = Action.replace(TargetStandin, Namelist)
            if not Single:
                if not await Opener():
                    return
                try:
                    await client.wait_for('reaction_add', timeout=60.0, check=check)
                    await check_msg(False)

                except asyncio.TimeoutError:
                    if not Yeslist:
                        Err = discord.Embed()
                        Err.add_field(name="Sorry but you waited too long!",
                                      value="You have 60 Seconds after you're asked.")
                        await ctx.send(embed=Err)
                    else:
                        await check_msg(True)
                    return
            else:
                await main_int()
                return

    def more(self):
        pass


class Special:
    stats = {}

    def __init__(self):
        self.Min = 1
        self.Max = 10
        self.Num = 7
        self.Avab_Points = 5
        self.stats = {
            "Strength": 5,
            "Perception": 5,
            "Endurance": 5,
            "Charism": 5,
            "Intelligence": 5,
            "Agility": 5,
            "Luck": 5
        }

    def random_gen(self):
        def Less_Check():
            random.seed()
            rando = random.randint(1, self.Num + 1)
            return rando

        while Less_Check() is not self.Num + 1:
            Less_Role = Less_Check()
            Less_Index = Less_Role - 3
            Vals = list(self.stats.values())[Less_Index]
            if Vals >= 1:
                self.stats[list(self.stats.keys())[Less_Index]] = Vals - 1
                self.Avab_Points = self.Avab_Points + 1
        # print(f"Reduction Completed: {self.stats} with {self.Avab_Points} Points")
        while self.Avab_Points > 1:
            for key, value in self.stats.items():
                if self.Avab_Points >= 0 and random.randint(0, 1):
                    # print(f"{key} : {value}")
                    # print(f"Points: {self.Avab_Points}")
                    self.Avab_Points = self.Avab_Points - 1
                    self.stats[key] = value + 1
        print(self.stats)
        # return self.stats

    def gen_gen(self, mother, father):
        print(mother.special.stats["Luck"])


class Member:
    def __init__(self, Gender, Age, Name, User, Sexuality):
        self.id = len(Memberlist)
        self.Gender = Gender
        self.Age = Age
        self.Name = Name
        self.User = User
        self.Siblings = []
        self.Offspring = []
        self.Spouse = []
        self.FormerSpouse = []
        self.Parents = []
        self.sexuality = Sexuality
        self.special = Special()
        integrate(self)
        self.special.random_gen()
        # self.special.random_gen()

    def add_Parents(self, Parent):
        if Parent not in self.Parents:
            self.Parents.append(Parent)

    def add_Spouse(self, Spouse):
        if Spouse not in self.Siblings:
            self.Siblings.append(Spouse)

    def add_sibling(self, Sib_User):
        if Sib_User not in self.Siblings:
            print(type(Sib_User))
            self.Siblings.append(Sib_User)
            if self not in Sib_User.Siblings:
                Sib_User.add_sibling(self)
                print(Sib_User.Siblings)

    def add_Offspring(self, Off_User):
        if Off_User not in self.Offspring:
            if self not in Off_User.Parents:
                Off_User.add_Parents(self)
            for Partners in self.Spouse:
                Off_User.add_Parents(Partners)
            self.Offspring.append(Off_User)

    def return_Parents(self):
        return self.Parents

    def printRelation(self, degree):
        parnum = 0
        for Parents in self.Parents:
            parnum = + 1
            print(f"{parnum}: {Parents.Name} with those {Parents.return_Parents()}")

    def getAll(self):
        pass


class Event:
    def __init__(self):
        pass
