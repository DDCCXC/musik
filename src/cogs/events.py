import nextcord
from nextcord.ext.commands import AutoShardedBot,Cog
from database import GUILD
from events.join_leave import JOIN_LEAVE
class all_events(Cog):
    def __init__(self, bot: AutoShardedBot):
        self.bot = bot

    @Cog.listener()
    async def on_guild_join(self, guild):
        await self.bot.wait_until_ready()
        print(guild.id)
        if await GUILD.find_one({"guild": guild.id}) is None:
            await GUILD.insert_one({"guild":guild.id})
    @Cog.listener()
    async def on_guild_remove(self, guild):
        await self.bot.wait_until_ready()
        if await GUILD.find_one({"guild": guild.id}) is not None:
            await GUILD.delete_one({"guild":guild.id})
            
    @Cog.listener()
    async def on_member_join(self, member:nextcord.Member):
        await self.bot.wait_until_ready()
        await JOIN_LEAVE("join",GUILD,member)
        
    @Cog.listener()
    async def on_member_remove(self, member:nextcord.Member):
        await self.bot.wait_until_ready()
        await JOIN_LEAVE("leave",GUILD,member)
        
def setup(bot: AutoShardedBot) -> None:
    bot.add_cog(all_events(bot))