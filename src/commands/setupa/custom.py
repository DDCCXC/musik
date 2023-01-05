from nextcord import Interaction
import nextcord
    
LIMIT_CHAR={
    "title":256,
    "description":4096,
    "author":256,
    "footer":2048,
}
# +-------------+------------------------+
# |    Field    |         Limit          |
# +-------------+------------------------+
# | title       | 256 characters         |
# | description | 4096 characters*       |
# | fields      | Up to 25 field objects |
# | field.name  | 256 characters         |
# | field.value | 1024 characters        |
# | footer.text | 2048 characters        |
# | author.name | 256 characters         |
# +-------------+------------------------+
    
async def custom(inter: Interaction,typecustom:str,contain:str,volume:str,guild):
    embed=nextcord.Embed(color=0xdc4700)
    if contain not in ["color","image","thumbnail","auth_icon","footer_icon"]:
        if len(volume) >= LIMIT_CHAR[contain]:
            embed.description=f"{contain}ต้องไม่เกิน {LIMIT_CHAR[contain]} ตัวอักษร"
            await inter.send(embed=embed)
            return
    
    await guild.update_one({"guild": inter.guild.id}, {"$set": {f"{typecustom}.embed":{contain:volume}}})
    embed.description="custom แล้วจ้า"
    
    
    await inter.send(embed=embed)