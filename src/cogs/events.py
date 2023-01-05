import nextcord
from nextcord import member
from nextcord.ext.commands import AutoShardedBot,Cog
from database import guild as guild_collet
class all_events(Cog):
    def __init__(self, bot: AutoShardedBot):
        self.bot = bot

    @Cog.listener()
    async def on_guild_join(self, guild):
        await self.bot.wait_until_ready()
        print(guild.id)
        if await guild_collet.find_one({"guild": guild.id}) is None:
            await guild_collet.insert_one({"guild":guild.id})
    @Cog.listener()
    async def on_guild_remove(self, guild):
        await self.bot.wait_until_ready()
        if await guild_collet.find_one({"guild": guild.id}) is not None:
            await guild_collet.delete_one({"guild":guild.id})
            
    @Cog.listener()
    async def on_member_join(self, member:member.Member):
        await self.bot.wait_until_ready()
        guild=await guild_collet.find_one({"guild": member.guild.id}) 
        if guild is None or guild["join"] is None:
            return
        channel=member.guild.get_channel(guild["join"]["id_channel"])
        await channel.send("join")
    @Cog.listener()
    async def on_member_remove(self, member:member.Member):
        await self.bot.wait_until_ready()
        guild=await guild_collet.find_one({"guild": member.guild.id}) 
        if guild is None:
            return
        if  guild["leave"] is None:
            return
        channel=member.guild.get_channel(guild["leave"]["id_channel"])
        await channel.send("leave")
def setup(bot: AutoShardedBot) -> None:
    bot.add_cog(all_events(bot))