from nextcord import Interaction
import nextcord
async def create_DJ(inter: Interaction,role:nextcord.Role|None,guild):
    if role is None:
        role=await inter.guild.create_role(name="DJ",colour=0xdc4700)
        await guild.update_one({"guild": inter.guild.id}, {"$set": {"DJ_Role":role.id}})
    else:
        await guild.update_one({"guild": inter.guild.id}, {"$set": {"DJ_Role":role.id}})
    embed=nextcord.Embed(color=0xdc4700,description=f"<@&{role.id}> เป็นdjแล้ว")
    await inter.send(embed=embed)