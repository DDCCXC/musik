
from nextcord import Interaction, slash_command
from nextcord.ext.commands import AutoShardedBot, Cog
from database import guild
import nextcord
from commands.setupa import *
class setup_commands(Cog):
    def __init__(self, bot: AutoShardedBot) -> None:
        self.bot = bot
    @slash_command(force_global=True)
    async def setup(self,inter: nextcord.Interaction):...
    @setup.subcommand()
    async def muzik(self,inter: nextcord.Interaction):...
    @setup.subcommand()
    async def join_leave(self,inter: nextcord.Interaction):...
    @muzik.subcommand(name="create-role-dj", description="Asdasd")
    async def create_Dj(self, inter: Interaction,role:nextcord.Role=nextcord.SlashOption(name="role",default=None)) -> None:
        await create_DJ(inter,role,guild)
        
    @join_leave.subcommand(name="set-join", description="Asdasd")
    async def set_join(self, inter: Interaction,channel:nextcord.TextChannel=nextcord.SlashOption(name="channel",default=None)) -> None:
        await set_join(inter,channel,guild)
    @join_leave.subcommand(name="custom-join", description="Asdasd")
    async def customj(self, inter: Interaction,contain:str=nextcord.SlashOption(name="contain",
    choices=[
        "title",
        "descript",
        "color",
        "image",
        "thumbnail",
        "auth_icon",
        "auth_text",
        "footer_icon",
        "footer_text"
        ])
        ,volume:str=nextcord.SlashOption(name="volume")) -> None:
        await custom(inter,"join",contain,volume,guild)
    @join_leave.subcommand(name="custom-join", description="Asdasd")
    async def customleave(self, inter: Interaction,contain:str=nextcord.SlashOption(name="contain",
    choices=[
        "title",
        "descript",
        "color",
        "image",
        "thumbnail",
        "auth_icon",
        "auth_text",
        "footer_icon",
        "footer_text"
        ])
        ,volume:str=nextcord.SlashOption(name="volume")) -> None:
        await custom(inter,"leave",contain,volume,guild)
    @join_leave.subcommand(name="set-leave", description="Asdasd")
    async def set_leave(self, inter: Interaction,channel:nextcord.TextChannel=nextcord.SlashOption(name="channel",default=None)) -> None:
        await set_leave(inter,channel,guild)
def setup(bot: AutoShardedBot) -> None:
    bot.add_cog(setup_commands(bot))