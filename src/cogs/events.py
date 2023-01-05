import nextcord
from nextcord import user
from nextcord.ext.commands import AutoShardedBot,Cog
from database import guild as guild_collet
class all_events(Cog):
    def __init__(self, bot: AutoShardedBot):
        self.bot = bot

    @Cog.listener()
    async def on_guild_join(self, guild):
        await self.bot.wait_until_ready()
        print(guild.id)
        
        await guild_collet.insert_one({"guild":guild.id})
    @Cog.listener()
    async def on_guild_remove(self, guild):
        await self.bot.wait_until_ready()
        if guild_collet.find_one({"guild": guild.id}):
            await guild_collet.delete_one({"guild":guild.id})
def setup(bot: AutoShardedBot) -> None:
    bot.add_cog(all_events(bot))