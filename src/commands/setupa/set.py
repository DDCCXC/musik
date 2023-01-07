from nextcord import Interaction
import nextcord
async def set_room(type_channel:str,inter: Interaction,channel:nextcord.TextChannel|None,guild):
    if channel is None:
        channel_id= inter.channel_id
        await guild.update_one({"guild": inter.guild.id}, {"$set": {type_channel:{"id_channel":channel_id}}})
    else:
        channel_id= channel.id
        await guild.update_one({"guild": inter.guild.id}, {"$set": {type_channel:{"id_channel":channel_id}}})
    embed=nextcord.Embed(color=0xdc4700,description=f"<#{channel_id}> set {type_channel} แล้วจ้า")
    await inter.send(embed=embed)