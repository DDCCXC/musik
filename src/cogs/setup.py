
from nextcord import Interaction, slash_command,message_command
from nextcord.ext.commands import AutoShardedBot, Cog
from database import GUILD
import nextcord
from commands.setupa import *
from events.join_leave import JOIN_LEAVE
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
        await create_DJ(inter,role,GUILD)
        
    @join_leave.subcommand(name="set-join", description="Asdasd")
    async def set_join(self, inter: Interaction,channel:nextcord.TextChannel=nextcord.SlashOption(name="channel",default=None)) -> None:
        await set_join(inter,channel,GUILD)
        
    @join_leave.subcommand(name="custom-join", description="Asdasd")
    async def customjoin(self, inter: Interaction,contain:str=nextcord.SlashOption(name="contain",
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
        ,volume:str=nextcord.SlashOption(name="leave")) -> None:
        await custom(inter,"join",contain,volume,GUILD)
        
    @join_leave.subcommand(name="custom-leave", description="Asdasd")
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
        await custom(inter,"leave",contain,volume,GUILD)
        
    @join_leave.subcommand(name="set-leave", description="Asdasd")
    async def set_leave(self, inter: Interaction,channel:nextcord.TextChannel=nextcord.SlashOption(name="channel",default=None)) -> None:
        await set_leave(inter,channel,GUILD)
    
    @join_leave.subcommand(name="upload-image-join", description="Asdasd")
    async def upload_image(self, inter: Interaction,contain:str=nextcord.SlashOption(name="contain",
    choices=[
        "image",
        "thumbnail",
        "auth_icon",
        "footer_icon",
        ])
        ,volume:nextcord.Attachment=nextcord.SlashOption(name="image")) -> None:
        await download(inter,"join",contain,volume,GUILD)
    @join_leave.subcommand(name="upload-image-leave", description="Asdasd")
    async def upload_image(self, inter: Interaction,contain:str=nextcord.SlashOption(name="contain",
    choices=[
        "image",
        "thumbnail",
        "auth_icon",
        "footer_icon",
        ])
        ,volume:nextcord.Attachment=nextcord.SlashOption(name="image")) -> None:
        await download(inter,"leave",contain,volume,GUILD)
        
    @join_leave.subcommand(name="set-report", description="Asdasd")
    async def set_report(self, inter: Interaction,channel:nextcord.TextChannel=nextcord.SlashOption(name="channel",default=None)) -> None:
        await set_report(inter,channel,GUILD)
    
    @join_leave.subcommand(name="sudo-join", description="Asdasd")
    async def sudo_join(self, inter: Interaction) -> None:
        await JOIN_LEAVE("join",GUILD,inter.user)
        await inter.send(embed=nextcord.Embed(color=0xdc4700,title="request ไปแล้วจ้า"))
    
    @join_leave.subcommand(name="sudo-leave", description="Asdasd")
    async def sudo_leave(self, inter: Interaction) -> None:
        await JOIN_LEAVE("leave",GUILD,inter.user)
        await inter.send(embed=nextcord.Embed(color=0xdc4700,title="request ไปแล้วจ้า"))
    @message_command(name="report", force_global=True)
    async def report(self, inter: Interaction, message: nextcord.Message) -> None:
        await report(self,inter,message,GUILD)
def setup(bot: AutoShardedBot) -> None:
    bot.add_cog(setup_commands(bot))