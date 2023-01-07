import nextcord
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
    if ty=="join": 
        title=embed_sitting.get("title","Welcome to <name(guild)>")
        description=embed_sitting.get("description","Welcome <mantion(user)>" )
        color=literal_eval(embed_sitting.get("color","0xdc4700"))
        image=embed_sitting.get("image","https://images-ext-2.discordapp.net/external/72u7pCkEPUfaXZu7t1OB0FX4AsCUnCryPqZQPHOiGk4/https/miro.medium.com/max/1400/0%2AcUpkVai00QRZHYDu?width=994&height=662")
    elif ty=="leave":
        title=embed_sitting.get("title","See u nekst time")
        description=embed_sitting.get("description","See u nekst time <mantion(user)>")
        color=literal_eval(embed_sitting.get("color","0xdc4700"))
        image=embed_sitting.get("image","https://images-ext-2.discordapp.net/external/72u7pCkEPUfaXZu7t1OB0FX4AsCUnCryPqZQPHOiGk4/https/miro.medium.com/max/1400/0%2AcUpkVai00QRZHYDu?width=994&height=662")
        
    thumbnail=embed_sitting.get("thumbnail","!img(guild)")
    auth_icon=embed_sitting.get("auth_icon","!img(user)")
    auth_text=embed_sitting.get("auth_text","<name(user)>")
    footer_icon=embed_sitting.get("footer_icon","!img(none)")
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
            
async def JOIN_LEAVE(type_,guild_collet,member):
    guild=await guild_collet.find_one({"guild": member.guild.id}) 
    if guild is None :
            return
    if type_ not in  guild :
            return
    channel=member.guild.get_channel(guild[type_]["id_channel"])
    if channel is None:
            return
    await channel.send(embed=create_embed(type_,guild[type_].get("embed",{}),member))