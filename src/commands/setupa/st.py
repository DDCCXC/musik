from nextcord import Interaction
import nextcord
async def create_DJ(inter: Interaction,role:nextcord.Role|None,guild):
    if role is None:
        dj=await inter.guild.create_role(name="DJ")
        await guild.insert_one({"dj_role":dj.id})
    ...