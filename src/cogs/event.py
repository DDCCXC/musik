import nextcord
from nextcord import user
from nextcord.ext import commands
from database import guild as guild_collet

class all_events(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        guild_collet.insert_one(guild.id)