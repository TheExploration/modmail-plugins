import discord
from discord.ext import commands

import requests

from box import Box

from core.paginator import EmbedPaginatorSession

class RedditScroller(commands.Cog):
    """See cursed images"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cursedimages(self, ctx):
        """Scroll through cursed images."""
        subreddit = "cursedimages"
        r = requests.get(f"https://api.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=10",
                     headers={'User Agent': 'Super Bot 9000'}).json()
        ctx.send(r)
        r = Box(r)

        embeds = []

        for data in r.data.children.data:
            ctx.send(data)

def setup(bot):
    bot.add_cog(RedditScroller(bot))