from nextcord import Interaction
import nextcord
async def set_join(inter: Interaction,channel:nextcord.TextChannel|None,guild):
    if channel is None:
        channel_id= inter.channel_id
        await guild.update_one({"guild": inter.guild.id}, {"$set": {"join":{"id_channel":channel_id}}})
    else:
        channel_id= channel.id
        await guild.update_one({"guild": inter.guild.id}, {"$set": {"join":{"id_channel":channel_id}}})
    embed=nextcord.Embed(color=0xdc4700,description=f"<#{channel_id}> set join แล้วจ้า")
    await inter.send(embed=embed)
    
async def set_leave(inter: Interaction,channel:nextcord.TextChannel|None,guild):
    if channel is None:
        channel_id= inter.channel_id
        await guild.update_one({"guild": inter.guild.id}, {"$set": {"leave":{"id_channel":channel_id}}})
    else:
        channel_id= channel.id
        await guild.update_one({"guild": inter.guild.id}, {"$set": {"leave":{"id_channel":channel_id}}})
    embed=nextcord.Embed(color=0xdc4700,description=f"<#{channel_id}> set leave แล้วจ้า")
    await inter.send(embed=embed)
    
async def set_report(inter: Interaction,channel:nextcord.TextChannel|None,guild):
    if channel is None:
        channel_id= inter.channel_id
        await guild.update_one({"guild": inter.guild.id}, {"$set": {"report":{"id_channel":channel_id}}})
    else:
        channel_id= channel.id
        await guild.update_one({"guild": inter.guild.id}, {"$set": {"report":{"id_channel":channel_id}}})
    embed=nextcord.Embed(color=0xdc4700,description=f"<#{channel_id}> set report แล้วจ้า")
    await inter.send(embed=embed)