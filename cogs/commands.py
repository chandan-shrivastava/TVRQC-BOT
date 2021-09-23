import platform
import random
import asyncio
import json
import aiohttp
import discord
import os
import os.path
from discord import message
from discord.ext import commands
from replit import db
from datetime import datetime
import pytz
from dislash import InteractionClient, ActionRow, Button, ButtonStyle
import convertapi
owners = [
    482849624030314525
]
# https://discordapp.com/oauth2/authorize?&client_id=881932098993270784&scope=bot&permissions=8
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
db["team-1"] = 0
db["team-2"] = 0
db["team-3"] = 0
db["team-4"] = 0
db["team-5"] = 0
db["team-6"] = 0
db["team-7"] = 0
db["team-8"] = 0
db["team-9"] = 0
db["team-1-answer"] = 0
db["team-2-answer"] = 0
db["team-3-answer"] = 0
db["team-4-answer"] = 0
db["team-5-answer"] = 0
db["team-6-answer"] = 0
db["team-7-answer"] = 0
db["team-8-answer"] = 0
db["team-9-answer"] = 0

slidecount=int(1)

teamchannels = [
        708749820839592036,
691293346848833578,
691293394730876988,
691293457544904785,
691293526717235300,
691293570396586096,
691293621214904320,
691293670065831986,
709008205975519283
]

class Help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, context):
        """
        List all commands. (!help)
        """
        prefix = "!"
        if not isinstance(prefix, str):
            prefix = prefix[0]
        embed = discord.Embed(
            title="", description="List of available commands:", color=0x42F56C)
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i.lower())
            commands = cog.get_commands()
            command_list = [command.name for command in commands]
            command_description = [command.help for command in commands]
            help_text = '\n'.join(
                f'{prefix}{n} - {h}' for n, h in zip(command_list, command_description))
            embed.add_field(name=i.capitalize(),
                            value=f'```{help_text}```', inline=False)
        await context.send(embed=embed)

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################

class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="info", aliases=["botinfo"])
    async def info(self, context):
        """
        Get some useful (or not) information about the bot. (!info)
        """
        embed = discord.Embed(
            description="Quiz Bot",
            color=0x42F56C
        )
        embed.set_author(
            name="Bot Information"
        )
        embed.add_field(
            name="Owner:",
            value="XX#1399",
            inline=True
        )
        embed.add_field(
            name="Python Version:",
            value=f"{platform.python_version()}",
            inline=True
        )
        embed.add_field(
            name="Prefix:",
            value="!",
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {context.message.author}({context.author.display_name})"
        )
        await context.send(embed=embed)

    @commands.command(name="ping")
    async def ping(self, context):
        """
        Check if the bot is alive. (!ping)
        """
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"The bot latency is {round(self.bot.latency * 1000)}ms.",
            color=0x42F56C
        )
        await context.send(embed=embed)

    @commands.command(name="poll")
    async def poll(self, context, *, title):
        """
        Create a poll where members can vote. (!poll *title*)
        """
        embed = discord.Embed(
            title="A new poll has been created!",
            description=f"{title}",
            color=0x42F56C
        )
        embed.set_footer(
            text=f"Poll created by: {context.message.author}({context.author.display_name}) • React to vote!"
        )
        embed_message = await context.send(embed=embed)
        await embed_message.add_reaction("1️⃣")
        await embed_message.add_reaction("2️⃣")
        await embed_message.add_reaction("3️⃣")
        await embed_message.add_reaction("4️⃣")
        await embed_message.add_reaction("5️⃣")
        await embed_message.add_reaction("6️⃣")
        await embed_message.add_reaction("7️⃣")
        await embed_message.add_reaction("8️⃣")
        await embed_message.add_reaction("9️⃣")

    @commands.command(name="answer", aliases=["ans"])
    @commands.cooldown(1, 60, commands.BucketType.channel)
    async def f(self, context, *, args):
        """
        Finalise answer. (!ans *answer*)
        """
        IST = pytz.timezone('Asia/Kolkata')
        datetime_ist = datetime.now(IST)
        curr_clock=datetime_ist.strftime('%H:%M:%S')
        channel1=context.message.channel.name
        channel = self.bot.get_channel(890126023251882034)
        channel2=channel1+"-answer"
        db[channel2]=args
        embed1 = discord.Embed(
        title="Final Answer locked",
        description=f"Answer: ```{args}```",
        color=0x42F56C
        )
        embed1.set_footer(
            text=f"Answered by {context.message.author}({context.author.display_name}) at {curr_clock}."
        )
        embed = discord.Embed(
        title=f"Answer received from {channel1}",
        description=f"```{args}```",
        color=0x42F56C
        )
        embed.set_footer(
            text=f"Answered in {channel1} by {context.message.author}({context.author.display_name}) at {curr_clock}"
        )
        await context.reply(embed=embed1)
        await channel.send(embed=embed)
    
    @commands.command(name="pass")
    async def passed(self, context):
        """
        Passes to next team. (!pass)
        """
        IST = pytz.timezone('Asia/Kolkata')
        datetime_ist = datetime.now(IST)
        curr_clock=datetime_ist.strftime('%H:%M:%S')
        channel = self.bot.get_channel(890126023251882034)
        size = len(context.message.channel.name)
        nextteam=context.message.channel.name[size-1]
        nextteam=int(nextteam)
        nextteam=nextteam+1
        if nextteam==10:
            nextteam=1
        channel1 = discord.utils.get(context.guild.channels, name=f"team-{nextteam}")
        embed = discord.Embed(
            title=f"Received pass from {context.message.channel.name}",
            color=0x42F56C
        )
        embed.set_footer(
            text=f"Passed by {context.message.author}({context.author.display_name}) at {curr_clock}."
        )
        await channel.send(embed=embed)
        await channel1.send("Received Pass from previous team. Its your turn.")

    @commands.command(name="join")
    async def joined(self, context, teamno):
        """
        Join team. (!join *team no*)
        """
        embed = discord.Embed(
            title=f"{context.message.author}({context.author.display_name}) -> Team- {teamno}",
            description=f"{context.message.author}({context.author.display_name}) joined Team-{teamno}",
            color=0x42F56C
        )
        embed.set_footer(
            text=f"You can now see team-{teamno} channel."
        )
        try:
            await context.message.author.add_roles(discord.utils.get(context.message.author.guild.roles, name=f"team{teamno}"))
            await context.send(embed=embed)
        except:
            await context.send(f"Role team{teamno} does not exist")
    
    @commands.command(name="leave")
    async def leaved(self, context, teamno):
        """
        Leave team. (!leave *team no*)
        """
        embed = discord.Embed(
            title=f"{context.message.author}({context.author.display_name}) xx Team- {teamno}",
            description=f"{context.message.author}({context.author.display_name}) left Team-{teamno}",
            color=0x42F56C
        )
        embed.set_footer(
            text=f"You now cannot see team-{teamno} channel."
        )
        try:
            await context.message.author.remove_roles(discord.utils.get(context.message.author.guild.roles, name=f"team{teamno}"))
            await context.send(embed=embed)
        except:
            await context.send(f"Role team{teamno} does not exist or you dont have that role")

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################

class owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member, *, reason="Not specified"):
        """
        Kick a user out of the server. (!kick *User* *Reason*)
        """
        if context.message.author.id in owners:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    title="Error!",
                    description="User has Admin permissions.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
            else:
                try:
                    await member.kick(reason=reason)
                    embed = discord.Embed(
                        title="User Kicked!",
                        description=f"**{member}** was kicked by **{context.message.author}({context.author.display_name})**!",
                        color=0x42F56C
                    )
                    embed.add_field(
                        name="Reason:",
                        value=reason
                    )
                    await context.send(embed=embed)
                    try:
                        await member.send(
                            f"You were kicked by **{context.message.author}({context.author.display_name})**!\nReason: {reason}"
                        )
                    except:
                        pass
                except:
                    embed = discord.Embed(
                        title="Error!",
                        description="An error occurred while trying to kick the user. Make sure my role is above the role of the user you want to kick.",
                        color=0xE02B2B
                    )
                    await context.message.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.command(name="nick")
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, context, member: discord.Member, *, nickname=None):
        """
        Change the nickname of a user on a server. (!nick *User* *Nickname*)
        """
        if context.message.author.id in owners:
            try:
                await member.edit(nick=nickname)
                embed = discord.Embed(
                    title="Changed Nickname!",
                    description=f"**{member}'s** new nickname is **{nickname}**!",
                    color=0x42F56C
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description="An error occurred while trying to change the nickname of the user. Make sure my role is above the role of the user you want to change the nickname.",
                    color=0xE02B2B
                )
                await context.message.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member: discord.Member, *, reason="Not specified"):
        """
        Bans a user from the server. (!ban *User* *Reason*)
        """
        if context.message.author.id in owners:
            try:
                if member.guild_permissions.administrator:
                    embed = discord.Embed(
                        title="Error!",
                        description="User has Admin permissions.",
                        color=0xE02B2B
                    )
                    await context.send(embed=embed)
                else:
                    await member.ban(reason=reason)
                    embed = discord.Embed(
                        title="User Banned!",
                        description=f"**{member}** was banned by **{context.message.author}({context.author.display_name})**!",
                        color=0x42F56C
                    )
                    embed.add_field(
                        name="Reason:",
                        value=reason
                    )
                    await context.send(embed=embed)
                    await member.send(f"You were banned by **{context.message.author}({context.author.display_name})**!\nReason: {reason}")
            except:
                embed = discord.Embed(
                    title="Error!",
                    description="An error occurred while trying to ban the user. Make sure my role is above the role of the user you want to ban.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.command(name="warn")
    @commands.has_permissions(manage_messages=True)
    async def warn(self, context, member: discord.Member, *, reason="Not specified"):
        """
        Warns a user in his private messages. (!warn *User* *Reason*)
        """
        if context.message.author.id in owners:
            embed = discord.Embed(
                title="User Warned!",
                description=f"**{member}** was warned by **{context.message.author}({context.author.display_name})**!",
                color=0x42F56C
            )
            embed.add_field(
                name="Reason:",
                value=reason
            )
            await context.send(embed=embed)
            try:
                await member.send(f"You were warned by **{context.message.author}({context.author.display_name})**!\nReason: {reason}")
            except:
                pass
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    async def purge(self, context, amount):
        """
        Delete a number of messages. (!purge *Number*)
        """
        if context.message.author.id in owners:
            try:
                amount = int(amount)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description=f"`{amount}` is not a valid number.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
                return
            if amount < 1:
                embed = discord.Embed(
                    title="Error!",
                    description=f"`{amount}` is not a valid number.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
                return
            purged_messages = await context.message.channel.purge(limit=amount)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.command(name="shutdown")
    async def shutdown(self, context):
        """
        Make the bot shutdown. (!shutdown)
        """
        if context.message.author.id in owners:
            embed = discord.Embed(
                description="Shutting down. Bye! :wave:",
                color=0x42F56C
            )
            await context.send(embed=embed)
            await self.bot.close()
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.command(name="say", aliases=["echo"])
    async def say(self, context, *, args):
        """
        The bot will say anything you want. (!say *message*)
        """
        if context.message.author.id in owners:
            await context.message.delete()
            await context.send(args)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.group(name="marks")
    async def marks(self, context):
        """
        Lets you add or remove marks. (!marks add *teamno* *marks*) (!marks remove)
        """
        # purged_messages = await context.message.channel.purge(limit=5)
        await context.message.delete()
        one = db["team-1"]
        two = db["team-2"]
        three = db["team-3"]
        four = db["team-4"]
        five = db["team-5"]
        six = db["team-6"]
        seven = db["team-7"]
        eight = db["team-8"]
        nine = db["team-9"]
        if context.invoked_subcommand is None:
            embed = discord.Embed(
               	description=f"```Team 1: {one}\nTeam 2: {two}\nTeam 3: {three}\nTeam 4: {four}\nTeam 5: {five}\nTeam 6: {six}\nTeam 7: {seven}\nTeam 8: {eight}\nTeam 9: {nine}```",
               	color=0x0000FF
            )
            await context.send(embed=embed)

    @marks.command(name="add")
    async def marks_add(self, context, teamno, marks):
        """
        Lets you give marks to the team. (!marks add *team-x* *marks*)
        """
        if context.message.author.id in owners:
            try:
                value=db[teamno]
                value1=int(value)+int(marks)
                db[teamno] = value1
                embed = discord.Embed(
                    title="Marks added",
                    description="You gave {}, {} marks".format(teamno, marks),
                    color=0x42F56C
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description="An unknown error occurred. Contact Bot Admin.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command. Contact Bot Admin.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @marks.command(name="remove")
    async def marks_remove(self, context):
        """
        Lets you clear all team marks from the bot database.(!marks remove)
        """
        if context.message.author.id in owners:
            try:
                db["team-1"] = 0
                db["team-2"] = 0
                db["team-3"] = 0
                db["team-4"] = 0
                db["team-5"] = 0
                db["team-6"] = 0
                db["team-7"] = 0
                db["team-8"] = 0
                db["team-9"] = 0
                embed = discord.Embed(
                    title="Marks cleared",
                    color=0x42F56C
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Error in clearing marks. Contact Owner.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command. Contact Bot Admin.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.command(name="uploadppt")
    async def uploadppt(self, ctx):
        """
        Uploads ppt. (ppt name must be presentation.pptx) (!uploadppt) 
        """
        if ctx.message.author.id in owners:
            attachment = ctx.message.attachments[0]
            print(attachment.url)
            for attachment in ctx.message.attachments:
                await attachment.save(attachment.filename)
            await ctx.send("File saved Successfully.")
            changemessage = await ctx.send("Please wait.....")
            convertapi.api_secret = os.environ['convertapi']
            convertapi.convert('jpg', { 'File': '/home/runner/TVRQCBOT/presentation.pptx'
}, from_format = 'pptx').save_files('/home/runner/TVRQCBOT/') 
            await changemessage.edit(content="Done.")
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)

    @commands.command(name="deleteppt")
    async def deleteppt(self, ctx):
        """
        Uploads ppt. (!deleteppt) 
        """
        if ctx.message.author.id in owners:
            os.remove("presentation.pptx")
            await ctx.send("File removed Successfully.")
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)

    @commands.command(name="slide")
    async def slide(self, context, number):
        """
        Sends slide. (!slide *number*)
        """
        if context.message.author.id in owners:
            await context.message.delete()
            number=int(number)
            if(number==1):
                for channelo in teamchannels:
                    file = discord.File(f"presentation.jpg")
                    e = discord.Embed(color=0x42F56C)
                    e.set_image(url=f"attachment://presentation.jpg")
                    channel = self.bot.get_channel(channelo)
                    await channel.send(file = file, embed=e)
                await context.send(f"Sent Slide Number: {number}.")
            elif(number<1):
                await context.send("Enter no. greater than 0")
            else:
                for channelo in teamchannels:
                    file = discord.File(f"presentation-{number}.jpg")
                    e = discord.Embed(color=0x42F56C)
                    e.set_image(url=f"attachment://presentation-{number}.jpg")
                    channel = self.bot.get_channel(channelo)
                    await channel.send(file = file, embed=e)
                await context.send(f"Sent Slide Number: {number}.")
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.command(name="timer")
    async def timer(self, ctx, seconds):
        """
        Starts timer (Must be less than 900 sec) (!timer *Seconds*)
        """
        if ctx.message.author.id in owners:
            try:
                await ctx.message.delete()
                secondint = int(seconds)
                if secondint > 900:
                    await ctx.send("I dont think im allowed to do go above 900 seconds.")
                    raise BaseException
                if secondint <= 0:
                    await ctx.send("I dont think im allowed to do negatives")
                    raise BaseException
                message = await ctx.send("Timer: {seconds}")
                while True:
                    secondint -= 1
                    if secondint == 0:
                        await message.edit(content="Ended!")
                        break
                    await message.edit(content=f"Timer: {secondint}")
                    await asyncio.sleep(1)
                await ctx.send("Time's up!")
            except ValueError:
                await ctx.send("Must be a number!")
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
    @commands.command(name="givemarks")
    async def givemarks(self, context):
        """
        Gives marks after round ends. (!givemarks *no of teams*)
        """
        if context.message.author.id in owners:
            row_of_buttons = ActionRow(
            Button(
                style=ButtonStyle.red,
                label="-10",
                custom_id="-10"
            ),
            Button(
                style=ButtonStyle.red,
                label="-5",
                custom_id="-5"
            ),
            Button(
                style=ButtonStyle.blurple,
                label="0",
                custom_id="0"
            ),
            Button(
                style=ButtonStyle.green,
                label="5",
                custom_id="5"
            ),
            Button(
                style=ButtonStyle.green,
                label="10",
                custom_id="10"
            )
            )
            for i in range(1,10):
                keyy=f"team-{i}-answer"
                embed = discord.Embed(
                title=f"Give marks to team {i}",
                color=0x42F56C
                )
                embed.add_field(
                    name="Answer:",
                    value=db[keyy]
                )
                embed2 = discord.Embed(
                title=f"Marks to team {i}",
                color=0x42F56C
                )
                await context.send(embed=embed,components=[row_of_buttons])
                def check(inter):
                    return inter.message.id
                inter = await context.wait_for_button_click(check)
                button_text = inter.clicked_button.label
                button_text=int(button_text)
                channel1=f"team-{i}"
                if button_text == -10:
                    value=db[channel1]
                    value1=int(value)+int(-10)
                    db[channel1] = value1
                    embed2.add_field(
                    name="Points given:",
                    value="-10",
                    inline=True
                    )
                if button_text == -5:
                    value=db[channel1]
                    value1=int(value)+int(-5)
                    db[channel1] = value1
                    embed2.add_field(
                    name="Points given:",
                    value="-5",
                    inline=True
                    )
                if button_text == 0:
                    value=db[channel1]
                    value1=int(value)+int(0)
                    db[channel1] = value1
                    embed2.add_field(
                    name="Points given:",
                    value="0",
                    inline=True
                    )
                if button_text == 5:
                    value=db[channel1]
                    value1=int(value)+int(5)
                    db[channel1] = value1
                    embed2.add_field(
                    name="Points given:",
                    value="5",
                    inline=True
                    )
                if button_text == 10:
                    value=db[channel1]
                    value1=int(value)+int(10)
                    db[channel1] = value1
                    embed2.add_field(
                    name="Points given:",
                    value="10",
                    inline=True
                    )
                channel2 = self.bot.get_channel(890335796383604777)
                await channel2.send(embed=embed2)
                await inter.reply("Successfull")
            db["team-1-answer"] = 0
            db["team-2-answer"] = 0
            db["team-3-answer"] = 0
            db["team-4-answer"] = 0
            db["team-5-answer"] = 0
            db["team-6-answer"] = 0
            db["team-7-answer"] = 0
            db["team-8-answer"] = 0
            db["team-9-answer"] = 0
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            
    @commands.command(name="broadcast")
    async def broadcast(self, context, *,args):
        """
        Sends broadcast to all teams. (!broadcast *message*)
        """
        if context.message.author.id in owners:
            for channelo in teamchannels:
                channel = self.bot.get_channel(channelo)
                await channel.send(f"```{args}```")
            await context.send(f"Broadcasted ```{args}```")
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
    bot.add_cog(general(bot))
    bot.add_cog(owner(bot))
