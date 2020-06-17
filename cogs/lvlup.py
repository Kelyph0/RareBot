from discord.ext import commands, tasks
import json
import datetime
from random import randint

epoch = datetime.datetime.utcfromtimestamp(0)
time_diff = round((datetime.datetime.utcnow() - epoch).total_seconds())

class lvlup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.content.startswith('B.') is not True:

            if ctx.guild != None:

                F = open("./bot_config/level.json")

                level = json.load(F)

                user_time = round((datetime.datetime.utcnow() - epoch).total_seconds())

                if str(f"{ctx.guild.id}") not in level:
                    level[f"{ctx.guild.id}"] = {}
                    print(f"Guild file has been created for {ctx.guild.id}/{ctx.guild.name}")

                if str(f"{ctx.author.id}") not in level[f"{ctx.guild.id}"]:

                    level[f"{ctx.guild.id}"][f"{ctx.author.id}"] = {"level" : "1", "xp" : "0", "NT" : f"0", "multi" : f"1", "txp" : f"0", "starttime" : f"{user_time}"}

                if user_time - int(level[f"{ctx.guild.id}"][f"{ctx.author.id}"]["NT"]) >= 60:
                    RNum = randint(1, 5)
                    MP = int(level[f"{ctx.guild.id}"][f"{ctx.author.id}"]["multi"])
                    XP = int(level[f"{ctx.guild.id}"][f"{ctx.author.id}"]["xp"]) + (RNum * MP)
                    TXP = int(level[f"{ctx.guild.id}"][f"{ctx.author.id}"]["txp"]) + (RNum * MP)
                    LVL = int(level[f"{ctx.guild.id}"][f"{ctx.author.id}"]["level"])

                    if XP >= 20*LVL**2:
                        XP = XP % (20*LVL**2)
                        LVL += 1

                        F1 = open("./bot_config/currency.json")
                        mon = json.load(F1)

                        if str(f"{ctx.author.id}") not in mon:
                            mon[f"{ctx.author.id}"] = {"money" : "0", "hist" : "0", "multimon" : "1"}

                        RNum1 = randint(1, 25)
                        MM = int(mon[f"{ctx.author.id}"]["multimon"])
                        Money = int(mon[f"{ctx.author.id}"]["money"]) + round(RNum1 * (LVL + 1) * MM)
                        HMoney = int(mon[f"{ctx.author.id}"]["hist"]) + round(RNum1 * (LVL + 1) * MM)

                        F1.close()

                        mon[f"{ctx.author.id}"]["money"] = f"{Money}"
                        mon[f"{ctx.author.id}"]["hist"] = f"{HMoney}"
                        level[f"{ctx.guild.id}"][f"{ctx.author.id}"][f"level"] = f"{LVL}"
                        level[f"{ctx.guild.id}"][f"{ctx.author.id}"][f"xp"] = f"{XP}"

                        with open("./bot_config/currency.json", "w") as F1w:
                            json.dump(mon, F1w)

                        print(f"{ctx.author.name}\nXP: {XP}\nLevel: {LVL}")

                    XP = int(level[f"{ctx.guild.id}"][f"{ctx.author.id}"]["xp"])

                    level[f"{ctx.guild.id}"][f"{ctx.author.id}"][f"multi"] = f"{MP}"
                    level[f"{ctx.guild.id}"][f"{ctx.author.id}"][f"xp"] = f"{XP}"
                    level[f"{ctx.guild.id}"][f"{ctx.author.id}"][f"txp"] = f"{TXP}"
                    level[f"{ctx.guild.id}"][f"{ctx.author.id}"][f"NT"] = f"{user_time}"

                    ttime = (user_time) - round(int(level[f"{ctx.guild.id}"][f"{ctx.author.id}"]["starttime"]))

                    F.close()

                    with open("./bot_config/level.json", "w") as Fw:
                        json.dump(level, Fw)

                    anlvl = int(level[f"{ctx.guild.id}"][f"{ctx.author.id}"]["level"])
                    ttimeday = int(int(ttime) / 86400)
                    ttimehour = int((int(ttime) % 86400) / 3600)
                    ttimemin = int(((int(ttime) % 86400) % 3600) / 60)
                    if ttimeday == int(1): tday = ""
                    else: tday = "s"
                    if ttimehour == int(1): thour = ""
                    else: thour = "s"
                    if ttimemin == int(1): tmin = ""
                    else: tmin = "s"
                    msgtt = f"{ttimeday} day{tday}, {ttimehour} hour{thour}, and {ttimemin} minute{tmin}"
                    if anlvl in [10, 20, 25, 50, 75, 100, 150, 200, 300]:
                        print(f"CONGRATS! {ctx.author.mention} has made it to level {anlvl} in just {msgtt}!")
                        channel = self.bot.get_channel(722820388253466635)
                        await channel.send(f"{ctx.author.mention} has reached level {anlvl} in {msgtt}!")


def setup(bot):
    bot.add_cog(lvlup(bot))