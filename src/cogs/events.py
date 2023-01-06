import nextcord
from nextcord import member
from nextcord.ext.commands import AutoShardedBot,Cog
from database import guild as guild_collet
from ast import literal_eval
def decode_text(text:str,user:nextcord.Member)->str:
    return text\
                .replace("<mantion(user)>",user.mention)\
                .replace("<name(user)>",user.name)\
                .replace("<id(user)>",str(user.id))\
                .replace("<join_at(user)>", str(user.joined_at))\
                .replace("<none>", "")\
                .replace("<name(guild)>", user.guild.name)\
                .replace("<id(guild)>", str(user.guild.id))
                               
def decode_image(text:str,user:nextcord.Member)->str:
    return text\
                .replace("!img(guild)",str(user.guild.icon.url))\
                .replace("!img(user)",user.avatar.url)\
                .replace("!img(none)","")\

def create_embed(ty:str,embed_sitting,user)->nextcord.Embed:
    embed_sitting = [] if embed_sitting is None else embed_sitting
    if ty=="join": 
        title=embed_sitting.get("title","Welcome to <name(guild)>")
        description=embed_sitting.get("description","Welcome <mantion(user)>" )
        color=literal_eval(embed_sitting.get("color",0xdc4700))
        image=embed_sitting.get("image","https://images-ext-2.discordapp.net/external/72u7pCkEPUfaXZu7t1OB0FX4AsCUnCryPqZQPHOiGk4/https/miro.medium.com/max/1400/0%2AcUpkVai00QRZHYDu?width=994&height=662")
    elif ty=="leave":
        title=embed_sitting.get("title","See u nekst time")
        description=embed_sitting.get("See u nekst time <mantion(user)>")
        color=literal_eval(embed_sitting.get("color",0xdc4700))
        image=embed_sitting.get("image","https://images-ext-2.discordapp.net/external/72u7pCkEPUfaXZu7t1OB0FX4AsCUnCryPqZQPHOiGk4/https/miro.medium.com/max/1400/0%2AcUpkVai00QRZHYDu?width=994&height=662")
        
    thumbnail=embed_sitting.get("thumbnail","!img(guild)")
    auth_icon=embed_sitting.get("auth_icon","!img(user)")
    auth_text=embed_sitting.get("auth_text","<name(user)>")
    footer_icon=embed_sitting.get("footer_icon","!img(user)")
    footer_text=embed_sitting.get("footer_text","<join_at(user)>")
    return nextcord.Embed(
            title=decode_text(title,user),
            description=decode_text(description,user),
            color=color,
            ).set_author(
                name=decode_text(auth_text,user),
                icon_url=decode_image(auth_icon,user)
            ).set_footer(
                text=decode_text(footer_text,user),
                icon_url=decode_image(footer_icon,user)
            ).set_image(
                url=decode_image(image,user)
            ).set_thumbnail(
                url=decode_image(thumbnail,user)
            )
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
    async def on_member_join(self, member:nextcord.Member):
        await self.bot.wait_until_ready()
        guild=await guild_collet.find_one({"guild": member.guild.id}) 
        if guild is None :
            return
        if "join" not in  guild :
            return
        channel=member.guild.get_channel(guild["join"]["id_channel"])
        if channel is None:
            return
        await channel.send(embed=create_embed("join",guild["join"].get("embed",None),member))
        
        
    @Cog.listener()
    async def on_member_remove(self, member:nextcord.Member):
        await self.bot.wait_until_ready()
        guild=await guild_collet.find_one({"guild": member.guild.id}) 
        if guild is None :
            return
        if "leave" not in  guild :
            return
        channel=member.guild.get_channel(guild["leave"]["id_channel"])
        if channel is None:
            return
        await channel.send(embed=create_embed("leave",guild["leave"].get("embed",None),member))
        
def setup(bot: AutoShardedBot) -> None:
    bot.add_cog(all_events(bot))