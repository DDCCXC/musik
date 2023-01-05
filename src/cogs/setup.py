
from nextcord import Interaction, slash_command
from nextcord.ext.commands import AutoShardedBot, Cog
from database import guild
import nextcord
from commands.setupa import create_DJ
class setup_commands(Cog):
    def __init__(self, bot: AutoShardedBot) -> None:
        self.bot = bot
    @slash_command(force_global=True)
    async def setup(self,inter: nextcord.Interaction):...
    @setup.subcommand()
    async def muzik(self,inter: nextcord.Interaction):...
    
    @muzik.subcommand(name="create-role-dj", description="Asdasd")
    async def create_Dj(self, inter: Interaction,role:nextcord.Role=nextcord.SlashOption(name="role",default=None)) -> None:
        await create_DJ(inter,role,guild)
def setup(bot: AutoShardedBot) -> None:
    bot.add_cog(setup_commands(bot))