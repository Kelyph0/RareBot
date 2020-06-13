import requests as req
import json
from os import system, listdir
from random import choice

from discord.ext import commands

class Distractions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Distractions Cog has been loaded\n-----")

    async def get_joke_categories(self):
        r = req.get("https://sv443.net/jokeapi/v2/categories")
        result = "The available categories are: \n-----"
        for category in json.loads(r.text)["categories"]:
            result += "\t{}\n-----".format(category)
        return result

    def get_joke(self, category):
        r = req.get("https://sv443.net/jokeapi/v2/joke/{}".format(category))
        data = json.loads(r.text)
        if data["type"] == "single":
            return data["joke"]
        else:
            return "{}\n-----{}".format(data["setup"], data["delivery"])

    def get_meme(self, category):
        system('cd ../skraper-master;./skraper ninegag /{} -t json -n 100'.format(category))
        file = listdir('../skraper-master/ninegag')
        f = open("../skraper-master/ninegag/{}".format(file[0]))
        data = json.load(f)
        f.close()
        system('rm ../skraper-master/ninegag/*')
        selection = data[choice(range(len(data)))]
        return "{}\n-----{}".format(selection["text"], selection["media"][0]["url"])


def setup(bot):
    bot.add_cog(Distractions(bot))