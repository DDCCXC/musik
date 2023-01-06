from nextcord import Interaction
import nextcord
    

async def download(inter: Interaction,typecustom:str,contain:str,volume:nextcord.Attachment,guild):
    embed=nextcord.Embed(color=0xdc4700)
    if contain not in ["color","image","thumbnail","auth_icon","footer_icon"]:
        if "image" not in volume.content_type:
            embed.description="image onlyจ้า"
            return await inter.send(embed=embed)
    await guild.update_one({"guild": inter.guild.id}, {"$set": {f"{typecustom}.embed":{contain:volume.proxy_url}}})
    embed.description="custom แล้วจ้า"
    
    
    await inter.send(embed=embed)